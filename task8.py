def is_polindrom():
    text = input("Введите слово: ")
    if text.lower() == text.lower()[::-1]:
        print("True")
    else:
        print("False")

is_polindrom()