import telebot
import random
from telebot import types

bot = telebot.TeleBot('your token here')
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
random.shuffle(cards) 

winner = 'none' 
packs = {'main': 0, 'croupier': 0} 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global packs
    
    if message.text == '/start':
        set_default_packs()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        getCard = types.KeyboardButton("✅ Начать игру")
        stats = types.KeyboardButton("❓ Статистика")
        markup.add(getCard, stats)
        bot.send_message(message.from_user.id, '👋 Добро пожаловать!', reply_markup=markup)

    elif message.text == '➕ Взять карту' or message.text == '✅ Начать игру' or message.text == '✅ Hit':
        if packs['main'] < 21:
            get_cards_main()
            get_cards_croupier()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            getCard = types.KeyboardButton("✅ Hit")
            standCard = types.KeyboardButton("❌ Stand")
            markup.add(getCard, standCard)
            if packs['main'] < 21:
                bot.send_message(message.from_user.id, '✅ Вы взяли карту.\n💸 Баланс: ' + str(packs['main']), reply_markup=markup)

            elif packs['main'] > 21:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                getCard = types.KeyboardButton("✅ Начать игру")
                markup.add(getCard)
                bot.send_message(message.from_user.id, '❌ Вы проиграли!\n💸 Ваш баланс: ' + str(packs['main'])+ '\n💸 Баланс крупье: ' + str(packs['croupier']), reply_markup=markup)
                set_default_packs()

    elif message.text == '❌ Stand':
        if packs['main'] < 15:
            get_cards_croupier()

        get_winner()
        if winner == 'self':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            getCard = types.KeyboardButton("✅ Начать игру")
            markup.add(getCard)
            bot.send_message(message.from_user.id, '✅ Вы выиграли!\n💸 Ваш баланс: ' + str(packs['main']) + '\n💸 Баланс крупье: ' + str(packs['croupier']), reply_markup=markup)
            set_default_packs()

        elif winner == 'croupier':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            getCard = types.KeyboardButton("✅ Начать игру")
            markup.add(getCard)
            bot.send_message(message.from_user.id, '❌ Вы проиграли!\n💸 Ваш баланс: ' + str(packs['main']) + '\n💸 Баланс крупье: ' + str(packs['croupier']), reply_markup=markup)
            set_default_packs()

        elif winner == 'none':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            getCard = types.KeyboardButton("✅ Начать игру")
            markup.add(getCard)
            bot.send_message(message.from_user.id, '⚠️ Ничья!\n💸 Ваш баланс: ' + str(packs['main']) + '\n💸 Баланс крупье: ' + str(packs['croupier']), reply_markup=markup)
            set_default_packs()
    return

def get_cards_main():
    global packs
    packs['main'] += cards.pop() 
    return

def get_cards_croupier():
    global packs
    if packs['croupier'] < 21 and packs['croupier'] < 20 and packs['croupier'] < 19 and packs['croupier'] < 18 and packs['croupier'] < 17:
        packs['croupier'] += cards.pop()
    return 

def set_default_packs(): 
    global cards
    global packs

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 
    random.shuffle(cards) 
    packs['main'] = 0 
    packs['croupier'] = 0 
    return

def get_winner():
    global winner
    global packs

    if packs['main'] <= 21 and packs['croupier'] > 21:
        winner = 'self'
    elif packs['main'] <= 21 and packs['croupier'] < 21 and packs['main'] > packs['croupier']:
        winner = 'self'
    elif packs['main'] > 21 and packs['croupier'] <= 21:
        winner = 'croupier'
    elif packs['main'] < 21 and packs['croupier'] <= 21 and packs['main'] < packs['croupier']:
        winner = 'croupier'
    elif packs['main'] > 21 and packs['croupier'] > 21:
        winner = 'croupier'
    elif packs['main'] == packs['croupier']:
        winner = 'none'
    return

bot.polling(none_stop=True, interval=0)
