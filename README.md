# Py - Telegram ChatGPT Bot - Myrai
a telegram virtual sister bot, based on ChatGPT 3.5. <br>
The bot is designed to be private chat only (no group allowed), because of future plan on using more resource for Image Captioning and SpeechToText-TextToSpeech feature (soon).

<br>

### Installation
1. Make a new telegram bot with BotFather (open telegram and search BotFather), copy the bot token and bot username
2. Sign up to ChatGPT API, and copy the organization id and secret key
3. Clone this repo
4. Rename .env.example to .env
5. Fill up the .env file
6. Install the requirements.txt
7. Run the main.py

<br>

### Character Personalization
The default character persona is Myrai, a muslim sister, speak Bahasa Indonesia, etc. If you wanna edit the character persona, you can go to 'chatgpt/database/characters/' directory.
1. Duplicate 'myrai.json'
2. Rename it to your desired name (no space)
3. Edit the json, fill up with your desired persona (use the language you used, here I use Bahasa Indonesia)
4. Open .env file, change the CHARA_NAME to name you gave in step 2
