import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 #Колода карт
random.shuffle(cards) #Перемешиваем колоду
main_pack = 0 #Изначальный баланс игрока
croupier_pack = 0 #Изначальный баланс крупье

def get_cards_main():
    global main_pack #Обращение к глобальной переменной main_pack (Баланс игрока)
    print('\nВыпала карта - ' + str(cards[-1])) #Выводим сообщение о том, какая выпала карта
    main_pack += cards.pop() #Добавляем последнюю карту с колоды к балансу игрока, после удаляем её
    return

def get_cards_croupier():
    global croupier_pack #Обращение к глобальной переменной croupier_pack (Баланс крупье)
    #Добавляем немного человечности боту
    if croupier_pack < 21 and croupier_pack < 20 and croupier_pack < 19 and croupier_pack < 18 and croupier_pack < 17:
        croupier_pack += cards.pop() #Добавляем последнюю карту с колоды к балансу бота, после удаляем её
    return 

def set_default(): #Ставим стандарт
    global cards
    global main_pack
    global croupier_pack

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 #Колода карт
    random.shuffle(cards) #Перемешиваем колоду
    main_pack = 0 #Изначальный баланс игрока
    croupier_pack = 0 #Изначальный баланс крупье
    return

def send_message(player): #Сообщение о выигрыше, выводим сообщение с балансами обоих игроков
    if player == 'self':
        print('\nРезультат: Вы выиграли!')
    elif player == 'croupier':
        print('\nРезультат: Вы проиграли!')
    elif player == 'none':
        print('\nРезультат: Ничья')
    print('\nВаш баланс: ' + str(main_pack) + '\nБаланс крупье: ' + str(croupier_pack) + '\n') #Баланс игрока и крупье
    return

def get_winner(): #Узнаём победителя
    global croupier_pack #Обращение к глобальной переменной KRUPIE_KOLODA (Баланс крупье)
    global main_pack #Обращение к глобальной переменной MAIN_KOLODA (Баланс игрока)

    if main_pack <= 21 and croupier_pack > 21:
        send_message('self') #Вывод сообщения о победе
    if main_pack <= 21 and croupier_pack < 21 and main_pack > croupier_pack:
        send_message('self') #Вывод сообщения о победе
    if main_pack > 21 and croupier_pack <= 21:
        send_message('croupier') #Вывод сообщения о проигрыше
    if main_pack < 21 and croupier_pack <= 21 and main_pack < croupier_pack:
        send_message('croupier') #Вывод сообщения о проигрыше
    if main_pack > 21 and croupier_pack > 21:
        send_message('croupier') #Вывод сообщения о проигрыше
    if main_pack == croupier_pack:
        send_message('none') #Вывод сообщения о ничьей
    return

while True:
    try:
        if main_pack < 21:
            print('\nБаланс: ', main_pack) #Выводим баланс игрока
            choice = input('Взять карту? [Y/N]: ') #Запрашиваем разрешение о выдаче карты

            if choice == 'Y' or choice == 'y' or choice == 'н' or choice == 'Н': #При согласии, отдаем разные карты игроку и крупье
                get_cards_croupier() #Крупье берёт карту
                get_cards_main() #Игрок берёт карту
                continue

            if choice == 'N' or choice == 'n' or choice == 'т' or choice == 'Т': #Отказ от выдачи карты
                get_cards_croupier() #Крупье берёт карту
                get_winner() #Выявляем победителя
                select = input('\n\nНачать заного? [Y/N]: ')

                if select == 'Y' or select == 'y' or select == 'н' or select == 'Н':
                    set_default()
                    continue

                elif select == 'N' or select == 'n' or select == 'т' or select == 'Т':
                    print('\n\n[Информация] Спасибо за игру!')
                    break

                else:
                    print('\n\n[Ошибка] Введите нужный символ')

            else:
                print('\n\n[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ
                continue
        else:
            get_winner() #Выявляем победителя
            select = input('[Информация] Начать заного? [Y/N]: ')

            if select == 'Y' or select == 'y' or select == 'н' or select == 'Н':
                set_default()
                continue

            elif select == 'N' or select == 'n' or select == 'т' or select == 'Т':
                print('\n\n[Информация] Спасибо за игру!')
                break

            else:
                print('\n\n[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ
                
    except ValueError:
        print('\n\n[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ, завершаем работу
