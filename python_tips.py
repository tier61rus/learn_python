#Видеокурс
#https://itvdn.com/ru/video/python-starter?utm_source=forum&utm_medium=post&utm_campaign=toster
челендж по питону на 100 заданий
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

курс 
https://itproger.com/course/python/7
#========================================================

#!/usr/bin/env python
Строка shebang обычно записывается в одной из двух форм:
#!/usr/bin/python3
или:
#!/usr/bin/env python3
В первом случае она определяет используемый интерпретатор.
Вторая форма может потребоваться для программ на языке Python, запускаемых вебсервером, хотя абсолютный путь в каждом конкретном случае может отличаться от того, что показан здесь. Во втором случае будет использован первый интерпретатор python3, найденный в текущем окружении.

# утф печать
# -*- coding: utf-8 -*-
....

# разделитель
print "." * 10

#импорт модуля
from sys import argv

# аргументы на вход
script_name, weight, height = argv

# обработка исключений
try:
    i = int(s)
    print ("Valid!")
except ValueError as er:
    print ("Oshibka:",er)

#======================
# блок if
if expr:
    suite1
elif expres2:
    suite2
else:
    suite3
#======================
# приглашение к вводу с консоли
line = input("integer: ")

#==== Cписки - аналог массивов
mylist =  [6, 5, 4, 3, 2, 1]
mylist.append (23) - вставка элемента
mylist.append (b) - расширение списка l списком b
mylist.insert (1,23) - меняет первое значение на 23
mylist.remove (34) - удалит первое вхождение 34 в списке
mylist.pop () - удаляет последний элемент
mylist.pop (5) - удаляет пятый элемент
mylist.count (34) - считает количество элементов
sort -сортировка
reverse - переворачивание
clear  - очистка
len (mylist) = 6
#=====================
# объявление функции

def count_middle(a,b):
    c = (a+b)/2;
    return c;


# ЦИКЛЫ
#======================
# цикл от 1 до 2
for _ in range (1, 3): 
    print (_)
#вариант break + else
for j in 'hello world':
	if j == 'w':
		break
else:
	print ("Буквы а нету в слове")
#======================
# цикл while
while 1:
    line = input("please enter number ")
    
Или так
while True:
    line = input("enter a number or Enter to finish: ")

# условие if or
if lowest is None or lowest > number:
#=========================
тернарный оператор
k = 10 if a > 8 else  5
#=========================

#стандартная документация
python -m pydoc <module_name>

#==============================
# конкатенации строк, способ "%" 
"your %s is in the %s" % (object, location)
# конкатенации строк, способ "+"
"your " + object + " is in the " + location 

#================================
#агалог perl -c???
python -m py_compile  3_vogon_poetry.py

#================================
#инкремент ++ - не поддерживается
lines += 1
#декремент
lines -= 1

#=====================
 аналог перлового exit
#sys.exit()

 perem = """her"s mother"""
