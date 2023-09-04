from env import Env
from chatgpt.chatgpt_database import ChatGPTDatabase
from customtime.customtime_service import CustomTime

import openai


class ChatGPTService:

    openai.organization = Env.OPENAI_ORG_ID
    openai.api_key = Env.OPENAI_API_KEY

    @classmethod
    def get_answer(cls, model: str, messages: list) -> str:
        result = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )

        answer = result['choices'][0]['message']['content']

        return answer

    @classmethod
    def get_weighted_answer(cls, chat_id: int, user_name: str, user_message: str):
        chat_context_data_path = ChatGPTDatabase.CONTEXT_DATA_DIR + str(chat_id) + '.dat'

        database = ChatGPTDatabase.load_chara_json()
        chat_context = ChatGPTDatabase.load_context_data(chat_context_data_path)

        temp_context = CustomTime.get_time_context() + ' '

        if chat_id == 780492181:
            temp_context += 'Kamu sedang berbalas sms dengan kakakmu, Myracle. Panggil ia kakak atau kak.'
        else:
            temp_context += f'Kamu sedang berbalas sms dengan teman kakakmu, {user_name}. '

        temp_context += f'Berikan jawaban yang singkat dan gaul, '
        temp_context += f'seolah kamu adalah seorang manusia. Maksimal 2 kalimat.'
        temp_context += f'Namun, jika kamu tidak ingin membalasnya, kamu bisa membalas dengan "X90XXX".'

        chat_context['messages'].append({"role": "system", "content": temp_context})
        chat_context['messages'].append({"role": "user", "content": user_message})

        # getting the weighted answer
        weighted_answer = cls.get_answer(Env.MODEL_NAME, database['messages'] + chat_context['messages'])

        if weighted_answer == 'X90XXX':
            weighted_answer = ''
        else:
            chat_context['messages'].append({"role": "assistant", "content": weighted_answer})
        ChatGPTDatabase.maintain_json(chat_context)
        ChatGPTDatabase.save_context_data(chat_context_data_path, chat_context)

        return weighted_answer
