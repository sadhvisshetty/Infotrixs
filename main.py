import requests
import json
import time
from datetime import datetime

API_KEY = "4eebb0d047c7f0ef4e8fc52bbd87323f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
REFRESH_INTERVAL = 30
def get_weather(city_name):
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error:Unable to fetch weather data.")
        return None

def main():
    global date_time
    while True:
        print("Weather Checking Application")
        print("1. Check Weather by City Name")
        print("2. Add City to Favorites")
        print("3. Exit")

        select = input("Enter your choice: ")

        if select == "1":
            city_name = input("Enter your city name: ")
            weather_data = get_weather(city_name)
            if weather_data:
                temp_city = weather_data['main']['temp']
                weather_desc = weather_data['weather'][0]['description']
                hmdt = weather_data['main']['humidity']
                wind_spd = weather_data['wind']['speed']
                date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

                print("----------------------------------------------------------------------------")
                print("Weather starts for - {} || {}". format(city_name.upper(), date_time))
                print("----------------------------------------------------------------------------")

                print("Current Temperature is: {:.2f} deg C".format(temp_city))
                print("Current Weather desc  :", weather_desc)
                print("Current Humidity      :", hmdt, '%')
                print("Current Wind Speed    :", wind_spd, 'kmph')

        elif select == "2":
            list1=[]
            x=int(input("Enter total number of  favourite cities"))
            for i in range(0,x):
                s=str(input())
                if s not in list1:
                    list1.append(s)
            print(f"{list1} are the list of favourite cities")
            break
        elif select == "3":
            print("Existing the application.")
            break
        else:
            print("Invalid Choice. Please try again.")
        time.sleep(REFRESH_INTERVAL)
if __name__ == "__main__":
    main()
