import telebot
from telebot import types
import requests
from datetime import datetime

bot = telebot.TeleBot('5447415742:AAHnkIuNvbajvxBlRcGs_kCbPRM1Ur82sOA')

rate_list = {}
exchange_list = ['USD', 'EUR', 'RUB', 'CNY']
for rate in exchange_list:
    try:
        r = requests.get('http://www.nbrb.by/API/ExRates/Rates/' + rate + '?ParamMode=2')
        a = r.json()
        rate_list[rate] = a['Cur_OfficialRate']
    except Exception:
        b = float(input("Enter rate of " + rate + ":"))
        rate_list[rate] = b
        print(exchange_list)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    curr1 = types.KeyboardButton("USD")
    curr2 = types.KeyboardButton("EUR")
    curr3 = types.KeyboardButton("RUB")
    curr4 = types.KeyboardButton("CNY")
    # change = types.KeyboardButton("Конвертировать")
    exit = types.KeyboardButton("Выйти")
    markup.add(curr1, curr2, curr3, curr4, exit)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Если хочешь узнать курсы валют на сегодня, выбери валюту".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def currency(message):
    if (message.text == "USD"):
        bot.send_message(message.chat.id, text=(rate_list['USD']))
    elif (message.text == "EUR"):
        bot.send_message(message.chat.id, text=(rate_list['EUR']))
    elif (message.text == "RUB"):
        bot.send_message(message.chat.id, text=(rate_list['RUB']/100))
    elif (message.text == "CNY"):
        bot.send_message(message.chat.id, text=(rate_list['CNY']/10))
    # elif (message.text == "Конвертировать"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    #     cur1 = types.KeyboardButton("в евро")
    #     cur2 = types.KeyboardButton("в доллары")
    #     cur3 = types.KeyboardButton("в росс. рубли")
    #     cur4 = types.KeyboardButton("в юани")
    #     exit = types.KeyboardButton("Выйти")
        markup.add(cur1, cur2, cur3, cur4, exit)
        # bot.send_message(message.chat.id, text=value("Введи сумму в BYN:"), reply_markup=markup)

# @bot.message_handler(content_types=['value'])
# def exchange(message):
#     if (message.text == "в доллары"):
#         bot.send_message(message.chat.id, text=(value/rate_list['USD']))
#     elif (message.text == "в евро"):
#         bot.send_message(message.chat.id, text=(value/rate_list['EUR']))
#     elif (message.text == "в росс. рубли"):
#         bot.send_message(message.chat.id, text=(value/(rate_list['RUB'] / 100)))
#     elif (message.text == "в юани"):
#         bot.send_message(message.chat.id, text=(value/(rate_list['CNY'] / 10)))
    elif (message.text == "Выйти"):
        bot.send_message(message.chat.id, text=("До свиданья!"))
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован.")



# Время
t = datetime.time(datetime.now())
def time_before(time):
    if t == ('14:00:00:000000'):
        return rate_list['EUR', 'USD', "RUB", 'CNY']
    else:
        return None


bot.polling(non_stop=True, interval=0)