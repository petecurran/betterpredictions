import json

#Grabs average rainfall on this day from JSON
def getAverageRainOnDate(filePath,today):
    """
    Takes a datetime.today() object and calculates average rainfall on that day.
    """
    with open(filePath,'r') as data:
        rainData = json.load(data)

    #Empty list to hold rain values/
    rainValues = []
    #Find the current year.
    thisYear = int(today.year)
    for i in range(75):
        #Format a search string to match JSON. Starts last year.
        searchString = today.strftime("{}-%m-%d".format(thisYear -1 -i))
        #Get the rain data from the JSON
        rainAmount = float(rainData[searchString])
        rainValues.append(rainAmount)
    #Calc average rainfall and round to 2sf.
    average = round(sum(rainValues) / len(rainValues),2)

    return average

def getAverageRain(filePath):
    """
    Gets average rain for all values in JSON
    """
    with open(filePath,'r') as data:
        rainData = json.load(data)

    #Make a list of all values, cast to floats.
    values = [float(value) for value in rainData.values()]
    #Calc and round to 2sf
    average = round(sum(values)/len(values),2)

    return average

def tenYearHistory(filePath,today):
    """
    Find the rain on this day for the past 10 years.
    """
    with open(filePath,'r') as data:
        rainData = json.load(data)

    #List to hold [year,rainValues]
    rainValues = []
    #Calculates the year
    thisYear = int(today.year)
    for i in range(10):
        #Format a string to match the JSON. Starts last year.
        searchString = today.strftime("{}-%m-%d".format(thisYear-i-1))
        #Get the rainfall on that day
        rainAmount = float(rainData[searchString])
        #Add year and value to list
        year = thisYear-i-1
        rainValues.append([year,rainAmount])

    #Returns a 2D list
    return rainValues