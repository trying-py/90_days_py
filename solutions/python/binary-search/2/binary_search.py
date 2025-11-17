def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")
    mid = len(search_list) // 2
    mid_value = search_list[mid]

    if mid_value == value:
        return mid
    
    if mid_value < value:
        result = find(search_list[mid+1:], value)
        return mid + 1 + result
    
    else:
        return find(search_list[:mid], value)