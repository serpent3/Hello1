#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def conrtol(list, n):
    if not list or not n:
        return False


def bsr(list = None, n = None):
    
    if not list or not n:
        return False
    
    f = 0
    l = len(list)
    m = (f + l)//2
    
    print(list)
    
    if l - f <= 1:
        return True if n == list[f] else False
    
    if n < list[m]:
        return bsr(list[f:m], n)
    else:
        return bsr(list[m:l], n)
    

def bs(list = None, n = None):
    
    if not list or not n:
        return False
    
    f = 0
    l = len(list)
    
    while l - f > 1:
        m = (f + l)//2
        
        if n < list[m]:
            l = m
        else:
            f = m
    return f if n == list[f] else False  


def sort(list):
    
    if not list:
        return False

    while True:
        
        counter = 0  
        
        for i in range(len(list) - 1):           
                
            it = list[i]
            nextEl = list[i + 1]
                
            if it > nextEl:
                temp = nextEl
                list[i + 1] = it               
                list[i] = temp
            else: 
                counter += 1
                    
        if counter == len(list) - 1:
            return print("sorted: ", list)

                
def minus(a,b):
    while a != b: 
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)
                 
    
def randlist(amount = 1, fromEl = 1, toEl = 10, step = 1):
    from random import randrange
    list = []
    for i in range(amount):
       list.append(randrange(fromEl, toEl, step))   
    return list
    
    
class randnumlist(list):    
    '''
    int [amount] [fromEl] [toEl] [step]
    dependence: from random import randrange
    '''
    def __init__(self, amount = 1, fromEl = 1, toEl = 10, step = 1):            
        for i in range(amount): 
            self.append(randrange(fromEl, toEl, step))
    
    
    
    
    
    
    
    
    
    
    
    
      
