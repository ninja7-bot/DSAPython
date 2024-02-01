def descending(list):
    return list == sorted(list, reverse=True)
"""    for i in range(0, len(list)-1):
        if list[i]>list[i+1]:
            continue
        else:
            return False
    return True"""

def ascending(list):
    return list == sorted(list)

"""    for i in range(0, len(list)-1):
        if list[i] < list[i+1]:
            continue
        else:
            return False
    return True """                 

print(descending([10,9,8,7]), ascending([1,2,3,4]))