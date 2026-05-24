#!/usr/bin/env python3
import requests
import json
from datetime import datetime

# --- CONFIGURATION ---
LATITUDE = -27.7333
LONGITUDE = 27.0667
API_KEY = "8bcd81d07c9ef5a23dd709885254d64c"
LOCATION = "Odendaalsrus"
# ---------------------

def get_weather_icon(weather_id, is_night=False):
    if weather_id == 800:
        return "🌙" if is_night else "☀️"
    if 200 <= weather_id < 300: return "⛈"
    if 300 <= weather_id < 400: return "🌧"
    if 500 <= weather_id < 600: return "🌧"
    if 600 <= weather_id < 700: return "❄️"
    if 700 <= weather_id < 800: return "🌫"
    if 801 <= weather_id < 900: return "☁️"
    return "🌤"

def get_moon_phase_icon(phase):
    # Moon phase: 0=new, 0.5=full
    if phase < 0.1 or phase > 0.9: return "🌑"
    if phase < 0.25: return "🌒"
    if phase < 0.4: return "🌓"
    if phase < 0.5: return "🌔"
    if phase < 0.6: return "🌕"
    if phase < 0.75: return "🌖"
    if phase < 0.9: return "🌗"
    return "🌘"

try:
    # Current weather
    current_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric"
    current_resp = requests.get(current_url, timeout=5)
    current_resp.raise_for_status()
    current = current_resp.json()
    
    # Forecast (5 days)
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric"
    forecast_resp = requests.get(forecast_url, timeout=5)
    forecast_resp.raise_for_status()
    forecast = forecast_resp.json()
    
    # Current conditions
    temp = int(current['main']['temp'])
    feels_like = int(current['main']['feels_like'])
    humidity = current['main']['humidity']
    pressure = current['main']['pressure']
    wind_speed = current['wind']['speed'] * 3.6  # m/s to km/h
    weather_id = current['weather'][0]['id']
    desc = current['weather'][0]['description'].title()
    icon = get_weather_icon(weather_id)
    
    # Sunrise/Sunset
    sunrise = datetime.fromtimestamp(current['sys']['sunrise']).strftime("%H:%M")
    sunset = datetime.fromtimestamp(current['sys']['sunset']).strftime("%H:%M")
    
    # Moon phase (approximate)
    moon_age = (datetime.now().toordinal() - 694039) % 29.53
    moon_phase = moon_age / 29.53
    moon_icon = get_moon_phase_icon(moon_phase)
    
    # Build tooltip
    tooltip_text = f"{LOCATION}\n"
    tooltip_text += f"{icon} {desc} • {temp}°C\n"
    tooltip_text += f"Feels Like: {feels_like}°C\n"
    tooltip_text += f"💧 Humidity: {humidity}%\n"
    tooltip_text += f"🌡 Pressure: {pressure} hPa\n"
    tooltip_text += f"💨 Wind: {wind_speed:.1f} km/h\n"
    tooltip_text += f"🌅 Sunrise: {sunrise} • 🌇 Sunset: {sunset}\n"
    tooltip_text += f"{moon_icon} Moon Phase\n"
    tooltip_text += f"\n📅 5-Day Forecast:\n"
    
    # Process forecast - get daily data (one per day at noon)
    daily_forecasts = {}
    for item in forecast['list']:
        date = item['dt_txt'].split(' ')[0]
        if date not in daily_forecasts:
            daily_forecasts[date] = item
    
    # Show next 5 days
    for i, (date, data) in enumerate(list(daily_forecasts.items())[:5]):
        day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%a %d")
        temp_min = int(data['main']['temp_min'])
        temp_max = int(data['main']['temp_max'])
        weather_id = data['weather'][0]['id']
        day_icon = get_weather_icon(weather_id)
        tooltip_text += f"{day_name} {day_icon} {temp_min}°/{temp_max}° {data['weather'][0]['description'].title()}\n"
    
    tooltip_text += f"\nLast updated: {datetime.now().strftime('%H:%M:%S')}"
    
    # Output JSON for waybar
    output = {
        "text": f"{icon} {temp}°C",
        "tooltip": tooltip_text
    }
    print(json.dumps(output))

except Exception as e:
    fallback = {
        "text": "🌤 --°C",
        "tooltip": "Weather data unavailable"
    }
    print(json.dumps(fallback))
