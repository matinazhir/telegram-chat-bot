import json
import config
from telebot import TeleBot
tb = TeleBot(config.bot_token)


@tb.message_handler(commands=['start'])
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
    path = "user_data/{}.json".format(sender_fn)
    with open(path, "w") as f:
        json.dump(userdata, f)
    # message that includes user's data will send to admin
    user_alert = """New User Started the Bot
    -FirstName: {}
    -LastName: {}
    -UserName: {}
    -UserID: {}
    """.format(sender_fn, sender_ln, sender_un, sender_id)
    tb.send_message(config.admin_id, user_alert)  # send info to admin
    # send welcome to user
    tb.send_message(message.from_user.id, start_message)


# with content_types bot can gest messages includes all type of files
@tb.message_handler(content_types=["document", "video", "photo", "audio",
                                   "voice", "sticker", "text"])
def message(message):
    # to check message is from admin or others
    if message.from_user.id == config.admin_id:
        reply_message = message.text
        try:  # if message is from admin, send it to user
            sender_id = message.reply_to_message.forward_from.id
            tb.send_message(sender_id, reply_message)
        except AttributeError:  # if the bot was unable to get user id
            """
            if user uses privacy settings the bot won't get it's id
            so the bot opens a file that belongs to the user
            and has saved by it's firstname and includes it's data
            so the bot can gets the user's id in this way
            """
            sender_fn = str(message.reply_to_message.forward_sender_name)
            with open("user_data/{}.json".format(sender_fn), 'r') as f:
                user = json.load(f)
                # send message to user
                tb.send_message(int(user["id"]), reply_message)
    else:  # it will forward messages from user to admin
        tb.forward_message(config.admin_id, message.chat.id, message.id)


print("Bot Started!")
tb.polling()
