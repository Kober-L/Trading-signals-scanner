import telegram

my_token = 0000 # insert your token here
my_chat_id = 0000 # insert your chat id here

def send(msg,  chat_id = my_chat_id , token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

