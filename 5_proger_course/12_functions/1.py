#!/usr/bin/python
#Ваша задача сделать функцию, которая будет принимать 2 параметра (время и скорость) и возвращать сколько проедет километров человек исходя из параметров. Теперь вам необходимо вывести это на экран. Если человек проехал 1 километр, то писать так: "Вы проедете: 1 километр", иначе писать так: "Вы проедете: {здесь цифра} километров". Последнее выполнить через lambda

def count_distance (v, t):
    print ("скорость = ", v)
    print ("время = ", t)
    return v*t

s = count_distance(1,1);
back_mess = (lambda a: "kilometr" if a == 1 else "kilometrov")(s)
print ("Вы проедете: ", s, back_mess )

# Создайте функцию, которая будет принимать параметр и внутри этой функции будет еще одна функция, которая также будет принимать параметр. Вторая функция должна просто суммировать оба параметра, а первая должна вернуть результат.

def funk1(par1):
    def funk2(par2):
        return par1 + par2
    return funk2

summa_sotka_funk = funk1(100)
res = summa_sotka_funk(200)
print ("res = ", res)

#Создайте функцию с параметрами по умолчанию. Вызовите эту функцию и передайте в нее не все параметры. Функция должна вернуть деление всех чисел. При этом добавьте проверку при деления на ноль.

def chastnoe (a,b,c = 1):
    if ((a == 0) or (b == 0) or (c == 0 )):
        print ("alarm")
    else:
        return int(a/b/c)

diff = chastnoe (8,4)
print ("diff=", diff)

#Создайте функцию, которая может принимать не установленное количество параметров. Выведите сумму всех переданных параметров.
def many_params (*params):
    res_sum = 0
    for i in params:
        print ("i=",i)
        res_sum += i
    return res_sum

list = (3,6)
print (many_params(3,5))

#Создайте анонимную функцию с неустановленным количеством параметров. Функция должна выводить все параметры на экран.
anon_funk = lambda *args: print (args)
anon_funk(3,7)
