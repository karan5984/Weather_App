#REQUESTS MODULE
import requests

#API KEY FOR CONNECTION AND BASE URL TO REQUEST DATA
API_KEY = "Enter your API key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#FUNCTION TO FETCH WEATHER DETAILS OF GIVEN CITY
def weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    #CONDITONS TO CHECK THE ERROR DUE TO API
    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        print("\nCity:", city.title())
        print("Temperature:", temp,"°C")
        print("Humidity:", humidity,"%")
        print("Condition:", condition)
        print("Wind Speed:", wind_speed,"m/s")
    elif response.status_code == 404:
        print("\nError: City not found. Please check the name and try again...")
    elif response.status_code == 401:
        print("\nError: Invalid API key! Please try again later...")
    else:
        print("\nError: Something went wrong. Please try again...")

#FUNCTION TO CHECK ABOUT THE PROGRAM
def info():
    print("""\n ABOUT THE PROGRAM
This is a simple command-line weather application written in Python. It fetches the current weather data for a user-specified city using the OpenWeatherMap API and displays key details like:
- Temperature (in Celsius)
- Humidity
- Weather condition (e.g., "Clear sky", "Rainy")

The program also includes error handling for:
- Invalid city names
- Missing or incorrect API keys
- Network connection issues""")

#TASK LIST
def task():
    print("\nTask List:\n 1.Check Weather.\n 2.Information and Instructions.\n 3.Exit.")
    global choice
    choice = int(input(" Enter your choice: "))

#BEGINNING
task()
while (True):
    if choice == 1:
        again = "yes"
        while (True):
            if again.lower() == "yes":
                city = input("\nEnter city name: ")
                weather(city)
                again = input("\nEnter "yes" to check again else "no" to get to task list: ")
            elif again.lower() == "no":
                task()
                break
            else:
                print("Invalid input. Please try again...")
                again = input("\nEnter "yes" to check again else "no" to get to task list: ")
    elif choice == 2:
        info()
        task()
    elif choice == 3:
        print("\nThanks for using the program!")
        break
    else:
        print("\nInvalid Input. Please try again...")
        task()
