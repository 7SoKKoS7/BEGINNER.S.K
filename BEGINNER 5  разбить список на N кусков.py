# Напишите функцию, которая принимает список, и число.
# Функция должна разбить список на N кусков, переданных в функцию в качестве втрого аргумента.
# Выполнить проверки по здравому смыслу (например, нет смысла пытаться разбить список из 3 элементов на 4 элемента)
def spisok_fun(spisok, num):
    if len(spisok) >= int(num):
     avg = len(spisok) / float(num)
     new_spisok = []
     last = 0.0
     while last < len(spisok):
        new_spisok.append(spisok[int(last):int(last + avg)])
        last += avg
    else:
        return 'Nelzya razdelit'
    return new_spisok

list = ['10','20','30','40','50','60','70','80','90','100','111','120','130','140',]
print('Spisok: ', list)
num = input('Vvedite na skolko chastey razdelit =')
print(spisok_fun(list, num))
