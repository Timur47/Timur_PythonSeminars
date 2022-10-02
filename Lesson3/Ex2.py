# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list=['ghbdtn',1,'qq',12,'212']
for i in list:
    if isinstance(i,int) or isinstance(i,float):
        print('yes')
