def bubble_sort(num_list):
    start = 0
    while start < len(num_list):
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        i += 1
        start += 1
    return num_list   
        
list1 = [2, 5, 1, 9, 3]
list2 = []
list3 = [1, 1, 1, 1, 1]
list4 = [19, 1211, 41, -1, 13123121]
list5 = [0, 1, 0, 1, 0]

print(bubble_sort(list1))
print(bubble_sort(list2))
print(bubble_sort(list3))
print(bubble_sort(list4))
print(bubble_sort(list5))