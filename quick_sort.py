from random import choice

my_list = [41, 23, 11, 5, 17, 84, 3, 25, 48, 2, 61, 4, 55, 2, 9, 30, 1, 74]


def quick_sort(my_list):
    
    if my_list:

        pivot = choice(my_list)
        
        less = [i for i in my_list if i < pivot]
        equal = [i for i in my_list if i == pivot]
        greater = [i for i in my_list if i > pivot]

        return quick_sort(less) + equal + quick_sort(greater)

    return []

        
def q_sort(my_list):
    
    if my_list: return q_sort([i for i in my_list if i<my_list[0]]) + [i for i in my_list if i==my_list[0]] + q_sort([i for i in my_list if i>my_list[0]])

    return []


a = quick_sort(my_list) # or q_sort(my_list)

print(a)

# you get [1, 2, 2, 3, 4, 5, 9, 11, 17, 23, 25, 30, 41, 48, 55, 61, 74, 84]

