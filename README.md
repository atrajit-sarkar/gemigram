# TeleAIMemoryBased
Here below the setup guide for server and termux. 
**Termux setup:** You can run this bot locally in your mobile using termux app which you can get from playstore.

## Termux Setup Guide:
1. Install termux from [playstore](https://play.google.com/store/apps/details?id=com.termux)
2. run the following command to update repository
   ```bash
   apt update
   ```
3. The install python 
   ```bash
   pkg install python3 -y
   ```
4. Install git
   ```bash
   pkg install git -y
   ```
5. Clone the repo:
   ```bash
   git clone https://github.com/atrajit-sarkar/gemigram.git
   ```
6. Then navigate to the project directory:
   ```bash
   cd gemigram
   ```
7. make `.env` file:
   ```bash
   nano .env
   ```
8. Write the following content:
   ```bash
    DEBUG_MODE=true
    GEMINI_API_KEY = 
    TELEGRAM_BOT_TOKEN = 
    FIREBASE_CREDENTIALS_PATH=service.json
    FIRESTORE_COLLECTION=test-bot
   ```
 **Note:** You have to get the `gemini_api_key` from [here](https://aistudio.google.com/api-keys)
Create a bot from telegram and paste it there.

9. Now create a firebase project and copy paste the service.json file in the gemigram directory service.json file.
```bash
nano service.json
```

10. Install required python dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```
11. Run the bot:
    ```bash
    python3 main.py
    ```
