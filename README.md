# Weather App

A simple and elegant weather application that shows current weather conditions for any city worldwide.

## Features
- Clean and modern user interface
- Real-time weather data from OpenWeatherMap API
- Displays temperature, weather description, "feels like" temperature, humidity, and wind speed
- Error handling for invalid cities or network issues

## Setup

1. First, get your API key:
   - Go to [OpenWeatherMap](https://openweathermap.org/)
   - Sign up for a free account
   - Get your API key from your account dashboard

2. Create a `.env` file in the project root and add your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

After setup, simply run:
```bash
python weather_app.py
```

## Usage
1. Enter a city name in the text field
2. Click the "Search" button or press Enter
3. The weather information will be displayed below

## Error Handling
The app handles various error cases:
- Invalid city names
- Network connection issues
- Missing API key
- API errors

## Technologies Used
- Python 3
- tkinter for GUI
- requests for API calls
- OpenWeatherMap API
- python-dotenv for environment variables 