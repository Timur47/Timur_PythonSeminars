# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str_one = 'good news everyone, or oneone'
str_two = 'one'
count = 0
index = 0
start = index
while index !=-1:
    if str_one.find(str_two, start+1) !=-1:
        index = str_one.find(str_two,start+1)
        start = index
        count +=1
    else:
        index =-1
print(count)
