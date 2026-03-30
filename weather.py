import requests
import json
import datetime
import sys

# ─────────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────────
API_KEY = "your_api_key_here"   # Replace with your OpenWeatherMap API key

# Author: Ashish Kumar Rai | Reg. No: 24BAI10666
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city: str) -> dict | None:
    """Fetch current weather data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"\n❌  City '{city}' not found. Please check the spelling.")
        elif response.status_code == 401:
            print("\n❌  Invalid API key. Please update the API_KEY in weather.py")
        else:
            print(f"\n❌  HTTP error: {e}")
    except requests.exceptions.ConnectionError:
        print("\n❌  No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        print("\n❌  Request timed out. Try again later.")
    return None


def get_forecast(city: str) -> dict | None:
    """Fetch 5-day (3-hourly) forecast data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "cnt": 5            # Next 5 time-slots (~15 hours ahead)
    }
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def display_weather(data: dict) -> None:
    """Pretty-print current weather data."""
    city        = data["name"]
    country     = data["sys"]["country"]
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    condition   = data["weather"][0]["description"].title()
    wind_speed  = data["wind"]["speed"]
    visibility  = data.get("visibility", 0) / 1000   # metres → km
    sunrise_ts  = data["sys"]["sunrise"]
    sunset_ts   = data["sys"]["sunset"]

    sunrise = datetime.datetime.fromtimestamp(sunrise_ts).strftime("%H:%M")
    sunset  = datetime.datetime.fromtimestamp(sunset_ts).strftime("%H:%M")

    print("\n" + "═" * 45)
    print(f"  🌍  Weather in {city}, {country}")
    print("═" * 45)
    print(f"  🌡️   Temperature  : {temp:.1f}°C  (Feels like {feels_like:.1f}°C)")
    print(f"  🌤️   Condition    : {condition}")
    print(f"  💧   Humidity     : {humidity}%")
    print(f"  🌬️   Wind Speed   : {wind_speed} m/s")
    print(f"  👁️   Visibility   : {visibility:.1f} km")
    print(f"  🌅   Sunrise      : {sunrise}")
    print(f"  🌇   Sunset       : {sunset}")
    print("═" * 45)


def display_forecast(data: dict) -> None:
    """Pretty-print short forecast."""
    print("\n  📅  Short Forecast (next ~15 hours)")
    print("  " + "─" * 43)
    for item in data["list"]:
        time_str  = datetime.datetime.fromtimestamp(item["dt"]).strftime("%a %H:%M")
        temp      = item["main"]["temp"]
        condition = item["weather"][0]["description"].title()
        print(f"  {time_str}  |  {temp:5.1f}°C  |  {condition}")
    print()


def save_to_file(data: dict, filename: str = "weather_report.json") -> None:
    """Save weather data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n  ✅  Data saved to '{filename}'")


def main() -> None:
    print("\n╔══════════════════════════════════╗")
    print("║    🌦️   Weather Dashboard CLI    ║")
    print("╚══════════════════════════════════╝")

    # Accept city name from command-line argument or prompt
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("\n  Enter city name: ").strip()

    if not city:
        print("  ❌  No city provided. Exiting.")
        return

    print(f"\n  ⏳  Fetching weather for '{city}'...")

    weather_data = get_weather(city)
    if not weather_data:
        return

    display_weather(weather_data)

    forecast_data = get_forecast(city)
    if forecast_data:
        display_forecast(forecast_data)

    # Ask user if they want to save
    save = input("  💾  Save report to JSON? (y/n): ").strip().lower()
    if save == "y":
        save_to_file(weather_data)


if __name__ == "__main__":
    main()
