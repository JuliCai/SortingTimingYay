from timing import time_function

def _mergelists(list1,list2):
    merged = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            merged.append(list1[idx1])
            idx1 += 1
        else:
            merged.append(list2[idx2])
            idx2 += 1
    merged.extend(list1[idx1:])
    merged.extend(list2[idx2:])
    return merged

@time_function
def bubble(list):
    sorted = list
    if len(list)>1:
        for i in range(len(list)):
            for j in range(len(list)-i-1):
                if sorted[j]>sorted[j+1]:
                    sorted[j],sorted[j+1]=sorted[j+1],sorted[j]
    return sorted

def _merge_sort(lst):
    if len(lst) <= 1:
        return lst
    splitpoint = len(lst) // 2
    return _mergelists(_merge_sort(lst[:splitpoint]), _merge_sort(lst[splitpoint:]))

@time_function
def merge(list):
    return _merge_sort(list)

@time_function
def insertion(list):
    sorted = []
    for item in list:
        insertindex = len(sorted)
        while insertindex > 0 and sorted[insertindex - 1] > item:
            insertindex -= 1
        sorted.insert(insertindex, item)
    return sorted

# NOT MY IMPLEMENTATION:
def _quick_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    # Median-of-three pivot to avoid worst-case on sorted/reversed inputs
    a, b, c = lst[0], lst[n // 2], lst[-1]
    # Determine median without relying on built-in sorted
    if (a - b) * (c - a) >= 0:
        pivot = a
    elif (b - a) * (c - b) >= 0:
        pivot = b
    else:
        pivot = c

    less = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst if x > pivot]
    return _quick_sort(less) + equal + _quick_sort(greater)

@time_function
def quick(list):
    return _quick_sort(list)