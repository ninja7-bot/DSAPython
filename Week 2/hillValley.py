#Checks if a list is a hillValley or not.
def hillvalley(list):
    upperBound = len(list) - 1

    maxIndex = list.index(max(list))
    minIndex = list.index(min(list))

    if ((maxIndex == 0 and minIndex == upperBound) or (minIndex == 0 and maxIndex == upperBound)) or len(list) <= 4:
        return False
    elif descending(list[0:minIndex]) and ascending(list[minIndex:upperBound]):
        return True
    elif ascending(list[0:maxIndex]) and descending(list[maxIndex:upperBound]):
        return True
    return False


def descending(list):
    for i in range(0, len(list)-1):
        if list[i]>list[i+1]:
            continue
        else:
            return False
    return True

def ascending(list):
    for i in range(0, len(list)-1):
        if list[i] < list[i+1]:
            continue
        else:
            return False
    return True   
