# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:26:12 2019

@author: Adam
"""

import csv
import functions as func
import matplotlib.pyplot as plt
import os 
import pathlib
import time
import datetime
import numpy as np

clear = lambda: os.system('cls')
clear()
plt.ioff()
temp = []
location = []
fileTime = []
parameter = []
result = []
unit = []
saveDir = 'C:\\TempSaveDir\\'



#Open Data files
with open('E:\Dropbox\Yana\YanaPlottingProject\RoundFive\Data\YanaTrySmart\OneColMapReal.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    
    for row in data:
        location.append(row[4])
        fileTime.append(row[0])
        parameter.append(row[9])
        result.append(row[12])
        unit.append(row[14])
    location.pop(0)
    fileTime.pop(0)
    parameter.pop(0)
    result.pop(0)
    unit.pop(0)
print('Data file has been opened')
#Open Location file
searchLocation = []

locationName = []
locationReplacment = []
with open('E:\Dropbox\Yana\YanaPlottingProject\RoundFive\Data\locationMap.txt') as csvfile:
    data = csv.reader(csvfile,delimiter = '\t')
    for row in data:
        locationName.append(row[0])
        locationReplacment.append(row[1])
    locationName.pop(0)
    locationReplacment.pop(0)
 
locationNew = list(location)
print('New map has been created')
for curLocName, curRepName in zip(locationName,locationReplacment):
    #print(curLocName, curRepName)
    func.locReplace(curRepName, curLocName, locationNew)

searchLocation = list(set(searchLocation)) #remove duplicates from the search locaitons.



with open(saveDir+'Datafile.csv','w',newline='') as myfile:
    wr = csv.writer(myfile)
    logFileData = zip(fileTime,location,locationNew,parameter,result,unit)
    wr.writerow(['Date','OldLocation','NewLocation','Parameter','Result','Unit'])
    for row in logFileData:
        wr.writerow(row)
print('Data log created')

#
#

     
