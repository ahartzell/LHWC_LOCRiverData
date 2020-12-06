# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 01:07:43 2019

@author: Adam
"""
import numpy as np 

def findLoc(fullList,searchString):
    index = []
    b = 0
    for i, curString in enumerate(fullList):   #for each value in fullLocaiton
        if searchString == curString:
            index.append(i)
        if i == 25518:
            print(i)
        
#    print(b)    
    return index


def findParam(fullList,searchString):
    index = []

    for i, curString in enumerate(fullList):   #for each value in fullLocaiton
        if searchString == curString:
            index.append(i)
   
    return index

def locReplace(replaceWith, itemsToReplace, locationFunc):
    for i, curLocation in enumerate(locationFunc):
        if curLocation == itemsToReplace:
            locationFunc[i] = replaceWith
    return list(locationFunc)
    

def checkDir(path):
    import os
    
    if os.path.exists(path):
        os.remove(path)
    os.makedirs(path)

def locAndSourceReplace(replaceWith, locToReplace, sourceToReplace, locationFunc, sourceFunc):
    for i, curLocation in enumerate(locationFunc):
        if curLocation == locToReplace and sourceToReplace == sourceFunc:
            locationFunc[i] = replaceWith
    return list(locationFunc)

# function to get unique values 
def unique(list1): 
    x = np.array(list1) 
    print(np.unique(x)) 
    return np.unique(x)


            