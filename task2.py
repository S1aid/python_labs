glas = "aeiou"

def delete_glass(lst):
    text = input("Введите строку: ")
    need_text = ""
    for i in text:
        if i.lower() not in lst:
            need_text += i
    return need_text

text = delete_glass(glas)
print(text)