from observers import *
from subject_weather_data import Subject, WeatherData

def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.setMeasurements(26, 65, 30.4)
    weather_data.setMeasurements(28, 70, 29.2)
    weather_data.setMeasurements(25, 90, 29.2) 

main()
