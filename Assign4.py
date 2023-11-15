# Name: Kevin Wu
# Student Number: 251284607
# This program takes in the file names of airports and flights and based on the function called will provide you infomation that you request
from Airport import *
from Flight import *


# initialize the lists and dictionary for the file
allAirports = []
allFlights = dict()

# this function takes in the file names and loads and processes the data within them
def loadData(airportFile, flightFile):
    # It tries loading the file and reading the information if not then it will return false, or else it returns true
    try:
        # reads line by line processes it and creates the object then adds to the list
        fileContent = open(airportFile, "r", encoding='utf8')
        for line in fileContent:
            tempList = line.split(",")
            airport = Airport(tempList[0].strip(), tempList[2].strip(), tempList[1].strip())
            allAirports.append(airport)
        fileContent.close()


        # reads the file puts it in a list and then puts it in a bigger list
        fileContent = open(flightFile, "r", encoding='utf8')
        listOfEverything = []
        for line in fileContent:
            tempList = line.split(",")
            listOfEverything.append(tempList)

        # loops through the bigger list and grabs the key and finds all instances of the key puts it in a list then adds it to the dictionary
        for list in listOfEverything:
            key = list[1].strip()
            tempList = []
            for line in listOfEverything:
                if line[1].strip() == key:
                    flightNo = line[0].strip()
                    origin = line[1].strip()
                    airport1 = ""
                    airport2 = ""
                    for i in allAirports:
                        if i.getCode() == line[1].strip():
                            airport1 = i
                        elif i.getCode() == line[2].strip():
                            airport2 = i
                    flight = Flight(flightNo, airport1, airport2)
                    tempList.append(flight)
            #allFlights[origin] = []
            allFlights[origin] = tempList

    except FileNotFoundError:
        return False
    else:
        return True

# this function grabs the airport from its code
def getAirportByCode(code):
    # airport = Airport("A", "A", "A")
    # for i in range(0, len(allAirports), 1):
    #     if allAirports[i].getCode() == code:
    #         airport = allAirports[i]
    # if airport.getCode == "A":
    #     return -1
    # else:
    #     return airport
    for airport in allAirports:
        if code == airport.getCode():
            return airport
    return -1

# this function finds all flights from and to this city
def findAllCityFlights(city):
    listOfFlights = []
    airportCode = ""
    for i in allAirports:
        if i.getCity() == city:
            airportCode = i.getCode()
    # loops through all values of the dictionary to find the airports that match the code
    for flightList in allFlights.values():
        for flights in flightList:
            if flights.getOrigin().getCode() == airportCode or flights.getDestination().getCode() == airportCode:
                listOfFlights.append(flights)
    return listOfFlights

# this function finds all flights from and to this country
def findAllCountryFlights(country):
    listOfAirports = [] # countrylist
    listOfFlights = []
    for airport in allAirports:
        if airport.getCountry() == country:
            listOfAirports.append(airport)
    # loops through all values of the dictionary to find the airports that match the country
    for flightList in allFlights.values():
        for flights in flightList:
            if flights.getOrigin() in listOfAirports or flights.getDestination() in listOfAirports:
                listOfFlights.append(flights)
    return listOfFlights

# this function finds all direct flights or one stop flights between the origin and destination if none then return -1
def findFlightBetween(origAirport, destAirport):
    # checks for direct flights
    for flight in allFlights[origAirport.getCode()]:
        if flight.getDestination() == destAirport:
            return "Direct Flight: %s to %s"%(origAirport.getCode(), destAirport.getCode())
    setOfPossible = set()
    # checks for 1 stop flights
    for flight in allFlights[origAirport.getCode()]:
        for secondFlight in allFlights[flight.getDestination().getCode()]:
            if secondFlight.getDestination() == destAirport:
                setOfPossible.add(secondFlight.getOrigin().getCode())
    if not len(setOfPossible) == 0:
        return setOfPossible
    else:
        return -1
# finds the flight return trip
def findReturnFlight(firstFlight):
    newOrigin = firstFlight.getDestination()
    newDestination = firstFlight.getOrigin()
    for flight in allFlights[newOrigin.getCode()]:
        if flight.getDestination() == newDestination:
            return flight
    return -1
