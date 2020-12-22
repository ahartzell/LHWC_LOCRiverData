# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:26:12 2019

@author: Adam
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
saveDir = r'D:\Dropbox\Yana\YanaPlottingProject\Round13\Data'

folderName = 'Results' + strftime("%Y-%m-%d %H_%M_%S", gmtime())
pathToMake = os.path.join(saveDir, folderName)
boxPlotPath = os.path.join(saveDir, folderName, 'BoxPlots')
os.makedirs(os.path.join(saveDir, folderName, 'BoxPlots'))
locationPlotPath = os.path.join(saveDir, folderName, 'Location')
os.makedirs(os.path.join(saveDir, folderName, 'Location'))
paramPlotPath = os.path.join(saveDir, folderName, 'Param')
os.makedirs(os.path.join(saveDir, folderName, 'Param'))

#Open Data files
with open(r'D:\Dropbox\Yana\YanaPlottingProject\Round13\DataStore.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    
    for row in data:
        location.append(row[1])
        fileTime.append(row[0])
        parameter.append(row[2])
        result.append(row[4])
        unit.append(row[5])
        source.append(row[6])
    location.pop(0)
    fileTime.pop(0)
    parameter.pop(0)
    result.pop(0)
    unit.pop(0)
    source.pop(0)
print('Data file has been opened')
#Open Location file
searchLocation = []

 
root = tk.Tk()
root.withdraw()

#fileLocationPath = filedialog.askopenfilename(title = 'Select Location File')
fileLocationPath = r'D:\Dropbox\Yana\YanaPlottingProject\Round13\13_Location.txt'

with open(fileLocationPath) as csvfile:
    tempLocation = csv.reader(csvfile, delimiter ='\t')
    print('file locaiton open')
    for row in tempLocation:
        searchLocation.append(row[0])
print('Opened location')


#Open paramaters file

#fileAnalytePath = filedialog.askopenfilename(title = 'Select Analyte File')
fileAnalytePath = r'D:\Dropbox\Yana\YanaPlottingProject\Round13\13_Analyte.txt'
searchParmeters = []
with open(fileAnalytePath) as csvfile:
    tempParams = csv.reader(csvfile, delimiter ='\t')
    
    for row in tempParams:
        searchParmeters.append(row[0])
print('Parameters and Locations Loaded')
#Make a time data set

#dataTime = []
#for curTime in fileTime:
#    dt = datetime.datetime.strptime(curTime, '%Y-%m-%d'
#    tempTime = time.mktime(dt.timetuple())
#    dataTime.append(tempTime)
#    

#Create a new list with the replacement data types.
#locationName = []
#locationReplacment = []
#with open('E:\Dropbox\Yana\YanaPlottingProject\RoundFive\Data\locationMap.txt') as csvfile:
#    data = csv.reader(csvfile,delimiter = '\t')
#    for row in data:
#        locationName.append(row[0])
#        locationReplacment.append(row[1])
#    locationName.pop(0)
#    locationReplacment.pop(0)
# 
#locationNew = list(location)
#print('New map has been created')
#for curLocName, curRepName in zip(locationName,locationReplacment):
#    #print(curLocName, curRepName)
#    func.locReplace(curRepName, curLocName, locationNew)
#
#searchLocation = list(set(searchLocation)) #remove duplicates from the search locaitons.
#

runBoxPlot =  input('Would you like to run box plots? (y/n)')
runTimePlot =  input('Would you like to run time plots? (y/n)')
#runTimePlot = 'y'
#runBoxPlot = 'n'
#runBoxPlot = 'n'
#runTimePlot = 'y'
#with open(pathToMake,'w',newline='') as myfile:
#    wr = csv.writer(myfile)
#    logFileData = zip(fileTime,location,location,parameter,result,unit)
#    wr.writerow(['Date','OldLocation','NewLocation','Parameter','Result','Unit'])
#    for row in logFileData:
#        wr.writerow(row)
#print('Data log created')


if runBoxPlot == 'y':
    for curParam in searchParmeters:  # find all values in each paramater
       print('Starting pramater: ', curParam)
       resultsToPlot = []
       locToPlot = []
       resultsToPlotb = []
       locToPlotb = []
       fig = plt.figure(1,figsize=(19.20,10.80))
      
       paramIndex = func.findParam(parameter,curParam)
       
       paramSearch = [] 
       locSearch = []
       fileTimeSearch = []
       unitSearch = []
       resultSearch =[]
       
       
       for i in paramIndex:  #Get all required data at each paramater index.
           paramSearch.append(parameter[i])
           locSearch.append(location[i])
           resultSearch.append(result[i])
           fileTimeSearch.append(fileTime[i])
           unitSearch.append(unit[i])
           
       for curLocation in searchLocation:  #find data for each location we are looking for in the shortended data.
           locIndex = func.findLoc(locSearch,curLocation)
               
           plotLocation = []
           plotdataTime = []
           plotParam = []
           plotResults = []
           plotUnit = []
           newResult = []
           print('Looking at : ', curLocation)
           
           if locIndex !=0:
               for j in locIndex:  #Get the data at each location index
                   
                   if resultSearch[j] != '': 
                       plotLocation.append(locSearch[j])
                       plotdataTime.append(fileTimeSearch[j])
                       plotParam.append(paramSearch[j])
                       plotResults.append(resultSearch[j])
                       plotUnit.append(unitSearch[j])
               
               
               for curResult in plotResults:
    
                  if curResult != 'NA':
                        newResult.append(curResult)
               if plotLocation != list():
    #               try:
                      
    #                       if i != 'NA':
    #                           resultsToPlot.append([float(i)])
    #                           locToPlot.append(plotLocation[0])
                          
                       
                 resultsToPlot.append([float(i) for i in newResult])
                 locToPlot.append(plotLocation[0])
    #               except:
    #                   pass
       
       if resultsToPlot != list():
           ax = fig.add_subplot(111) 
           bp = ax.boxplot(resultsToPlot)
           ax.set_xticklabels(locToPlot)
           plt.gcf().autofmt_xdate(rotation=90)
           plt.xlabel('Sampling Location')
           plt.ylabel(unitSearch[0])
           plt.title(curParam,fontweight="bold")
           plt.rcParams["font.weight"] = "bold"
           plt.rcParams["axes.labelweight"] = "bold"
           
           #This section will check to see if we the largest values in the data set is >999 and if so it will add commas to the
           #axis tick marks.
           resultsToPlot = [x for x in resultsToPlot if x]
           try:
               boxplotMaxRange = []
               for i in resultsToPlot:
                   boxplotMaxRange.append(max(i))
               if max(boxplotMaxRange) >= 999:
                       ax.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ','))) #add a commma every third digit
           except:
               pass
           #plt.savefig(saveDir+'BoxPlots\\'+curParam+'.jpg')
           plt.title(curParam,fontweight="bold")
           plt.rcParams["font.weight"] = "bold"
           plt.rcParams["axes.labelweight"] = "bold"
           plt.savefig(boxPlotPath+'\\'+curParam+'.jpg')      
           plt.close()
        
        

