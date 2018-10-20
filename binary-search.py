# That algorithm working for only sorted array

my_list = [1, 3, 5, 7, 11, 14, 17, 21, 23, 30, 32, 34, 37, 43, 51, 56, 75, 76]


def binary_search(my_list, searched, start, stop):

    if searched == my_list[0]:
        
        return 0
               
    elif start >= stop:
       
        return -1

    else:
        
        mid = (start + stop) // 2


        if searched == my_list[mid]:
            
            return mid

        elif searched < my_list[mid]:

            return binary_search(my_list, searched, start, mid - 1)

        else:

            return binary_search(my_list, searched, mid + 1, stop)


searched = 75 # number what need to find
start = 0
stop = len(my_list)

x = binary_search(my_list, searched, start, stop)

if x == -1:    
    print(f'Item {searched} not found')

else:   
    print('-' * 25)
    print(f'Item {searched} found at index {x}')
    print('-' * 25)



    
