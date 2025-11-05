from timing import time_function

def _mergelists(list1,list2):
    idx=0
    merged = []
    while (idx<len(list1)) or (idx<len(list2)):
        if (idx<len(list1)) and (idx<len(list2)):
            if list1[idx]<list2[idx]:
                merged.append(list1[idx])
                merged.append(list2[idx])
            else:
                merged.append(list2[idx])
                merged.append(list1[idx])
        else:
            if idx<len(list1):
                merged.append(list1[idx])
            if idx<len(list2):
                merged.append(list2[idx])
        idx += 1
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

@time_function
def merge(list):
    if(len(list)<=1):
        return list
    else:
        splitpoint = len(list)//2
        _ , firsthalf = merge(list[:splitpoint])
        _, secondhalf = merge(list[splitpoint:])
        return _mergelists(firsthalf,secondhalf)

@time_function
def insertion(list):
    sorted = []
    for item in list:
        insertindex = 0
        while insertindex < len(sorted) and sorted[insertindex] < item:
            insertindex += 1
        sorted.insert(insertindex, item)
    return sorted