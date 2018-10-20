my_list = [41, 37, 2, 51, 16, 84, 3, 25, 48, 42, 61, 14, 72, 18, 9, 23 , 1, 74]


def insertion_sort(my_list):
    
    for i in range(1, len(my_list)):

        j = i - 1

        while (j > -1) and my_list[j + 1] < my_list[j]:
            
            my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
            
            j -= 1

    return my_list


a = insertion_sort(my_list)

print(a)

# you get [1, 2, 3, 9, 14, 16, 18, 23, 25, 37, 41, 42, 48, 51, 61, 72, 74, 84]
