



def binary_search(ordered_list, item): 

    size_of_list = len(ordered_list) - 1 
    index_of_first_element = 0 
    index_of_last_element = size_of_list 
    while index_of_first_element <= index_of_last_element: 
        mid_point = (index_of_first_element + index_of_last_element)//2 
        if ordered_list[mid_point] == item: 
            return mid_point 
        if item > ordered_list[mid_point]: 
            index_of_first_element = mid_point + 1 
        else: 
            index_of_last_element = mid_point - 1 
    if index_of_first_element > index_of_last_element: 
        return None