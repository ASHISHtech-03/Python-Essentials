# Project Report
## Weather Dashboard CLI — Python Essentials BYOP Capstone

**Student Name:** Ashish Kumar Rai  
**Registration Number:** 24BAI10666  
**Course:** Python Essentials  
**University:** VIT Bhopal University  
**Submission Date:** March 31, 2026

---

## 1. Problem Statement

Access to real-time weather information is a universal need — from deciding what to wear, to planning travel or outdoor events. Most people rely on smartphone apps or websites for this, but these tools are black boxes that hide how the information is actually retrieved and processed.

For this capstone, I chose to build a **command-line weather application** that directly queries a live public API and presents the results in a clean, readable format. The goal was to understand how real-world software communicates with external services and processes data — a foundational skill for any Python developer.

---

## 2. Why This Project Matters

- **Practical relevance:** Weather apps are used by millions of people daily. Building one from scratch demonstrates understanding of how such tools actually work under the hood.
- **API literacy:** The ability to consume REST APIs is one of the most in-demand beginner skills in the software industry.
- **Learning opportunity:** The project touches on HTTP requests, JSON parsing, error handling, command-line interfaces, and file I/O — core Python concepts covered in this course.
- **Extensibility:** The foundation built here can be extended into a web app, GUI app, or data analysis tool with minimal changes.

---

## 3. Approach and Design

### 3.1 Architecture

The application is a single-file Python script (`weather.py`) structured around four core functions:

| Function | Responsibility |
|---|---|
| `get_weather(city)` | Makes a GET request to the current weather endpoint |
| `get_forecast(city)` | Makes a GET request to the 5-day forecast endpoint |
| `display_weather(data)` | Parses and formats the current weather JSON for the terminal |
| `display_forecast(data)` | Parses and formats forecast data |
| `save_to_file(data)` | Writes the raw JSON response to disk |
| `main()` | Entry point — handles user input and orchestrates the other functions |

### 3.2 Technology Choices

- **`requests` library:** Chosen for its simplicity and readability. It is the industry standard for HTTP in Python and is beginner-accessible.
- **OpenWeatherMap API:** Free tier, no credit card required, supports 60 requests/minute — ideal for a student project.
- **JSON (built-in):** Used to save data to file. No additional library needed.
- **`datetime` (built-in):** Used to convert Unix timestamps from the API into readable sunrise/sunset times.

### 3.3 User Experience Decisions

- The app accepts a city name both as a command-line argument (`python weather.py Mumbai`) and interactively (prompt), making it flexible to use.
- Errors are caught and explained in plain English rather than showing raw Python exceptions.
- Weather data is shown with emoji icons to improve readability in the terminal.

---

## 4. Key Implementation Details

### 4.1 Making the API Call

```python
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}
response = requests.get(BASE_URL, params=params, timeout=10)
response.raise_for_status()
data = response.json()
```

`raise_for_status()` automatically raises an exception for any 4xx or 5xx HTTP response code, which is then caught in the `except` block.

### 4.2 Error Handling

One of the most important lessons was that real-world API calls can fail in many ways — invalid city name, bad API key, no internet, timeout. Each scenario is handled separately:

```python
except requests.exceptions.HTTPError as e:
    if response.status_code == 404:
        print(f"City '{city}' not found.")
    elif response.status_code == 401:
        print("Invalid API key.")
```

### 4.3 Timestamp Conversion

The API returns sunrise and sunset as Unix timestamps (seconds since Jan 1, 1970). Python's `datetime` module converts this to a readable time:

```python
sunrise = datetime.datetime.fromtimestamp(sunrise_ts).strftime("%H:%M")
```

---

## 5. Challenges Faced

### Challenge 1: Understanding the API Response Structure

The OpenWeatherMap API returns a deeply nested JSON object. Understanding which keys to access required carefully reading the API documentation and printing the raw response during development.

**Solution:** I printed `json.dumps(data, indent=2)` to explore the structure before writing the parsing logic.

### Challenge 2: Handling API Key Activation Delay

After creating an OpenWeatherMap account, the free API key takes up to 10 minutes to become active. Initially, all my requests returned `401 Unauthorized`, which I mistakenly thought was a code bug.

**Solution:** I waited and retried, then added clear error messaging in the code so future users don't face the same confusion.

### Challenge 3: Command-line Argument for Multi-word City Names

Cities like "New York" or "Kuala Lumpur" contain spaces. Using `sys.argv[1]` alone would only capture the first word.

**Solution:** Used `" ".join(sys.argv[1:])` to join all arguments after the script name into a single city string.

---

## 6. What I Learned

1. **How REST APIs work:** I now understand how a client sends a GET request with query parameters, receives a JSON response, and parses it — a pattern that applies to virtually every modern API.

2. **The importance of error handling:** A program that crashes with a raw Python traceback is not production-ready. Writing clean, user-friendly error messages makes a real difference to the user experience.

3. **Reading documentation:** The OpenWeatherMap API docs were essential. Learning to navigate and apply external documentation is a crucial developer skill.

4. **Python built-in libraries:** `datetime`, `json`, and `sys` are powerful tools that come with Python and don't need installation — using them effectively reduces dependencies.

5. **Version control habits:** Committing code incrementally on GitHub (instead of a one-time upload) made it easy to track my progress and roll back when something broke.

---

## 7. Possible Future Improvements

- **GUI version** using `tkinter` or a web interface using `Flask`
- **Unit tests** using `pytest` to validate parsing logic
- **Celsius/Fahrenheit toggle** as a command-line flag (`--unit imperial`)
- **Historical weather** using OpenWeatherMap's historical API
- **City autocomplete** to handle misspellings
- **CSV export** in addition to JSON

---

## 8. Conclusion

This project gave me hands-on experience with one of Python's most important real-world use cases: integrating with external web services. By building the Weather Dashboard CLI from scratch, I gained practical knowledge of HTTP requests, JSON data handling, error management, and clean code organisation. The project is functional, well-documented, and extensible — a foundation I can continue to build on.

---

## 9. References

- OpenWeatherMap API Documentation: https://openweathermap.org/api
- Python `requests` library documentation: https://docs.python-requests.org/
- Python `datetime` documentation: https://docs.python.org/3/library/datetime.html
- Real Python — Working with APIs: https://realpython.com/python-api/
