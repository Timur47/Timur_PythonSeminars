# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def arifmethic_progression(some_list):
    res_list=[]
    max_ch=some_list[0]
    res_list.append(max_ch)
    for i in range(len(some_list)-1):
        if some_list[i+1]>max_ch:
            max_ch=some_list[i+1]
            res_list.append(max_ch)
    print(res_list)

some_list = [1,5,2,3,4,6,1,7]
arifmethic_progression(some_list)