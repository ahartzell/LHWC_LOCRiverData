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
t_mrl = []
t_result = []
unit = []
source = []
fileComments = []
resultsToPlot = []
saveDir = r'C:\Data'

# folderName = 'Results' + strftime("%Y-%m-%d %H_%M_%S", gmtime())
# pathToMake = os.path.join(saveDir, folderName)
# boxPlotPath = os.path.join(saveDir, folderName, 'BoxPlots')
# os.makedirs(os.path.join(saveDir, folderName, 'BoxPlots'))
# locationPlotPath = os.path.join(saveDir, folderName, 'Location')
# os.makedirs(os.path.join(saveDir, folderName, 'Location'))
# paramPlotPath = os.path.join(saveDir, folderName, 'Param')
# os.makedirs(os.path.join(saveDir, folderName, 'Param'))

#Open Data files
with open(r'D:\Dropbox\Yana\YanaPlottingProject\Round13\Reservoir 2019_2020.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    
    for row in data:
        location.append(row[1])
        fileTime.append(row[0])
        parameter.append(row[3])
        result.append(row[6])
        t_result.append(row[7])
        t_mrl.append(row[4])
        unit.append(row[8])
        source.append(row[5])
    location.pop(0)
    fileTime.pop(0)
    parameter.pop(0)
    result.pop(0)
    unit.pop(0)
    t_result.pop(0)
    t_mrl.pop(0)
print('Data file has been opened')

 

####  Place code to generate information for resultsToPlot here.  This will is where things will be different every time.    ######

#The code in this section is basd off the following rules. 
  #0  Valid data in results (ie not empty) 
  #1. IF t-Result is a simple numeric value, then use that value for Result.
  #2. IF t-Result is >2419.6, then use 2420 for Result (occurred only in E-Coli).
  #3. IF t-Result begins with <, then use one-half of the t-MRL column for the Result.
  #4. IF t-Result is numeric followed by “(+-(numeric value))”, then use the numeric result and ignore the value within the parentheses.
  #5. IF t-Result  is ND, then use one-half the tMRL (if tMRL is blank, then use zero)
  #6. IF t-Result is anything else, ignore the entry (generate a list of entries that are to be ignored).
  
 #Start with rule number 1.
j =0 
for i, x in enumerate(result):
    j=j+1
    dataFound = False
    #RULE 0:  Valid data in the results variable    
    if x:  #this is a test to see if x is empty.  If it is not empty run test below.
        resultsToPlot.append(float(x))
        dataFound = True
        fileComments.append('Valid Data.  No test needed.')
    else:  #if x was empty then perform rules 1-5.
        try:    
            float(t_result[i]) #Check Rule Number 1 by seeing if we can convert to float to indicate a "simple numeric value"
        #RULE 1
            if float(t_result[i]) < 2419.6:  #If this is ture we have satisified rule 1
                resultsToPlot.append(float(t_result[i]))
                dataFound = True
                fileComments.append('Value determined from rule 1')
        #RULE 2        
            else: #if not then we have satisfied rule 2
                    resultsToPlot.append(2420.0)
                    dataFound = True
                    fileComments.append('Value determined from rule 2')
        except:
            #RULE 3
                t_results_i = t_result[i]
                if t_results_i[0] == '<':  #check if the first charicter is <  
                    resultsToPlot.append(float(t_mrl[i])/2) #append data if its true and set value to tmrl/2
                    dataFound = True
                    fileComments.append('Value determined from rule 3')
            #RULE 4
                if '(+-' in t_results_i:  #check to see if the string contains the charicters '(+-'
                    splitResult = t_results_i.split('(')
                    resultsToPlot.append(float(splitResult[0])) #append the numeric data before the (
                    dataFound = True
                    fileComments.append('Value determined from rule 4')
            #RULE 5
                if t_results_i == 'ND':
                    if t_mrl[i]:
                        resultsToPlot.append(float(t_mrl[i])/2) #append data if its true and set value to tmrl/2
                        dataFound = True
                        fileComments.append('Value determined from rule 5, t_mrl/2')
                    else:
                        resultsToPlot.append(0) #append data if its true and set value to tmrl/2
                        dataFound = True
                        fileComments.append('Value determined from rule 5, tmrl empty')
    #RULE 6
    if dataFound == False:
        resultsToPlot.append(99999999.9999999) #append data if its true and set value to tmrl/2
        fileComments.append('No valid data found')

#One of the analytes has a '\' in it. Search through all locations and replacae with 



          
####  End code to genterate custom results

with open(r'D:\Dropbox\Yana\YanaPlottingProject\Round13\DataStore.txt', 'w') as csvfile:
    dataStoreFile = csv.writer(csvfile, delimiter='\t', lineterminator="\n")
    dataStoreFile.writerow(['Time','Location','Analyte','Result','ResultsToPlot','Unit','Source','FileComments'])
    # for i in location.length-1  #Ruby Shit
    for i, locValue in enumerate(location):
        dataStoreFile.writerow([fileTime[i],location[i],parameter[i],result[i],resultsToPlot[i],unit[i],source[i],fileComments[i]])

        

    