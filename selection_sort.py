my_list = [27, 23, 11, 5, 17, 2, 7, 25, 78, 2, 41, 44, 15, 53, 9, 30, 1, 74]


def selection_sort(my_list):

    for i in range(len(my_list)):
        
        index_min = i

        for j in range(i + 1, len(my_list)):
            
            if my_list[j] < my_list[index_min]:

                index_min = j

        tmp = my_list[index_min]
        my_list[index_min] = my_list[i]
        my_list[i] = tmp

    return my_list


print(selection_sort(my_list))
# you get [1, 2, 2, 5, 7, 9, 11, 15, 17, 23, 25, 27, 30, 41, 44, 53, 74, 78]


