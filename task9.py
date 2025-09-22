def real_ip():
    flag = True
    for i in input("Введите IP адрес в формате XXX.XXX.XXX.XXX: ").split("."):
        if int(i) > 255 or int(i) < 0:
            flag = False
    return flag

answear = real_ip()
print(answear)