import telebot
from random import randint
 
bot = telebot.TeleBot('5784181471:AAGJ75DniNdzckq1NXsN4GjcMCGLuVg1t-g')
 
@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, '/rules\n/start')
 
@bot.message_handler(commands=['rules'])
def welcome(message):
    bot.send_message(message.chat.id, 'На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
 
candies = 100
 
def bot_vasy(message):
    global candies
    player = message.from_user.first_name
    k = randint(1, 28)
    if k < candies:
        candies -= k
        bot.send_message(message.chat.id, f'Бот забрал {k} конфет. На столе осталось {candies} конфет.\nВаш ход, {player}. Сколько конфет Вы хотите забрать?')
    else:
        bot.send_message(message.chat.id, 'Бот выиграл!')
 
@bot.message_handler(commands = ['start'])
def start(message):
    player = message.from_user.first_name 
    global candies
    flag = randint(0, 1)
    if flag:
        bot.send_message(message.chat.id, f'На столе {candies} конфет. {player} делает первый ход')
        bot.send_message(message.chat.id,  f'{player}, сколько конфет Вы хотите забрать?')
    else:
        bot.send_message(message.chat.id, f'На столе {candies} конфет. Бот делает первый ход')
        bot_vasy(message)
        
@bot.message_handler(func = lambda _: True)
def players(message):
    player = message.from_user.first_name
    global candies
    try:
        n = int(message.text)
        if n > 28:
            bot.send_message(message.chat.id, f'{player}, не больше 28. Попробуем ещё раз.')
        elif n > candies:
            bot.send_message(message.chat.id, f'{player}, столько конфет не осталось. Попробуем ещё раз.')
        else:
            if n < candies:
                candies -= n
                bot.send_message(message.chat.id, f'Осталось {candies} конфет.')
                bot_vasy(message)
            else:
                bot.send_message(message.chat.id, f'{player}, Вы выйграли!')
    except:
        bot.send_message(message.chat.id, 'Что-то не то, попробуйте еще раз.')    
 
bot.polling()