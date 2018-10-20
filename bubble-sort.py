old_list = [23,1,32,34,56,30,76,75,43,21,14,17,3,5,7,37,51,11]


def bubble_sort(my_list):

    last_item = len(my_list) - 1

    for i in range(0, last_item):
        
        for j in range (0, last_item - i):
            
            if my_list[j] > my_list[j + 1]:
                
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


new_list = bubble_sort(old_list).copy()

print(new_list)

# you get [1, 3, 5, 7, 11, 14, 17, 21, 23, 30, 32, 34, 37, 43, 51, 56, 75, 76]
