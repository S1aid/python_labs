def ideal_gas():
    p = int(input("Введите давление (в кПа) : "))
    v = int(input("Введите объём (в л/дм3) : "))
    t = int(input("Введите температуру (в целсиях C): "))
    R = 8.31 
    need_t = t + 273
    moles = (p*v)/(R*need_t)
    return moles

answear = ideal_gas()
print(answear)