from env import Env

import os
import json
from cryptography.fernet import Fernet
from typing import Final


class ChatGPTDatabase:

    CHARA_JSON_DIR: Final = './chatgpt/database/characters/'
    CONTEXT_DATA_DIR: Final = './chatgpt/database/contexts/'

    @classmethod
    def load_chara_json(cls):
        chara_json_path = cls.CHARA_JSON_DIR + Env.CHARA_NAME + '.json'
        if os.path.isfile(chara_json_path):
            f = open(chara_json_path)
            database = json.load(f)
            f.close()

            return database
        else:
            return {"model": "gpt-3.5-turbo", "messages": []}

    @classmethod
    def load_context_data(cls, data_path: str):
        if os.path.isfile(data_path):
            f = open(data_path)

            encrypted = f.read()
            fernet = Fernet(Env.CONTEXT_FERNET_KEY)
            decrypted = fernet.decrypt(encrypted).decode()

            database = json.loads(decrypted)
            f.close()

            return database
        else:
            return {"model": "gpt-3.5-turbo", "messages": []}

    @classmethod
    def save_context_data(cls, data_path: str, database: dict):
        with open(data_path, 'w+') as f:
            decrypted = json.dumps(database)
            fernet = Fernet(Env.CONTEXT_FERNET_KEY)
            encrypted = fernet.encrypt(decrypted.encode()).decode()

            f.write(encrypted)
            f.close()

    @classmethod
    def maintain_json(cls, database: dict):
        db_len = len(database['messages'])
        context_json_line = Env.CONTEXT_JSON_LINE
        if db_len > context_json_line:
            database['messages'] = database['messages'][-context_json_line:]
