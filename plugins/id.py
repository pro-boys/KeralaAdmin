from config import *

@bot.message_handler(commands=['id'])
def get_id(message):
    if message.chat.type == "private":
        bot.reply_to(message.chat.id, '''*Information of the user*

*Name :* `{}`
*Username :* `{}`
*User ID :* `{}`'''.format(message.from.first_name, message.from.username, message.from.id), parse_mode='Markdown')
        return
