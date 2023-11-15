# Name: Kevin Wu
# Student Number: 251284607
from Airport import *


class Flight:
    # this function creates the flight object by taking in its parameters and defining them within the object
    def __init__(self, flightNo, origin, destination):
        # print(flightNo)
        self._flightNo = ""
        self._origin = origin
        self._destination = destination

        # Check if the destination and origin are airport objects before creating the object or else it will raise a type error
        t1 = isinstance(self._origin, Airport)
        t2 = isinstance(self._destination, Airport)
        if t1 and t2:
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")

    # this function formats the string to print if an object is called upon
    def __repr__(self):
        whereTo = ""
        if self.isDomesticFlight():
            whereTo = "domestic"
        else:
            whereTo = "international"
        rep = "Flight: %s from %s to %s {%s}"%(self._flightNo, self._origin.getCity(), self._destination.getCity(), whereTo)
        return rep

    # this funcion checks if the object and other object have the same trip ignoring the flight number
    def __eq__(self, other):
        if isinstance(other, Flight):
            if self._origin == other.getOrigin() and self._destination == other.getDestination():
                return True
        else:
            return False

    # this function checks if it is a domestic flight or it goes out of country
    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    # getters for this class
    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    # setters for this class
    def setFlightNumber(self, flightNo):
        self._flightNo = flightNo

    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination
