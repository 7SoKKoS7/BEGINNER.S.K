# Дана строка из имён, в формате "Денис, Олег, Вася, Петя,Дима,Женя".
# Разбейте строку так, чтобы получился список имён.
# Заметьте: после запятой не всегда есть пробел (он не должен входить в имена, которые попадут в список)
string = "Денис, Олег, Вася, Петя,    Дима,Женя"
print(string)
new_string = string.replace(' ', '')
list = new_string.split(',')
print(list)
