import telebot
from auth_data import token
from telebot import types

client = telebot.TeleBot(token)


@client.message_handler(commands = ['get_info', 'info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'YES', callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = 'NO', callback_data = 'no')

    markup_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Do u want to something about you?',
        reply_markup = markup_inline
    )


@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('MY ID')
        item_username = types.KeyboardButton('MY USERNAME')

        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, 'Press One Button',
            reply_markup = markup_reply
        )
    elif call.data == 'no':
        pass



@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == 'MY ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'MY USERNAME':
        client.send_message(message.chat.id, f'Your First Name: {message.from_user.first_name} And Last Name: {message.from_user.last_name}')


#client.polling(none_stop=True, interval=0)
client.polling()