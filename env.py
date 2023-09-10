from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()


class Env:

    # telegram tokens
    BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
    BOT_USERNAME: Final = os.getenv('BOT_USERNAME')

    # openai tokens
    OPENAI_API_KEY: Final = os.getenv('OPENAI_API_KEY')
    OPENAI_ORG_ID: Final = os.getenv('OPENAI_ORG_ID')

    # chatgpt
    MODEL_NAME: Final = os.getenv('MODEL_NAME')
    CHARA_NAME: Final = os.getenv('CHARA_NAME')
    CONTEXT_JSON_LINE: Final = int(os.getenv('CONTEXT_JSON_LINE'))
    CONTEXT_FERNET_KEY: Final = bytes(os.getenv('CONTEXT_FERNET_KEY'), 'utf-8')
    DEFAULT_TYPE_WPM: Final = int(os.getenv('DEFAULT_TYPE_WPM'))
    DEFAULT_READ_WPM: Final = int(os.getenv('DEFAULT_TYPE_WPM'))

    # audio prompt
    VOICE_DIR: Final = os.getenv('VOICE_DIR')
    VOICE_LANGUAGE: Final = os.getenv('VOICE_LANGUAGE')
    VOICE_MODEL_PATH: Final = os.getenv('VOICE_MODEL_PATH')
    VOICE_CONFIG_PATH: Final = os.getenv('VOICE_CONFIG_PATH')
    VOICE_TRANSPOSE: Final = int(os.getenv('VOICE_TRANSPOSE'))
