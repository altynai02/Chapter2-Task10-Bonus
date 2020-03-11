# BONUS
# 4.Напишите программу для игры “Камень-ножницы-бумага” для 2-их человек.
# Правила:
# •Ножницы бьют бумагу
# •Бумага бьёт камень
# •Камень бьёт ножницы
# Игра должна продолжаться до 3-х побед. По окончании партии выводится победитель.
# Подсказка
# infinite loop
# break
# while
import time # для задержки времени
your_score = 0  # count score
your_friend_score = 0 #count score every time
while True:
    if your_friend_score == 3:
        time.sleep(1)
        print("Игра закончилась...Вы проиграли")
        break # the game is over
    elif your_score == 3:
        print("Поздравляю с победой!")
        break # the game is over
    you = input("\nВыбирай:\nкамень\nножницы\nбумага\n-> ").lower()
    time.sleep(1)
    your_friend = input("\nВыбирает ваш друг:\nкамень\nножницы\nбумага\n-> ").lower()
    if you == "камень":
        if your_friend == "камень":
            time.sleep(1)
            print("Ничья")
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга")
        elif your_friend == "бумага":
            time.sleep(1)
            print("\nВаш друг выиграл!")
            your_friend_score += 1
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга")
        else:
            time.sleep(1)
            print("\nВы выиграли!")
            your_score += 1
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга")
    elif you == "бумага":
        if your_friend == "бумага":
            time.sleep(1)
            print("Ничья")
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга") #Выводит ппосле каждой партии
        elif your_friend == "ножницы":
            time.sleep(1)
            print("\nВаш друг выиграл!")
            your_friend_score += 1
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга") #Выводит ппосле каждой партии
        else:
            time.sleep(1)
            print("\nВы выиграли!")
            your_score += 1
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга") #Выводит ппосле каждой партии
    elif you == "ножницы":
        if your_friend == "ножницы":
            print("Ничья")
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга") #Выводит ппосле каждой партии
        elif your_friend == "камень":
            print("\nВаш друг выиграл!")
            your_friend_score += 1
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга") #Выводит ппосле каждой партии
        else:
            print("\nВы выиграли!")
            your_score += 1
            print("Ваши очки-", your_score, ":", your_friend_score, "- Очки вашего друга") #Выводит ппосле каждой партии

