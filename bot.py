from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "6503352676:AAFdmZZWiFSpyLwuTOldk-QD6hSZXrX-y5M")

API_ID = int(os.environ.get("API_ID", "26376042"))

API_HASH = os.environ.get("API_HASH", "1f5343b0646645ca1eaf7c4759fc248f")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