#Start searching data to match it
if runTimePlot == 'y':
    timeData = []
    for curLocation in searchLocation:
        print('Current Location: ',curLocation)
        locIndex = func.findLoc(location,curLocation)
        
        
        paramSearch = [] 
        locSearch = []
        fileTimeSearch = []
        unitSearch = []
        resultSearch =[]
        for i in locIndex:  #Pull out a list of the paramaters at the indices found.
           paramSearch.append(parameter[i].strip())
#           for ii in paramSearch:
#               paramSearch[ii].strip #remove any leading or trailing white space as it should not be there.
           locSearch.append(location[i].strip())
           resultSearch.append(result[i])
           fileTimeSearch.append(fileTime[i])
           unitSearch.append(unit[i])
           
         
        
        for curParam in searchParmeters:
            print('The current parameter is: ',curParam ,' at location: ', curLocation)
            paramIndex = func.findParam(paramSearch,curParam)    
        
            plotLocation = []
            plotdataTime = []
            plotParam = []
            plotResults = []
            plotUnit = []
            
            for i in paramIndex:  #pull out all data for each set.
                if math.isnan(float(resultSearch[i])):
                    pass
                else:
                    plotLocation.append(locSearch[i])
                    plotdataTime.append(fileTimeSearch[i])
                    plotParam.append(paramSearch[i])
                    plotResults.append(resultSearch[i])
                    plotUnit.append(unitSearch[i])
                    #curDir = saveDir+'Location\\'+plotLocation[0]
                    curDir = os.path.join(locationPlotPath, plotLocation[0])
                    pathlib.Path(curDir).mkdir(parents=True,exist_ok=True)
                    imageName = curDir+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg'
                    
                    #curDirParam = saveDir+'Param\\'+plotParam[0]
                    curDirParam = os.path.join(paramPlotPath,plotParam[0])
                    pathlib.Path(curDirParam).mkdir(parents=True,exist_ok=True)
                    imageNameParam = curDirParam+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg'
                
    
            try:
                if len(plotUnit) != 0 and len(plotResults) != 0 and os.path.isfile(imageName) == False:
                    print('Plotting now')
                    #plotdataTime.append('5/20/2019')
                    #plotResults.append('324')
                    figure = plt.figure(1,figsize=(19.20,10.80))
                    plotdataTime_obj = [datetime.datetime.strptime(s,"%m/%d/%Y") for s in plotdataTime]
                    figure = plt.plot(plotdataTime_obj,[float(i) for i in plotResults], marker='.', markersize=10)
                    figure = plt.xlabel('Sampling Date')
                    figure = plt.ylabel(plotUnit[0])
                    figure = plt.title(plotLocation[0]+'\n'+plotParam[0],fontweight="bold")
