from observers import *

class Subject:

    def registerObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyObservers(self):
        pass

class WeatherData(Subject):

    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        for element in self.observers:
            if (id(element) == id(observer)):
                del element
                break

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
            
    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperatureStation(self):
        # get temperature from the station
        pass

    def getHumidityStation(self):
        # get humidity from the station
        pass

    def getPressureStation(self):
        # get pressure from the station
        pass
        
    #def returnObservers(self):
    #    return self.observers

    


    


        
        


    