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
source = []
saveDir = 'C:\\TempSaveDir\\'



#Open Data files
with open('D:\Dropbox\Yana\YanaPlottingProject\RoundFive\Data\Data.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    
    for row in data:
        location.append(row[19])
        fileTime.append(row[2])
        parameter.append(row[10])
        result.append(row[13])
        unit.append(row[15])
        source.append(row[6])
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
source = []
with open('E:\Dropbox\Yana\YanaPlottingProject\RoundFive\Data\sourceMapping.txt') as csvfile:
    data = csv.reader(csvfile,delimiter = '\t')
    for row in data:
        locationName.append(row[0])
        source.append(row[1])
        locationReplacment.append(row[2])

 
locationNew = list(location)
sourceNew = list(source)
print('New map has been created')
for curLocName, curRepName, curSource in zip(locationName,locationReplacment,sourceNew):
    #print(curLocName, curRepName)
    func.locAndSourceReplace(curRepName, curLocName, curSource, locationNew, sourceNew)

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

     
