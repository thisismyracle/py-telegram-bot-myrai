from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()


class Env:

    BOT_TOKEN: Final = os.getenv('BOT_TOKEN')
    BOT_USERNAME: Final = os.getenv('BOT_USERNAME')

    OPENAI_API_KEY: Final = os.getenv('OPENAI_API_KEY')
    OPENAI_ORG_ID: Final = os.getenv('OPENAI_ORG_ID')

    MODEL_NAME: Final = os.getenv('MODEL_NAME')
    CHARA_NAME: Final = os.getenv('CHARA_NAME')
    CONTEXT_JSON_LINE: Final = int(os.getenv('CONTEXT_JSON_LINE'))
    CONTEXT_FERNET_KEY: Final = bytes(os.getenv('CONTEXT_FERNET_KEY'), 'utf-8')
    DEFAULT_TYPE_WPM: Final = int(os.getenv('DEFAULT_TYPE_WPM'))
    DEFAULT_READ_WPM: Final = int(os.getenv('DEFAULT_TYPE_WPM'))
