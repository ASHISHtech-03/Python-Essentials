# Weather Dashboard CLI

A beginner-friendly Python command-line application that fetches **real-time weather data** and a **short forecast** for any city in the world using the OpenWeatherMap API.

---

## Sample Output

```
╔══════════════════════════════════╗
║       Weather Dashboard CLI    ║
╚══════════════════════════════════╝

  Enter city name: London

    Fetching weather for 'London'...

═════════════════════════════════════════════
    Weather in London, GB
═════════════════════════════════════════════
     Temperature  : 14.2°C  (Feels like 13.0°C)
     Condition    : Partly Cloudy
     Humidity     : 72%
     Wind Speed   : 5.1 m/s
     Visibility   : 10.0 km
     Sunrise      : 06:12
     Sunset       : 19:45
═════════════════════════════════════════════

  Short Forecast (next ~15 hours)
  ───────────────────────────────────────────
  Mon 15:00  |   13.5°C  |  Light Rain
  Mon 18:00  |   12.8°C  |  Overcast Clouds
  ...

    Save report to JSON? (y/n): y
    Data saved to 'weather_report.json'
```

---

## Features

- Real-time temperature, feels-like, humidity, wind speed, and visibility
- Short forecast for the next ~15 hours
- Option to save weather data to a JSON file
- Friendly error messages for invalid cities or API issues
- Accepts city name as a command-line argument or via interactive prompt

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ASHISHtech-03/weather-dashboard-cli.git
cd weather-dashboard-cli
```

### 2. Install Dependencies

Make sure you have **Python 3.10+** installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Get a Free API Key

1. Go to [https://openweathermap.org/](https://openweathermap.org/) and create a free account.
2. Navigate to **API Keys** in your account dashboard.
3. Copy your API key.

### 4. Add Your API Key

Open `weather.py` and replace the placeholder on line 8:

```python
API_KEY = "your_api_key_here"   # ← Replace this
```

> **Note:** Free-tier API keys may take up to 10 minutes to activate after creation.

---

## ▶️ How to Run

**Interactive mode (you will be prompted for a city):**

```bash
python weather.py
```

**Pass city name directly:**

```bash
python weather.py Mumbai
python weather.py New York
python weather.py "Kuala Lumpur"
```

---

## Project Structure

```
weather-dashboard-cli/
│
├── weather.py          # Main application file
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── weather_report.json # Auto-generated when you save (not committed)
```

---

## How It Works

1. The user provides a city name.
2. The app sends a GET request to the **OpenWeatherMap Current Weather API**.
3. The JSON response is parsed and displayed in a formatted layout.
4. A second API call fetches the **5-day forecast endpoint** (limited to 5 time slots).
5. The user can optionally save the raw JSON response to a file.

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| `requests` | HTTP API calls |
| `json` | Parsing and saving API responses |
| `datetime` | Formatting timestamps |
| OpenWeatherMap API | Weather data source |

---

## Known Limitations

- Requires an active internet connection.
- Free-tier API allows 60 calls/minute — more than enough for this app.
- Temperature is displayed in Celsius by default (changeable in `weather.py`).

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

**Ashish Kumar Rai**  
Registration No: 24BAI10666  
VIT Bhopal University  
Python Essentials — BYOP Capstone Project  
March 2026
