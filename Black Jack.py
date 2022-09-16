import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 #Колода карт

random.shuffle(cards) #Перемешиваем колоду

main_pack = 0 #Изначальный баланс игрока
croupier_pack = 0 #Изначальный баланс крупье

def get_cards_main():
    global main_pack #Обращение к глобальной переменной main_pack (Баланс игрока)
    print('Выпала карта - ' + str(cards[-1])) #Выводим сообщение о том, какая выпала карта
    main_pack += cards.pop() #Добавляем последнюю карту с колоды к балансу игрока, после удаляем её
    return

def get_cards_croupier():
    global croupier_pack #Обращение к глобальной переменной croupier_pack (Баланс крупье)
    #Добавляем немного человечности боту
    if croupier_pack < 21 and croupier_pack < 20 and croupier_pack < 19 and croupier_pack < 18 and croupier_pack < 17:
        croupier_pack += cards.pop() #Добавляем последнюю карту с колоды к балансу бота, после удаляем её
    return 

def Win(): #Сообщение о выигрыше, выводим сообщение с балансами обоих игроков
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----[Вы выиграли]----')
    print('Ваш баланс: ' + str(main_pack)) #Баланс игрока
    print('Баланс крупье: ' + str(croupier_pack)) #Баланс крупье
    print('---------------------\n')
    return

def Lose(): #Сообщение о проигрыше, выводим сообщение с балансами обоих игроков
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----[Вы проиграли]----')
    print('Ваш баланс: ' + str(main_pack)) #Баланс игрока
    print('Баланс крупье: ' + str(croupier_pack)) #Баланс крупье
    print('----------------------\n')
    return

def Nothing(): #Сообщение о ничьей, выводим сообщение с балансами обоих игроков
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----[Ничья]----')
    print('Ваш баланс: ' + str(main_pack)) #Баланс игрока
    print('Баланс крупье: ' + str(croupier_pack)) #Баланс крупье
    print('---------------\n')
    return

def get_winner(): #Узнаём победителя
    global croupier_pack #Обращение к глобальной переменной KRUPIE_KOLODA (Баланс крупье)
    global main_pack #Обращение к глобальной переменной MAIN_KOLODA (Баланс игрока)
    
    if main_pack <= 21 and croupier_pack > 21:
        Win() #Вывод сообщения о победе
    if main_pack <= 21 and croupier_pack < 21 and main_pack > croupier_pack:
        Win() #Вывод сообщения о победе
    if main_pack > 21 and croupier_pack <= 21:
        Lose() #Вывод сообщения о пройгрыше
    if main_pack < 21 and croupier_pack <= 21 and main_pack < croupier_pack:
        Lose() #Вывод сообщения о пройгрыше
    if main_pack > 21 and croupier_pack > 21:
        Lose() #Вывод сообщения о пройгрыше
    if main_pack == croupier_pack:
        Nothing() #Вывод сообщения о ничьей
    return

while True:
    try:
        if main_pack < 21:
            print('Баланс: ', main_pack) #Выводим баланс игрока
            choice = input('Взять карту? [Y/N]: ') #Запрашиваем разрешение о выдаче карты
            print('\n\n\n\n\n\n\n\n\n\n\n') 
            if choice == 'Y' or choice == 'y' or choice == 'н' or choice == 'Н':
                
                #При согласии, отдаем разные карты игроку и крупье
                get_cards_croupier() #Крупье берёт карту
                get_cards_main() #Игрок берёт карту
                continue

            if choice == 'N' or choice == 'n' or choice == 'т' or choice == 'Т': #Отказ от выдачи карты
                get_cards_croupier() #Крупье берёт карту
                get_winner() #Выявляем победителя
                break
            else:
                print('[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ
                continue
        else:
            get_winner() #Выявляем победителя
            break
    except ValueError:
        print('[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ, завершаем работу
