# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:16:41 2020

@author: ahart
"""

import csv
import functions as func
import matplotlib.pyplot as plt
import matplotlib as mpl
import os 
import pathlib
import math
import time
import datetime
import numpy as np
import tkinter as tk
from tkinter import filedialog
from time import gmtime, strftime
import time

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
saveDir = r'C:\Data'

folderName = 'Results' + strftime("%Y-%m-%d %H_%M_%S", gmtime())
pathToMake = os.path.join(saveDir, folderName)
boxPlotPath = os.path.join(saveDir, folderName, 'BoxPlots')
os.makedirs(os.path.join(saveDir, folderName, 'BoxPlots'))
locationPlotPath = os.path.join(saveDir, folderName, 'Location')
os.makedirs(os.path.join(saveDir, folderName, 'Location'))
paramPlotPath = os.path.join(saveDir, folderName, 'Param')
os.makedirs(os.path.join(saveDir, folderName, 'Param'))

#Open Data files
with open(r'D:\Dropbox\Yana\YanaPlottingProject\Round13\Reservoir 2019_2020.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    
    for row in data:
        location.append(row[1])
        fileTime.append(row[0])
        parameter.append(row[3])
        result.append(row[6])
        unit.append(row[8])
        source.append(row[5])
    location.pop(0)
    fileTime.pop(0)
    parameter.pop(0)
    result.pop(0)
    unit.pop(0)
print('Data file has been opened')

dataStore = [fileTime,location,parameter,result,unit,source]
tempStore = np.transpose(dataStore)
dataStore = []
dataStore = tempStore.tolist()


with open(r'D:\Dropbox\Yana\YanaPlottingProject\Round13\DataStore.txt', 'w') as csvfile: 
    dataStoreFile = csv.writer(csvfile, delimiter='\t', lineterminator="\n")
    dataStoreFile.writerow(['Time','Location','Analyte','Result','Unit','Source'])
    # for i in location.length-1  #Ruby Shit
    for i, locValue in enumerate(location):
        dataStoreFile.writerow([fileTime[i],location[i],parameter[i],result[i],unit[i],source[i]])

        

    