import random

need_num = random.randint(1, 100)

def number_guessing(need_number):
    players_num = 0
    while players_num != need_number:
        players_num = int(input())
        if players_num < need_number:
            print("Больше")
        elif players_num > need_number:
            print("Меньше")
        else:
            break
    print("Вы угадали число")

number_guessing(need_num)