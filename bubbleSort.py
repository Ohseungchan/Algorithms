# -*- coding: utf-8 -*- 
# 버블정렬 패스스루 1 회 반복 정렬 값
# 버블정렬 패스스루 반복후 정렬 값

def bubble_sort(list):
    unsorted_until_index = len(list) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
            unsorted_until_index = unsorted_until_index -1

list = [65,55,45,35,25,15,10]
bubble_sort(list)
print(list)
print('')

forRotate = len(list) - 1
while forRotate < len(list):
    bubble_sort(list)
    print(list)
    forRotate = forRotate -1
    if forRotate == 0:
        break
