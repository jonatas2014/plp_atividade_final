require_relative 'observers'

class Subject

    def registerObserver(observer); end

    def removeObserver(observer); end

    def notifyObservers; end

end

class WeatherData < Subject

    def initialize
        @temperature = 0
        @humidity = 0
        @pressure = 0
        @@observers = []
    end

    def registerObserver(observer)
        @@observers.push(observer)
    end

    def removeObserver(observer)
        @@observers.each do |obs|
            if obs == observer
                @@observers.pop(observer)
            end
        end
    end

    def self.notifyObservers
        @@observers.each do |observer|
            observer.update(@temperature, @humidity, @pressure)
            return nil
        end
    end

    def self.measurementsChanged
        WeatherData.notifyObservers
    end

    def setMeasurements(temperature, humidity, pressure)
        @temperature = temperature
        @humidity = humidity
        @pressure = pressure
        WeatherData.measurementsChanged
    end

    def getTemperatureStation; end

    def getHumidityStation; end

    def getPressureStation; end

end