import requests
from datetime import datetime
import telebot
from get_xmr import getPrice
from auth_data import token
from telebot import types
from auth_data import currency
import auth_data

#global currency2
def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup_inline = types.InlineKeyboardMarkup()
        item_rub = types.InlineKeyboardButton(text = 'RUB', callback_data = 'rub')
        item_usd = types.InlineKeyboardButton(text = 'USD', callback_data = 'usd')
        item_eur = types.InlineKeyboardButton(text = 'EUR', callback_data = 'eur')

        markup_inline.add(item_rub, item_usd, item_eur)
        bot.send_message(message.chat.id, 'Hello User! To Start, Choose The Currency that will be displayed:',
            reply_markup = markup_inline
        )
    @bot.callback_query_handler(func = lambda call: True)
    def answer(call):
        global currency2
        if call.data == 'rub':
            currency = 'RUB'
            auth_data.currency = 'RUB'
            currency2 = 'RUB'
            print('rub')
        elif call.data == 'usd':
            currency = 'USD'
            auth_data.currency = 'USD'
            currency2 = 'USD'
            print('usd')
        elif call.data == 'eur':
            currency = 'EUR'
            auth_data.currency = 'EUR'
            currency2 = 'EUR'
            print('eur')

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                strPrice = getPrice()
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {strPrice} {currency2}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )
        else:
            bot.send_message(message.chat.id, "Whaaat??? Check the command dude!")

    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
