def deletels():
    result = 0
    num = input("Введите число: ")
    if int(num)%7==0:
        print("Магическое число")
    else:
        for i in range(len(num)):
            result += int(num[i])
        print(result)

deletels()