import math
import random

def sorted(length):
    return list(range(length))

def mostlysorted(length):
    templist = sorted(length)
    for i in range(math.ceil(length/10)):
        indexa = random.randint(0,length-1)
        indexb = random.randint(0,length-1)
        templist[indexa],templist[indexb]=templist[indexb],templist[indexa]
    return templist

def reversed(length):
    templist = sorted(length)
    for i in range(length):
        templist[i] = int(length-i-1)
    return templist

def shuffled(length):
    templist = sorted(length)
    random.shuffle(templist)
    return templist
