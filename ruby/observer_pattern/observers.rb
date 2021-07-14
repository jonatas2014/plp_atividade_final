require_relative 'subject_weather_data'

module Observer

    def update(temp, humidity, pressure); end

end

module DisplayElement

    def display; end

end

class CurrentConditionsDisplay

    include Observer
    include DisplayElement

    def initialize(weather_data)
        @temperature = 0
        @humidity = 0
        @weather_data = weather_data
        @weather_data.registerObserver(self)
    end

    def self.display
        puts "Current conditions: #{@temperature}°C degrees, #{@humidity}% humidity"
    end

    def update(temperature, humidity, pressure)
        @temperature = temperature
        @humidity = humidity
        CurrentConditionsDisplay.display
    end

end

class StatisticsDisplay
    include Observer
    include DisplayElement

    def initialize(weather_data)
        @max_temperature = -20
        @min_temperature = 60
        @temperature_sum = 0
        @temp_readings = 0
        @weather_data = weather_data
        @weather_data.registerObserver(self)
    end

    def self.display
        avg_temp = @temperature_sum/@temp_readings
        puts "Avg/Max/Min temperature = #{avg_temp.round(2)}/#{@max_temperature.round(2)}/#{@min_temperature.round(2)}"
    end

    def update(temperature, humidity, pressure)
        @temperature_sum += temperature
        @temp_readings += 1

        if temperature > @max_temperature
            @max_temperature = temperature
        end

        if temperature < @min_temperature
            @min_temperature = temperature
        end
        StatisticsDisplay.display
    end

end

class ForecastDisplay
    include Observer
    include DisplayElement

    def initialize(weather_data)
        @currentPressure = 29.92
        @lastPressure = 29.90
        @weather_data = weather_data
        @weather_data.registerObserver(self)
    end

    def update(temperature, humidity, pressure)
        @lastPressure = @currentPressure
        @currentPressure = pressure
        ForecastDisplay.display
    end

    def self.display
        if @currentPressure > @lastPressure
            puts "Forecast: Improving weather on the way!"
        elsif @currentPressure == @lastPressure
            puts "Forecast: More of the same"
        else
            puts "Forecast: Watch out for cooler, rainy weather"
        end
    end
end

class ThirdPartDisplay
    include Observer
    include DisplayElement

    def initialize(weather_data)
        @weather_data = weather_data
        @weather_data.registerObserver
    end

    def update(temperature, humidity, pressure); end

    def self.display; end

end







