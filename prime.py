# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:55:06 2022

@author: govin
"""
def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
def oddIndices(a):
    sum = 0;
    for i in range(len(a)):
        if prime(i) == True:
            sum += a[i]
    return sum