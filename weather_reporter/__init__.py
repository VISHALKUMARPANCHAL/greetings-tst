import requests

class WeatherReporter:
    """A simple class to fetch and display current weather information."""

    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self):
        """Fetch current weather data from the API."""
        params = {
            "latitude": 37.7749,   # Default to San Francisco
            "longitude": -122.4194,
            "current_weather": True
        }

        print(f"Fetching weather for {self.city}...")
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("current_weather", {})
        else:
            print("Error fetching data:", response.status_code)
            return {}

    def display_weather(self):
        """Display formatted weather information."""
        weather = self.get_weather()
        if not weather:
            print("No weather data available.")
            return

        print(f"\nWeather Report for {self.city}:")
        print(f"🌡️  Temperature: {weather['temperature']}°C")
        print(f"💨 Wind Speed: {weather['windspeed']} km/h")
        print(f"🧭 Wind Direction: {weather['winddirection']}°")
        print(f"🕒 Time: {weather['time']}")
