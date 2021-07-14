require_relative 'observers'
require_relative 'subject_weather_data'

if __FILE__ == $0

    weather_data = WeatherData.new

    current_display = CurrentConditionsDisplay.new(weather_data)
    statistics_display = StatisticsDisplay.new(weather_data)
    forecast_display = ForecastDisplay.new(weather_data)

    weather_data.setMeasurements(26, 65, 30.4)
    weather_data.setMeasurements(28, 70, 29.2)
    weather_data.setMeasurements(25, 90, 29.2)

end