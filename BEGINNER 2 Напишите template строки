#Напишите template строки, который можно будет многократно переиспользовать, вставляя в него имя и фамилию человека. Используйте метод строки "format".
from string import Template
i = 1
while i<5:
 i +=i   
 name = input('Enter name:')
 lname = input('Enter Lastname:')
 t = Template('$name ' ' $lname')
 print(t.substitute(name=name.format(name), lname=lname.format(lname)))
