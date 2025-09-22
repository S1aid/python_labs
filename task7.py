def second_to_minute():
    minute = int(input("Введите количество секунд: "))
    sec = minute%60
    minn = minute//60
    text = f'{minn} минута {sec} секунда'
    return text

need_t = second_to_minute()
print(need_t)