def cool_password():
    password = input("Введите пароль: ")
    if len(password) < 16:
        print("Слишком короткий")
    elif password.isalpha():
        print("Слишком слабый пароль")
    elif password.isdigit():
        print("Слишком слабый пароль")
    else:
        print("Надежный пароль")

cool_password()