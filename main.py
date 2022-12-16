import telebot
import json
from api import bot_token, admin_id

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    # a ready message to send when user touch the start button
    start_message = "Now, You can start chating!"
    sender_fn = message.from_user.first_name  # user's firstname
    sender_id = str(message.from_user.id)  # user's lastname
    # check if the lastname exists, if not make a empty variable
    if message.from_user.last_name is not None:
        sender_ln = message.from_user.last_name
    else:
        sender_ln = "-None-"
    # check if the username exists, if not make a empty variable
    if message.from_user.username is not None:
        sender_un = '@' + str(message.from_user.username)
    else:
        sender_un = "-None-"
    # a file with user's firstname will save that includes user's data
    userdata = {
        "id": sender_id,
        "username": sender_un,
        "firstname": sender_fn,
        "lastname": sender_ln
    }
    path = "./data/{}.json".format(sender_fn)
    with open(path, "w") as f:
        json.dump(userdata, f)
    # message that includes user's data will send to admin
    user_alert = """New User Started the Bot
    -FirstName: {}
    -LastName: {}
    -UserName: {}
    -UserID: {}
    """.format(sender_fn, sender_ln, sender_un, sender_id)
    bot.send_message(admin_id, user_alert)
    bot.send_message(message.from_user.id, start_message)


@bot.message_handler()
def message(message):
    # to check message is from admin or others
    if message.from_user.id is admin_id:
        reply_message = message.text
        try:
            sender_id = message.reply_to_message.forward_from.id
            bot.send_message(sender_id, reply_message)
        except AttributeError:
            """
            if user uses privacy settings the bot won't get it's id
            so the bot opens a file that belongs to the user
            and has saved by it's firstname and includes it's data
            so the bot can gets the user's id in this way
            """
            sender_fn = str(message.reply_to_message.forward_sender_name)
            with open("./data/{}.json".format(sender_fn), 'r') as f:
                user = json.load(f)
                bot.send_message(int(user["id"]), reply_message)
    else:
        sender_id = message.from_user.id
        bot.forward_message(admin_id, message.chat.id, message.id)


print("Bot Started!")
bot.polling()
