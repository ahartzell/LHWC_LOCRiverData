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
clear = lambda: os.system('cls')
clear()

plt.ion()
location = []
time = []
parameter = []
result = []
unit = []
saveDir = 'E:\\Dropbox\\Yana\\YanaPlottingProject\\Images\\'

#Open Data files
with open('Data.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    
    for row in data:
        location.append(row[1])
        time.append(row[0])
        parameter.append(row[2])
        result.append(row[3])
        unit.append(row[4])
        
#Open Location file
searchLocation = []
with open('locations.txt') as csvfile:
    tempLocation = csv.reader(csvfile, delimiter ='\t')
    
    for row in tempLocation:
        searchLocation.append(row[0])

#Open paramaters file
searchParmeters = []
with open('parameters.txt') as csvfile:
    tempParams = csv.reader(csvfile, delimiter ='\t')
    
    for row in tempParams:
        searchParmeters.append(row[0])

#Start searching data to match it

for curLocation in searchLocation:
    print('Current Location: ',curLocation)
    locIndex = func.findLoc(location,curLocation)
    
    
    paramSearch = [] 
    locSearch = []
    timeSearch = []
    unitSearch = []
    resultSearch =[]
    for i in locIndex:  #Pull out a list of the paramaters at the indices found.
       paramSearch.append(parameter[i])
       locSearch.append(location[i])
       resultSearch.append(result[i])
       timeSearch.append(time[i])
       unitSearch.append(unit[i])
       
     
    
    for curParam in searchParmeters:
        print('The current parameter is: ',curParam ,' at location: ', curLocation)
        paramIndex = func.findParam(paramSearch,curParam)    
    
        plotLocation = []
        plotTime = []
        plotParam = []
        plotResults = []
        plotUnit = []
    
        for i in paramIndex:  #pull out all data for each set.
            plotLocation.append(locSearch[i])
            plotTime.append(timeSearch[i])
            plotParam.append(paramSearch[i])
            plotResults.append(resultSearch[i])
            plotUnit.append(unitSearch[i])
        
            curDir = saveDir+'Location\\'+plotLocation[0]
            pathlib.Path(curDir).mkdir(parents=True,exist_ok=True)
            imageName = curDir+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg'
            
            curDirParam = saveDir+'Param\\'+plotParam[0]
            pathlib.Path(curDirParam).mkdir(parents=True,exist_ok=True)
            imageNameParam = curDirParam+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg'
            
        try:
            if len(plotUnit) != 0 and len(plotResults) != 0 and os.path.isfile(imageName) == False:
                print('Plotting now')
                figure = plt.figure(1,figsize=(19.20,10.80))
                figure = plt.plot(plotTime,[float(i) for i in plotResults], marker='.', markersize=10)
                figure = plt.xlabel('Sampling Date')
                figure = plt.ylabel(plotUnit[0])
                figure = plt.title(plotLocation[0]+'\n'+plotParam[0])
                plt.grid()
                plt.gcf().autofmt_xdate()
                plt.savefig(curDir+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg', dpi=300)
                plt.savefig(imageNameParam)
                plt.close()
                #plt.box([float(i) for i in plotResults])
        except:
            pass
        
        






     
