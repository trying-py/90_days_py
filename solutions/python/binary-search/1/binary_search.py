def find(search_list, value):
    search_list = sorted(search_list)
    left = 0
    right = len(search_list) - 1
    
    while left <= right:
        mid_value = (left + right) // 2
        if search_list[mid_value] == value:
            return mid_value
        elif search_list[mid_value] < value:
            left = mid_value + 1
        else:
            right = mid_value - 1

    raise ValueError("value not in array")
        
            
