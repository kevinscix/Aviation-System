# Name: Kevin Wu
# Student Number: 251284607
class Airport:
    # this function creates the airport object by taking in its parameters and defining them within the object
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    # this function formats the string to print if an object is called upon
    def __repr__(self):
        rep = "{0}({1}, {2})".format(self._code, self._city, self._country)
        return rep

    # getters for the class
    def getCode(self):
        return self._code
    def getCity(self):
        return self._city
    def getCountry(self):
        return self._country
    # setters for the class
    def setCode(self, code):
        self._code = code
    def setCity(self, city):
        self._city = city
    def setCountry(self, country):
        self._country = country












