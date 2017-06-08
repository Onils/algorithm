#!/usr/bin/env python
#coding=utf-8
#二分法
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    list = [2,4,6,8,11,16,20]
    item = 11
    print "Item in list[%s]" % binary_search(list,item)
