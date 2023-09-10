from env import Env
from chatgpt.chatgpt_service import ChatGPTService
from voiceprompt.voiceprompt_service import VoicePrompt
from preprocessing.preprocessing_text import TextPreprocessing

from telegram import Update
from telegram.constants import ChatAction
from collections import deque
import asyncio


RESPONSE_QUEUE = deque()
READ_DELAY_QUEUE = deque()
cur_message_id = 0


class QueuingService:

    @classmethod
    async def send_message(cls, context_message: Update.message, reply_message: str, reply_type: str):
        try:
            if reply_type == 'text':
                print('sending')
                await context_message.reply_text(reply_message)
                print('sent')
            elif reply_type == 'voice':
                print('recording')
                await context_message.reply_chat_action(ChatAction.RECORD_VOICE)
                voice_path = await VoicePrompt.text_to_speech(reply_message)
                voice = open(voice_path, 'rb')

                await context_message.reply_voice(voice)
                voice.close()
                print('sent')
        except Exception as e:
            print(e)

        await cls.queue_message_start()

    @classmethod
    async def send_delay_message(cls, context_message: Update.message, reply_message: str, reply_type: str):
        word_count = len(reply_message.split(' '))
        type_delay = int((word_count / Env.DEFAULT_TYPE_WPM) * 60) + 3

        if reply_type == 'text':
            print('typing, ', type_delay)
            await context_message.reply_chat_action(ChatAction.TYPING)
            await asyncio.sleep(type_delay)

        await cls.send_message(context_message, reply_message, reply_type)

    @classmethod
    async def queue_message_start(cls):
        global RESPONSE_QUEUE, READ_DELAY_QUEUE
        global cur_message_id

        if len(RESPONSE_QUEUE) > 0:
            message_id, context_message, reply_message, reply_type = RESPONSE_QUEUE.popleft()

            if len(READ_DELAY_QUEUE) > 0:
                read_delay = READ_DELAY_QUEUE.popleft()

                try:
                    print('read, ', read_delay)
                    await asyncio.sleep(read_delay)
                except Exception as e:
                    print(e)

            await cls.send_delay_message(context_message, reply_message, reply_type)

    @classmethod
    async def send_messages(cls, context_message: Update.message, chat_id: int, user_name: str, user_message: str,
                            reply_type: str = 'text'):
        global RESPONSE_QUEUE, READ_DELAY_QUEUE
        global cur_message_id

        try:
            word_count = len(user_message.split(' '))
            read_delay = int((word_count / Env.DEFAULT_READ_WPM) * 60) + 6
            READ_DELAY_QUEUE.append(read_delay)

            weighted_answer = ChatGPTService.get_weighted_answer(chat_id, user_name, user_message)

            if weighted_answer == '':
                await cls.queue_message_start()
                return

            if reply_type == 'text':
                sentences = TextPreprocessing.get_sentences(weighted_answer)

                for sentence in sentences:
                    sentence = sentence if sentence[-1] != '.' else sentence[:-1]
                    RESPONSE_QUEUE.append((cur_message_id, context_message, sentence, reply_type))
                    cur_message_id += 1

                response_count = len(sentences)

                if len(RESPONSE_QUEUE) == response_count:
                    await cls.queue_message_start()
            elif reply_type == 'voice':
                RESPONSE_QUEUE.append((cur_message_id, context_message, weighted_answer, reply_type))

                await cls.queue_message_start()

        except Exception as e:
            print(e)

    @classmethod
    async def send_voice_messages(cls, context_message: Update.message, chat_id: int, user_name: str, voice_path: str):
        user_message = VoicePrompt.get_prompt_from_audio(voice_path)

        await cls.send_messages(context_message, chat_id, user_name, user_message, reply_type='voice')
