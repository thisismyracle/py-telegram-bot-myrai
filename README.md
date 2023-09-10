# Py - Telegram ChatGPT Bot - Myrai
a telegram virtual sister bot, based on ChatGPT 3.5. <br>
The bot is designed to be private chat only (no group allowed), because of future plan on using more resource for Image Captioning and voice-to-voice feature (soon).

<br>

### Installation
1. Make a new telegram bot with BotFather (open telegram and search BotFather), copy the bot token and bot username
2. Sign up to ChatGPT API, and copy the organization id and secret key
3. Clone this repo
4. Rename _.env.example_ to _.env_
5. Fill up the _.env_ file
6. Install the _requirements.txt_
7. Run the _main.py_

<br>

### Character Personalization
The default character persona is Myrai, a muslim sister, speak Bahasa Indonesia, etc. If you wanna edit the character persona, you can go to _'chatgpt/database/characters/'_ directory.
1. Duplicate _'myrai.json'_ in _'chatgpt/database/characters'_
2. Rename it to your desired name (no space)
3. Edit the json, fill up with your desired persona (use the language you used, here I use Bahasa Indonesia)
4. Open _.env_ file, change the _CHARA_NAME_ to name you gave in step 2
5. Edit _'chatgpt/chatgpt_service.py'_ -> _get_weighted_answer_ function up to your heart content (if you want exclusive calling only for you, the type of language she use, etc).

<br>

### For Language Other than Bahasa Indonesia
There are tasks to do if you want the bot not using Bahasa Indonesia:
1. Translate every string in _'chatgpt/chatgpt_service.py'_ variables: _days_, _months_, _time_affix_, and _time_context_
2. Translate every string in _'customtime/customtime_service.py'_ variables: _temp_context_

<br>

### Update: Voice-to-Voice feature added!
Now you can send voice note to your bot, and your bot will reply you with another voice note.
Before that, you must do:
1. Prepare your SOVITS model (you can train new one [here](https://github.com/thisismyracle/py-sovits-song-cover), or download existing model on huggingface ([example: alice](https://huggingface.co/spaces/zomehwh/sovits-models/tree/main/models)))
2. Paste your model folder into _'voiceprompt/database/model/'_
3. Copy your _model.pth_ and _config.json_ path, then paste it into _.env_ file (example: _'./voiceprompt/database/model/alice/alice.pth'_ and _'./voiceprompt/database/model/alice/config.json'_)

