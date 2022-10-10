# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'арпв полвд аджажаж абважаж адладв'
text2=text.split()
text3=[]

for i in range (0,len(text2)):
    if text2[i].find('абв') == -1:
        text3.append(text2[i])
print(text3)
