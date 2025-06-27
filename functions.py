# ================================
# functions.py with Obnoxious Comments
# ================================

# Importing numpy, a high-performance library used for numerical operations.
# Here it's mainly used for finding unique values in a list.
import numpy as np 

# ----------------------------------------------------
# Function: findLoc
# Purpose: Find indices in fullList where searchString matches.
# Arguments:
#   - fullList: list of strings (likely locations)
#   - searchString: the value to search for
# Returns:
#   - List of indices where fullList equals searchString
# ----------------------------------------------------
def findLoc(fullList, searchString):
    index = []  # This will store all matching indices
    b = 0       # This variable seems unused but might have been for debugging
    for i, curString in enumerate(fullList):  # Loop through list with index and value
        if searchString == curString:         # Check if the current string matches the target
            index.append(i)                  # If so, store the index
        if i == 25518:                       # If we hit a specific index (why 25518?) Magic fucking number lost to time.
            print(i)                         # Print the index (probably legacy debug code)
    return index  # Return the list of matched indices

# ----------------------------------------------------
# Function: findParam
# Purpose: Identical in structure to findLoc, but used for parameters.
# Arguments:
#   - fullList: list of strings (likely parameters)
#   - searchString: the value to search for
# Returns:
#   - List of indices where fullList equals searchString
# ----------------------------------------------------
def findParam(fullList, searchString):
    index = []  # Prepare an empty list to collect matching indices
    for i, curString in enumerate(fullList):  # Loop through the list
        if searchString == curString:         # Match found
            index.append(i)                   # Store the index
    return index  # Return the resulting list of indices

# ----------------------------------------------------
# Function: locReplace
# Purpose: Replace all instances of one value with another in a list.
# Arguments:
#   - replaceWith: new value to insert
#   - itemsToReplace: the value we are trying to replace
#   - locationFunc: the list in which replacement should happen
# Returns:
#   - Modified list with replacements done
# ----------------------------------------------------
def locReplace(replaceWith, itemsToReplace, locationFunc):
    for i, curLocation in enumerate(locationFunc):  # Loop over list with index
        if curLocation == itemsToReplace:           # Match found
            locationFunc[i] = replaceWith           # Replace it
    return list(locationFunc)  # Return the modified list

# ----------------------------------------------------
# Function: checkDir
# Purpose: Ensure a directory exists fresh. Removes and recreates.
# Arguments:
#   - path: full path to check and recreate
# Notes:
#   - Warning: This deletes existing files if they share the path name!
# ----------------------------------------------------
def checkDir(path):
    import os  # Import os locally (though it's better to import at the top)
    if os.path.exists(path):  # If path exists...
        os.remove(path)       # ...delete it. This could error if it's not a file!
    os.makedirs(path)         # Create a new directory structure

# ----------------------------------------------------
# Function: locAndSourceReplace
# Purpose: Replace a location if both the location and its data source match.
# Arguments:
#   - replaceWith: value to replace with
#   - locToReplace: location string to search for
#   - sourceToReplace: source string to match alongside location
#   - locationFunc: list of locations
#   - sourceFunc: list of sources
# Returns:
#   - Modified location list after replacement
# ----------------------------------------------------
def locAndSourceReplace(replaceWith, locToReplace, sourceToReplace, locationFunc, sourceFunc):
    for i, curLocation in enumerate(locationFunc):  # Go through locations
        if curLocation == locToReplace and sourceToReplace == sourceFunc:  # Match both
            locationFunc[i] = replaceWith  # Do the replacement
    return list(locationFunc)  # Return updated list

# ----------------------------------------------------
# Function: unique
# Purpose: Print and return unique elements in a list
# Arguments:
#   - list1: a list (likely strings or numerics)
# Returns:
#   - A numpy array of unique values
# Side Effects:
#   - Prints the unique values to stdout
# ----------------------------------------------------
def unique(list1): 
    x = np.array(list1)     # Convert to numpy array to use numpy utilities
    print(np.unique(x))     # Print unique values (user feedback)
    return np.unique(x)     # Return array of unique values
