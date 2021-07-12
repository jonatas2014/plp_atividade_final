from subject_weather_data import *

class Observer:

    def update(self, temp, humidity, pressure):
        pass

class DisplayElement:

    def display(self):
        pass

class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.temperature = 0
        self.humidity = 0
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity

        self.display()
        
    def display(self):
        print("Current conditions: ", self.temperature, "°C degrees, ",
        self.humidity, "% humidity")

class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.max_temperature = -20
        self.min_temperature = 60
        self.temperature_sum = 0
        self.temp_readings = 0
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature_sum += temperature
        self.temp_readings += 1

        if (temperature > self.max_temperature):
            self.max_temperature = temperature

        if (temperature < self.min_temperature):
            self.min_temperature = temperature

        self.display()

    def display(self):
        avg_temp = (self.temperature_sum)/self.temp_readings                        
        print("Avg/Max/Min temperature = ", round(avg_temp, 2), "/",
                                            round(self.max_temperature, 2), "/",
                                            round(self.min_temperature, 2))

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.currentPressure = 29.92
        self.lastPressure = 29.90
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure

        self.display()

    def display(self):
        if (self.currentPressure > self.lastPressure):
            print("Forecast: Improving weather on the way!")
        elif (self.currentPressure == self.lastPressure):
            print("Forecast: More of the same")
        elif (self.currentPressure < self.lastPressure):
            print("Forecast: Watch out for cooler, rainy weather")
        
    

class ThirdPartDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.registerObserver()

    def update(self, temperature, humidity, pressure):
        #Do something else based on the intent of the developer
        pass

    def display(self):
        #display something else based on measurements
        pass