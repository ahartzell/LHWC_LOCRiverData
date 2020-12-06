# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:47:32 2020

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
#Open Location file
searchLocation = []

 