#!/usr/bin/env python
# coding: utf-8


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        print numList[1:]
        return numList[0] + listsum(numList[1:])


print (listsum([1,3,5,7,9]))


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

print(toStr(1456,10))


def check_palin(lister):
    if  len(lister) <= 1 :
        print 'True'
        return True
    else:
        if lister[0] == lister[-1]:
            lister.pop()
            del lister[0]
            check_palin(lister)
        else:
            print  'False'
            return False

def remove_white(string):
    a = []
    for i in string:
        if i != ' ':
            a.append(i)
    return a


print check_palin(remove_white('y - akay'))


def ko(strd):
    if strd == 1:
        return True
    else:
        return False

print ko(1)
