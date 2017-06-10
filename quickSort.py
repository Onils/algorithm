#!/usr/bin/env python
#coding=utf-8
#快排

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greate = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greate)

if __name__ == '__main__':
    print quickSort([2,5,5,1,7,6,10,1,3,8])
