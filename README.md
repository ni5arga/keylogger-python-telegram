# keylogger-python-telegram

## Overview
This is a simple keylogger script written in Python that logs key presses and sends them to a specified Telegram chat using the Telegram Bot API. The script utilizes the `pynput` library for keyboard monitoring and the `python-telegram-bot` library for interacting with the Telegram API.

**Note: The use of keyloggers without explicit consent is unethical and potentially illegal. This script is intended for educational purposes only, and it is crucial to respect privacy and adhere to applicable laws and regulations.**

## Features
- Monitors keyboard inputs in real-time.
- Sends logged key presses to a Telegram chat.

## Requirements
- Python 3.x
- `pynput` library (`pip install pynput`)
- `python-telegram-bot` library (`pip install python-telegram-bot`)

## Setup
1. Create a new bot on Telegram by talking to the [BotFather](https://telegram.me/botfather).
2. Obtain the API token for your bot.
3. Get your chat ID.
4. Replace `'YOUR_API_TOKEN'` and `'YOUR_CHAT_ID'` in the script with your bot's API token and chat ID.

## Usage
Run the script, and it will start monitoring keyboard inputs. The key presses, along with timestamps, will be sent to the specified Telegram chat in Markdown format.

```bash
python keylogger.py
```

## Disclaimer
This script is intended for educational purposes only. The use of keyloggers without explicit consent is unethical and potentially illegal. The author is not responsible for any misuse of this script.
