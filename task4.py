def razmen():
    num = int(input("Введите сумму денег: "))
    r_100 = num // 100
    mod_100 = num%100
    r_50 = mod_100//50
    mod_50 = mod_100%50
    r_20 = mod_50//20
    mod_20 = mod_50%20
    r_10 = mod_20//10
    mod_10 = mod_20%10
    r_5 = mod_10//5
    mod_5 = mod_10%5
    r_2 = mod_5//2
    mod_2 = mod_5%2
    r_1 = mod_2//1
    print(f'{r_100} по 100, {r_50} по 50, {r_20} по 20, {r_10} по 10, {r_5} по 5, {r_2} по 2, {r_1} по 1')

razmen()