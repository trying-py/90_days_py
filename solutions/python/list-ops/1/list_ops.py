def append(list1, list2):
    result = []

    for i in list1:
        result += [i]
    for j in list2:
        result += [j]
    return result

def concat(lists):
    result = []
    for lst in lists:     
        for item in lst:
            result += [item]   
    return result


def filter(function, list):
    result = []
    for i in list:
        if function(i):
            result.append(i)
    return result

def length(list):
    count = 0
    for i in list:
        count += 1
    return count

def map(function, list):
    result = []
    for i in list:
        result += [function(i)]
    return result
            

def foldl(function, list, initial):
    acc = initial
    for i in list:
        acc = function(acc, i)
    return acc
    
def foldr(function, list, initial):
    if not list:
        return initial
    return function(foldr(function, list[1:], initial), list[0])


    
def reverse(list):
    result = []
    for i in list:
        result = [i] + result
    return result