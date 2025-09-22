def mobile_bill():
    minutes = int(input("Введите количество использованных минут: "))
    sms = int(input("Введите количество использованных SMS: "))
    mb = int(input("Введите количество использованного интернета (МБ): "))
    base_price = 24.99
    incl_min = 60
    incl_sms = 30
    incl_mb = 1024
    ext_min_pr = 0.89
    ext_sms_pr = 0.59
    ext_mb_pr = 0.79
    tax = 0.02
    ext_min = max(0, minutes - incl_min)
    ext_sms = max(0, sms - incl_sms)
    ext_mb = max(0, mb - incl_mb)
    total = (base_price + ext_min*ext_min_pr + ext_sms*ext_sms_pr + ext_mb*ext_mb_pr) + (base_price + ext_min*ext_min_pr + ext_sms*ext_sms_pr + ext_mb*ext_mb_pr)*tax
    print(f'{base_price} стоимость тарифа')
    print(f'{tax} налог')
    if ext_min != 0:
        print(f'{ext_min_pr} стоимость дополнитлнительных минут вне тарифа ({minutes})')
    if ext_sms != 0:
        print(f'{ext_sms_pr} стоимость дополнитлнительных sms вне тарифа ({sms})')
    if ext_mb != 0:
        print(f'{ext_mb_pr} стоимость дополнитлнительных mb вне тарифа ({mb})')
    print(total)

mobile_bill()