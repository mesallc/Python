import random

KOLODA = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 #колода карт

random.shuffle(KOLODA) #Перемешиваем колоду

MAIN_KOLODA = 0 #Изначальный баланс игрока
KRUPIE_KOLODA = 0 #Изначальный баланс крупье

def GET_CARD_MAIN():
    global MAIN_KOLODA #Обращение к глобальной переменной MAIN_KOLODA (Баланс игрока)
    print('Выпала карта - ' + str(KOLODA[-1])) #Выводим сообщение о том, какая выпала карта
    MAIN_KOLODA += KOLODA.pop() #Добавляем последнюю карту с колоды к балансу игрока, после удаляем её
    return

def GET_CARD_KRUPIE():
    global KRUPIE_KOLODA #Обращение к глобальной переменной KRUPIE_KOLODA (Баланс крупье)
    #Добавляем немного человечности боту
    if KRUPIE_KOLODA < 21 and KRUPIE_KOLODA < 20 and KRUPIE_KOLODA < 19 and KRUPIE_KOLODA < 18 and KRUPIE_KOLODA < 17:
        KRUPIE_KOLODA += KOLODA.pop() #Добавляем последнюю карту с колоды к балансу бота, после удаляем её
    return 

def Win(): #Сообщение о выйгрыше, выводим сообщение с балансами обоих игроков
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----[Вы выйграли]----')
    print('Ваш баланс: ' + str(MAIN_KOLODA))
    print('Баланс крупье: ' + str(KRUPIE_KOLODA))
    print('---------------------\n')
    return

def Lose(): #Сообщение о пройгрыше, выводим сообщение с балансами обоих игроков
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----[Вы проиграли]----')
    print('Ваш баланс: ' + str(MAIN_KOLODA))
    print('Баланс крупье: ' + str(KRUPIE_KOLODA))
    print('----------------------\n')
    return

def Nothing(): #Сообщение о ничьей, выводим сообщение с балансами обоих игроков
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----[Ничья]----')
    print('Ваш баланс: ' + str(MAIN_KOLODA))
    print('Баланс крупье: ' + str(KRUPIE_KOLODA))
    print('---------------\n')
    return

def GET_WINNER(): #Узнаём победителя
    global KRUPIE_KOLODA #Обращение к глобальной переменной KRUPIE_KOLODA (Баланс крупье)
    global MAIN_KOLODA #Обращение к глобальной переменной MAIN_KOLODA (Баланс игрока)
    
    if MAIN_KOLODA <= 21 and KRUPIE_KOLODA > 21:
        Win() #Вывод сообщения о победе
    if MAIN_KOLODA <= 21 and KRUPIE_KOLODA < 21 and MAIN_KOLODA > KRUPIE_KOLODA:
        Win() #Вывод сообщения о победе
    if MAIN_KOLODA > 21 and KRUPIE_KOLODA <= 21:
        Lose() #Вывод сообщения о пройгрыше
    if MAIN_KOLODA < 21 and KRUPIE_KOLODA <= 21 and MAIN_KOLODA < KRUPIE_KOLODA:
        Lose() #Вывод сообщения о пройгрыше
    if MAIN_KOLODA > 21 and KRUPIE_KOLODA > 21:
        Lose() #Вывод сообщения о пройгрыше
    if MAIN_KOLODA == KRUPIE_KOLODA:
        Nothing() #Вывод сообщения о ничьей
    return

while True:
    try:
        if MAIN_KOLODA < 21:
            print('Баланс: ', MAIN_KOLODA) #Выводим баланс игрока
            SELECTION = input('Взять карту? [Y/N]: ') #Запрашиваем разрешение о выдаче карты
            print('\n\n\n\n\n\n\n\n\n\n\n')
            if SELECTION == 'Y' or SELECTION == 'y' or SELECTION == 'н' or SELECTION == 'Н':
                
                #При согласии, отдаем разные карты игроку и крупье
                GET_CARD_KRUPIE() 
                GET_CARD_MAIN() 
                continue

            if SELECTION == 'N' or SELECTION == 'n' or SELECTION == 'т' or SELECTION == 'Т': #Отказ от выдачи карты
                GET_CARD_KRUPIE() #Крупье берет карту
                GET_WINNER() #Выявляем победителя
                break
            else:
                print('[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ
                continue
        else:
            GET_WINNER()
            break
    except ValueError:
        print('[Ошибка] Введите нужный символ') #Ошибка, если не введен нужный символ, завершаем работу
