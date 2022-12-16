# Telegram Chat Bot with Python
[![userinfobot](https://img.shields.io/badge/UserInfoBot-Get%20Your%20ID-blue)](https://t.me/userinfobot)
[![userinfobot](https://img.shields.io/badge/Requirements-See%20Here-green)](https://github.com/matinazhir/telegram_chat_bot/blob/master/requirements.txt)

It's a telegram bot that coded with python. By this bot you can chat with people anonymously.
This bot forward others message to you and you can reply them with replying their messages.

The bot uses users id to send messages. Normally every messages in telegram have senders id. But if the users makes privacy, the case will be different. Look at this image:

![Telegram Privacy Settings](https://i.stack.imgur.com/ARwvu.png "Telegram Privacy Settings")


Privacy settings is on Everybody by default, but when user puts it on Nobody, the bot won't get the user id.
So I use ```json``` to fix this problem.

When the user clicks or touches the start button in bot, the bot will save the user's data that includes the user's firsname, lastname, username and id in a json. So when the bot can't get the user id, it opens that json and will get the id. That was it.

# How to Run

1. Install python3, pip3, virtualenv, in your system.
2. Clone the project ```git clone https://github.com/matinazhir/telegram_chat_bot && cd telegram_chat_bot```.
3. In the project folder create a virtual environment using ```python3 -m venv .yourenvname``` for linux and ```python -m venv .yourenvname``` for windows.
4. Connect to your virtual environment using ```source .yourenvname/bin/activate```.
5. From the project folder, install packages using ```pip install -r requirements.txt```.
6. Add your telegram id to ```api.py``` (You can get your telegram id by badge that placed on top), and add your bot token.
7. Now environment is ready. Run it by ```python app/main.py```.