#                    plt.rcParams["axes.labelweight"] = "bold"
                    plt.rcParams["font.weight"] = "bold"
                    plt.rcParams["axes.labelweight"] = "bold"
                    
                    #figure = plt.xlim(['1/1/2008', '1/1/2019'])
                            #This was waht is working
                    ax = plt.gca()
      #broken              #ax.set_xlim(['5/29/2019', '10/20/2020'])
                    plotResultsFloat = [float(i) for i in plotResults]
                    if max(plotResultsFloat) >= 999:
                        ax.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ','))) #add a commma every third digit
                    for tick in ax.xaxis.get_major_ticks():
                        tick.label1.set_fontweight('bold')
                    for tick in ax.yaxis.get_major_ticks():
                        tick.label1.set_fontweight('bold')

                    plt.grid()
                    plt.gcf().autofmt_xdate(rotation=90)
                    
                    plt.savefig(curDir+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg', dpi=300)
                    plt.savefig(imageNameParam)
                    
                    figure = plt.close()
                    #plotSortedTime = sorted(plotdataTime, key=lambda x: datetime.datetime.strptime(x, '%m/%d/%y'))
                    #maxTime = plotSortedTime[-1]
                    #minTime = plotSortedTime[0]
                    #curTimeData = plotLocation[0]+','+plotParam[0]+','+minTime+','+maxTime
                    #print(curTimeData)
                    #timeData.append(curTimeData)
            except:
                pass
    saveDir+'\\'+folderName+'\\TimeData.csv'
    with open(saveDir+'\\'+folderName+'\\TimeData.csv', 'w') as filehandle:
        for row in timeData:
            filehandle.write('%s\n' % row)


#with open('listfile.txt', 'w') as filehandle:
#    for listitem in places:
#        filehandle.write('%s\n' % listitem)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#        
##
##               plt.boxplot([float(i) for i in plotResults])
##                plt.savefig(curDir+'\\'+plotLocation[0]+' '+plotParam[0]+'.jpg', dpi=300)
#                plt.savefig(imageNameParam)
#                plt.close()
#
#


     
