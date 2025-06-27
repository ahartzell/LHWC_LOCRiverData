# ================================
# DataParsing.py with Obnoxious Comments
# ================================

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:26:12 2019
This script processes environmental sampling data and generates both box plots and time series plots.
It loads data from user-specified files and creates directories to save resulting plots.
"""

# Standard Python module for reading CSV (or tab-delimited) files
import csv

# Custom module containing helper functions (must be in same directory or PYTHONPATH)
import functions as func

# Import matplotlib for plotting
import matplotlib.pyplot as plt
import matplotlib as mpl

# OS-related functionality (file paths, directory creation, etc.)
import os 

# pathlib for object-oriented path manipulation
import pathlib

# For numeric operations and NaN handling
import math

# Time and date utilities
import datetime

# Numerical Python, commonly used for handling numeric arrays
import numpy as np

# GUI file dialog module from tkinter
import tkinter as tk
from tkinter import filedialog

# Used for formatting time as strings
from time import gmtime, strftime

# --------------------------------------
# Clear the screen (Windows only)
# --------------------------------------
clear = lambda: os.system('cls')
clear()

# Turn off interactive plotting to prevent figures from popping up
plt.ioff()

# --------------------------------------
# Initialize lists to store various columns from the dataset
# --------------------------------------
temp = []
location = []
fileTime = []
parameter = []
result = []
unit = []
source = []

# Define the base directory where plots and logs will be saved
saveDir = r'X:\YanaPlottingProject\Round14\Data'

# Generate a timestamped folder name for this run
folderName = 'Results' + strftime("%Y-%m-%d %H_%M_%S", gmtime())

# Build full directory paths for each category of plots
pathToMake = os.path.join(saveDir, folderName)
boxPlotPath = os.path.join(saveDir, folderName, 'BoxPlots')
os.makedirs(boxPlotPath)  # Create directory for box plots
locationPlotPath = os.path.join(saveDir, folderName, 'Location')
os.makedirs(locationPlotPath)  # Create directory for location-specific plots
paramPlotPath = os.path.join(saveDir, folderName, 'Param')
os.makedirs(paramPlotPath)  # Create directory for parameter-specific plots

# --------------------------------------
# Load the main dataset
# --------------------------------------
with open(r'X:\YanaPlottingProject\Round14\DataStore.txt') as csvfile:
    data = csv.reader(csvfile, delimiter = '\t')
    for row in data:
        location.append(row[1])  # Column 1: Location
        fileTime.append(row[0])  # Column 0: Timestamp
        parameter.append(row[2]) # Column 2: Parameter/Analyte
        result.append(row[4])    # Column 4: Result value
        unit.append(row[5])      # Column 5: Unit of measurement
        source.append(row[6])    # Column 6: Data source
    # Remove header row manually (assumes first row is headers)
    location.pop(0)
    fileTime.pop(0)
    parameter.pop(0)
    result.pop(0)
    unit.pop(0)
    source.pop(0)
print('Data file has been opened')

# --------------------------------------
# Load location filter file
# --------------------------------------
searchLocation = []
root = tk.Tk()  # Initialize tkinter root window
root.withdraw() # Hide the root window (no GUI needed)
fileLocationPath = filedialog.askopenfilename(title = 'Select Location File')

with open(fileLocationPath) as csvfile:
    tempLocation = csv.reader(csvfile, delimiter = '\t')
    print('file location open')
    for row in tempLocation:
        searchLocation.append(row[0])
print('Opened location')

# --------------------------------------
# Load analyte/parameter filter file
# --------------------------------------
fileAnalytePath = filedialog.askopenfilename(title = 'Select Analyte File')
searchParmeters = []
with open(fileAnalytePath) as csvfile:
    tempParams = csv.reader(csvfile, delimiter = '\t')
    for row in tempParams:
        searchParmeters.append(row[0])
print('Parameters and Locations Loaded')

# --------------------------------------
# Prompt user whether to run plot types
# --------------------------------------
runBoxPlot =  input('Would you like to run box plots? (y/n)')
runTimePlot =  input('Would you like to run time plots? (y/n)')

# --------------------------------------
# Generate Box Plots
# --------------------------------------
if runBoxPlot == 'y':
    for curParam in searchParmeters:
       print('Starting parameter: ', curParam)
       resultsToPlot = []
       locToPlot = []
       fig = plt.figure(1,figsize=(19.20,10.80))

       paramIndex = func.findParam(parameter, curParam)

       paramSearch = [] 
       locSearch = []
       fileTimeSearch = []
       unitSearch = []
       resultSearch =[]

       for i in paramIndex:
           paramSearch.append(parameter[i])
           locSearch.append(location[i])
           resultSearch.append(result[i])
           fileTimeSearch.append(fileTime[i])
           unitSearch.append(unit[i])

       for curLocation in searchLocation:
           locIndex = func.findLoc(locSearch, curLocation)
           plotLocation = []
           plotdataTime = []
           plotParam = []
           plotResults = []
           plotUnit = []
           newResult = []
           print('Looking at : ', curLocation)

           if locIndex != 0:
               for j in locIndex:
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
                   resultsToPlot.append([float(i) for i in newResult])
                   locToPlot.append(plotLocation[0])

       if resultsToPlot != list():
           ax = fig.add_subplot(111)
           bp = ax.boxplot(resultsToPlot)
           ax.set_xticklabels(locToPlot)
           plt.gcf().autofmt_xdate(rotation=30)
           plt.xlabel('Sampling Location')
           plt.ylabel(unitSearch[0])
           plt.title(curParam, fontweight="bold")
           plt.rcParams["font.weight"] = "bold"
           plt.rcParams["axes.labelweight"] = "bold"

           resultsToPlot = [x for x in resultsToPlot if x]
           try:
               boxplotMaxRange = []
               for i in resultsToPlot:
                   boxplotMaxRange.append(max(i))
               if max(boxplotMaxRange) >= 999:
                   ax.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
           except:
               pass
           plt.savefig(boxPlotPath + '\\' + curParam + '.jpg')
           plt.close()

# --------------------------------------
# Generate Time Series Plots
# --------------------------------------
if runTimePlot == 'y':
    timeData = []
    for curLocation in searchLocation:
        print('Current Location: ', curLocation)
        locIndex = func.findLoc(location, curLocation)

        paramSearch = [] 
        locSearch = []
        fileTimeSearch = []
        unitSearch = []
        resultSearch = []
        for i in locIndex:
            paramSearch.append(parameter[i].strip())
            locSearch.append(location[i].strip())
            resultSearch.append(result[i])
            fileTimeSearch.append(fileTime[i])
            unitSearch.append(unit[i])

        for curParam in searchParmeters:
            print('The current parameter is: ', curParam ,' at location: ', curLocation)
            paramIndex = func.findParam(paramSearch, curParam)

            plotLocation = []
            plotdataTime = []
            plotParam = []
            plotResults = []
            plotUnit = []

            for i in paramIndex:
                if math.isnan(float(resultSearch[i])):
                    pass
                else:
                    plotLocation.append(locSearch[i])
                    plotdataTime.append(fileTimeSearch[i])
                    plotParam.append(paramSearch[i])
                    plotResults.append(resultSearch[i])
                    plotUnit.append(unitSearch[i])

                    curDir = os.path.join(locationPlotPath, plotLocation[0])
                    pathlib.Path(curDir).mkdir(parents=True, exist_ok=True)
                    imageName = curDir + '\\' + plotLocation[0] + ' ' + plotParam[0] + '.jpg'

                    curDirParam = os.path.join(paramPlotPath, plotParam[0])
                    pathlib.Path(curDirParam).mkdir(parents=True, exist_ok=True)
                    imageNameParam = curDirParam + '\\' + plotLocation[0] + ' ' + plotParam[0] + '.jpg'

            try:
                if len(plotUnit) != 0 and len(plotResults) != 0 and os.path.isfile(imageName) == False:
                    print('Plotting now')
                    figure = plt.figure(1, figsize=(19.20, 10.80))
                    plotdataTime_obj = [datetime.datetime.strptime(s, "%m/%d/%Y") for s in plotdataTime]
                    figure = plt.plot(plotdataTime_obj, [float(i) for i in plotResults], marker='.', markersize=10)
                    figure = plt.xlabel('Sampling Date')
                    figure = plt.ylabel(plotUnit[0])
                    figure = plt.title(plotLocation[0] + '\n' + plotParam[0], fontweight="bold")
                    plt.rcParams["font.weight"] = "bold"
                    plt.rcParams["axes.labelweight"] = "bold"

                    ax = plt.gca()
                    plotResultsFloat = [float(i) for i in plotResults]
                    if max(plotResultsFloat) >= 999:
                        ax.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
                    for tick in ax.xaxis.get_major_ticks():
                        tick.label1.set_fontweight('bold')
                    for tick in ax.yaxis.get_major_ticks():
                        tick.label1.set_fontweight('bold')

                    plt.grid()
                    plt.gcf().autofmt_xdate(rotation=90)

                    plt.savefig(curDir + '\\' + plotLocation[0] + ' ' + plotParam[0] + '.jpg', dpi=300)
                    plt.savefig(imageNameParam)

                    figure = plt.close()
            except:
                pass

    with open(saveDir + '\\' + folderName + '\\TimeData.csv', 'w') as filehandle:
        for row in timeData:
            filehandle.write('%s\n' % row)
