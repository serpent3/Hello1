#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class randNumList(list):    
    """
    1) int [amount] [fromEl] [toEl] [step]
    2) list to make copy 
    dependence: from random import randrange
    """

    
    def __init__(self, amount = 10, toEl = 100, fromEl = 1, step = 1):            
        from random import randrange
        #if arg[0] is list make copy else init new obgect 
        if isinstance(amount,list):
            for i in range(len(amount)):
                self.append(amount[i])
        else:
            for i in range(amount): 
                self.append(randrange(fromEl, toEl, step))        
 
    
    #it sorts copy or self
    def sort(self, sortList = None):    
        if not sortList:
            sortList = self
        while True:            
            counter = 0              
            for i in range(len(sortList) - 1):           
                    
                it = sortList[i]
                nextEl = sortList[i + 1]
                    
                if it > nextEl:
                    temp = nextEl
                    sortList[i + 1] = it               
                    sortList[i] = temp
                else: 
                    counter += 1                        
            if counter == len(sortList) - 1:
                return sortList
 
           
    def biSearch(self, n = None):    
        if not n:
            return False  
        #make copy of self
        sortList = randNumList(self)
        sortList.sort()
    
        f = 0
        l = len(sortList) 
        
        while l - f > 1:
            m = (f + l)//2            
            if n < sortList[m]:
                l = m
            else:
                f = m
        return True if n == sortList[f] else False         


# принимает аргументы командной строки    
if __name__ == '__main__':    
    import sys
    if len(sys.argv) == 1:
        print(randNumList())
    elif len(sys.argv) == 2:
        print(randNumList(int(sys.argv[1])))
    elif len(sys.argv) == 3:
        print(randNumList(int(sys.argv[1]),float(sys.argv[2]))) 
    elif len(sys.argv) == 4:
        print(randNumList(int(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])))    