#======================
определение кода символа в юникоде
print (hex(ord (evr)))
0x20ac
#========================
>>> ent_three = s[-3:]
>>> print (ent_three)
#========================
name = "Дмитрий"
age = 25
print("Меня зовут {}. Мне {} лет.".format(name, age)# кортеж
Меня зовут Дмитрий. Мне 25 лет.
print("Меня зовут {name} Мне {age} лет.".format(age=age, name=name) #словарь
Меня зовут Дмитрий. Мне 25 лет.

###### 2 CHAPTER
Список ключевых слов:
Ключевые слова

False - ложь.
True - правда.
None - "пустой" объект.
and - логическое И.
with / as - менеджер контекста.
assert условие - возбуждает исключение, если условие ложно.
break - выход из цикла.
class - пользовательский тип, состоящий из методов и атрибутов.
continue - переход на следующую итерацию цикла.
def - определение функции.
del - удаление объекта.
elif - в противном случае, если.
else - см. for/else или if/else.
except - перехватить исключение.
finally - вкупе с инструкцией try, выполняет инструкции независимо от того, было ли исключение или нет.
for - цикл for.
from - импорт нескольких функций из модуля.
global - позволяет сделать значение переменной, присвоенное ей внутри функции, доступным и за пределами этой функции.
if - если.
import - импорт модуля.
in - проверка на вхождение.
is - ссылаются ли 2 объекта на одно и то же место в памяти.
lambda - определение анонимной функции.
nonlocal - позволяет сделать значение переменной, присвоенное ей внутри функции, доступным в объемлющей инструкции.
not - логическое НЕ.
or - логическое ИЛИ.
pass - ничего не делающая конструкция.
raise - возбудить исключение.
return - вернуть результат.
try - выполнить инструкции, перехватывая исключения.
while - цикл while.
yield - определение функции-генератора.

#----------------------------------- 
dir() - возвращает список атрибутов объекта

начальный символ - любой из A-Z + набор нац симфолов, символ продолжения + цифры
_ - результат последнего вычисленного выражения

В логических выражениях число 0 и значение False представляют False,
а любое другое целое число и значение True представляют True.
В числовых выражениях значение True представляет 1, а False – 0.


0b - двоичное число (первое 0)
0o - восьмеричное
0x - шестнадцатиричное
int(s, base) - преобразование числа в целое, иначе ValueError

>>> dv = "0b101"
>>> decim = int (dv, 2)
>>> print ("decim=",decim)
decim= 5


x // Y - деление с усечением дробной части
x ** y - возведение в степень  = pow(x,y) (Return x raised to the power y)

#==============
# принт без пробелов
print ("decim=",decim, sep='')
# принт без \n
print ("decim=",decim, end='')
#можно оба сразу:
print (i,",", sep = '', end = '')

Преобразование целых
чисел в тип float можно выполнить с помощью функции float()
===========================
>>> n = int(1.9)
>>> print (n)
1
#---------------------------
>>> n = math.floor(1.6)
>>> print (n)
1
#---------------------------
>>> n = math.ceil(1.6)
>>> print (n)

#-----------------------
>>> m = decimal.Decimal(2/3);
>>> print (m)
0.66666666666666662965923251249478198587894439697265625

#--------------------------------
#Строки в языке Python представлены неизменяемым типом данных str, который хранит последовательность символов Юникода.

#Решить эту проблему можно, используя «сырые» (raw) строки. Это обычные строки в кавычках или в тройных кавычках, в которые перед
#первой кавычкой добавлен символ r. Внутри таких строк все символы интерпретируются как обычные символы, поэтому отпадает необходимость
#экранировать символы, которые в других типах строк имеют специальное значение.

#==================
#>>> text = r"тут можно писать что хочешь ';\[]{}"
#>>> print (text)
#тут можно писать что хочешь ';\[]{}

#==========
s = ("Это отличный способ объединить две длинные строки, "
" потому что он основан на конкатенации строковых литералов.")

#=================
>>> euros = "\u20AC"
>>> print (euros)
€
>>> print (ord(euros))
8364

#===================
#Работа с файлами
f = open("myfile.txt", "x")
f.write("Woops! I have deleted the content!")
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

# поиск всех файлов в папке по маске:
onlyfiles = glob.glob(folder_name + "/*.png")

#====================================
установка модулей через pip
yum install python3-pip
python3.5 -m pip install validate_email

#-------------------
print ("num = ",num," rub")
#-------------------

#GENERATORS
shortest = min((word for word in good_avas_list if word), key=len) # поиск самого короткого слова в словаре

#DICTS
for ava_src in avatars_src_dict.keys():

#===========================
# про main
if __name__ == "__main__":

Когда интерпретатор Python читает исходный файл, он исполняет весь найденный в нем код. Перед тем, как начать выполнять команды, он определяет несколько специальных переменных. Например, если интерпретатор запускает некоторый модуль (исходный файл) как основную программу, он присваивает специальной переменной __name__ значение "__main__". Если этот файл импортируется из другого модуля, переменной __name__ будет присвоено имя этого модуля.

В случае с вашим сценарием, предположим, что код исполняется как основная функция, например:

python threading_example.py
После задания специальный переменных интерпретатор выполнит инструкцию import и загрузит указанные модули. Затем он проанализирует блок def, создаст объект-функцию и переменную под названием myfunction, которая будет указывать на этот объект.

Затем он прочтет инструкцию if, «поймёт», что __name__ эквивалентен "__main__", и выполнит указанный блок.

Одна из причин делать именно так – тот факт, что иногда вы пишете модуль (файл с расширением .py), предназначенный для непосредственного исполнения. Кроме того, он также может быть импортирован и использован из другого модуля. Производя подобную проверку, вы можете сделать так, что код будет исполняться только при условии, что данный модуль запущен как программа, и запретить исполнять его, если его хотят импортировать и использовать функции модуля отдельно.

#=================
#работа с путями
import os
big_image_path = os.path.join(base_folder_path, "180x180", domain_name)

#========================
https://tproger.ru/translations/python-args-and-kwargs/

*args и **kwargs — специальный синтаксис, позволяющий передавать в функцию переменное количество аргументов. При этом, совсем не обязательно использовать имена аргументов args и kwargs;
*args используется для неименованных аргументов, с которыми можно работать как со списком;
**kwargs используется для именованных аргументов, с которыми можно работать как со словарём;
если вы хотите использовать и *args, и **kwargs, то это делается так: func(fargs, *args, **kwargs), порядок следования аргументов важен;
#=======================
#sleep
import time
time.sleep(5)

#=======================
#запуск внешнего скрипта
import subprocess
        args = [ 
            '/usr/local/bin/emlrecover',
            '-h', ip, 
            '-s', path,
            '-u', uidl,
            '-o', '/dev/stdout',
        ]
r = subprocess.run(args, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

