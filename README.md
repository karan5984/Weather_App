# Weather_App

# Weather App - Python

## 🌦️ Overview
This is a simple **Weather Application** written in Python that fetches real-time weather data for a user-specified city using the **OpenWeatherMap API**. The program provides essential weather details such as temperature, humidity, wind speed, and general weather conditions.

## 🚀 Features
- Fetches real-time weather data.
- Displays key weather details:
  - 🌡 Temperature (°C)
  - 💧 Humidity (%)
  - ☁️ Weather Condition (Clear sky, Rainy, etc.)
  - 💨 Wind Speed (m/s)
- Includes **error handling** for:
  - Invalid city names.
  - Incorrect or missing API keys.
  - Network connection issues.

## 🛠️ Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Steps to Run
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/weather-app.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd weather-app
   ```
3. **Install dependencies:**
   ```sh
   pip install requests
   ```
4. **Get an API key** from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
5. **Add your API key** to the script:
   ```python
   API_KEY = "your_api_key_here"
   ```
6. **Run the script:**
   ```sh
   python weather_app.py
   ```

## 📖 Usage
Upon running the script, the following options are displayed:
```
Task List:
 1️⃣ Check Weather
 2️⃣ Information and Instructions
 3️⃣ Exit
```
### How to Check the Weather
1. Select option `1` to check the weather.
2. Enter the name of the city.
3. The program will fetch and display the weather details.
4. You can check the weather for another city by entering "yes" or return to the main menu by entering "no".

### Example Run
```
Enter city name: London

City: London
Temperature: 15°C
Humidity: 60%
Condition: Clear sky
Wind Speed: 5.2 m/s
```

## 🤝 Contributing
Contributions are welcome! Follow these steps:
1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Make your changes and commit** (`git commit -m 'Added a new feature'`)
4. **Push to your branch** (`git push origin feature-branch`)
5. **Open a Pull Request**

## 🌟 Support
If you like this project, don't forget to ⭐ it on GitHub!

