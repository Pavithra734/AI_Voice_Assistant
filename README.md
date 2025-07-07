# AI_Voice_Assistant

# 🤖 AVI REDDY - AI Voice Assistant

**AVI REDDY** is a voice-activated AI assistant developed in Python. It performs tasks such as telling jokes, reading news, providing weather updates, playing YouTube songs, doing math, and managing system operations (e.g., shutdown, restart). It includes Selenium-powered YouTube automation and integrates with real-time APIs to deliver a smart and interactive experience.

---

## Project Structure

### 1. `jokes.py`
- Fetches random jokes using the Official Joke API.
- Contains the `joke()` function that returns a setup and punchline.

### 2. `main.py`
- Core assistant script that integrates multiple features.
- Uses `pyttsx3` for text-to-speech and `speech_recognition` for voice input.
- Recognizes commands like getting date/time, battery status, system operations (shutdown, restart), opening/closing apps, browsing websites, playing music, telling jokes, news, facts, and weather info.
- Utilizes other modules such as `jokes.py`, `News.py`, `YT_auto.py`, `weather.py` for specialized functions.

### 3. `News.py`
- Retrieves the top 3 latest news headlines from NewsAPI.
- Uses a predefined API key to fetch news data.

### 4. `selenium_web.py`
- A variant of the assistant that integrates Selenium for advanced web automation.
- Supports commands like searching and playing YouTube videos automatically.
- Shares many features with `main2.py` but is focused on Selenium-powered web interactions.

### 5. `weather.py` (embedded in `selenium_web.py` for weather info)
- Uses OpenWeatherMap API to fetch real-time weather data for a given city.
- Returns city name, weather description, and temperature in Celsius.

### 6. `YT_auto.py`
- Selenium automation script to search and play YouTube videos.
- Opens a Chrome browser, searches for the query, and plays the first video result.
- Uses `webdriver_manager` to handle ChromeDriver installation automatically.

---

## 🚀 Features

- 🎧 **Voice Interaction** (Google Speech Recognition + pyttsx3)
- 📅 **Date & Time Updates**
- 🔋 **Battery Status Information**
- 🌐 **Web Browsing Control** (Google, YouTube, Chrome)
- 📚 **Wikipedia Summaries**
- 🎵 **YouTube Music Search** (via Selenium WebDriver)
- 🗞️ **Latest News Headlines** (via NewsAPI)
- 🌡️ **Weather Info** (via OpenWeatherMap API)
- 😂 **Random Jokes** (via Joke API)
- 🤯 **Interesting Random Facts**
- 🧮 **Basic Math Operations** (Add, Subtract, Multiply, Divide)
- 🖥️ **System Controls** (Shutdown, Restart, Open/Close Notepad, Calculator, Chrome)

---

## 🛠️ Installation

1. Clone the repository or download the files.

2. Install required Python packages:
```bash
pip install pyttsx3 speechrecognition psutil wikipedia randfacts word2number selenium webdriver-manager requests
```

3. Get API keys:

- NewsAPI: https://newsapi.org/

- OpenWeatherMap: https://openweathermap.org/api

4.Insert your API keys in News.py and weather.py respectively.

---

## 🚀 How to Run

To start the basic assistant:

```bash
python main.py
```

To start the Selenium-integrated assistant:

```bash
python selenium_web.py
```

---

## 👨‍💻 Developed By

**Mekala Pavithra**  
B.Tech Computer Science  
Sri Venkateswara College of Engineering  
_AI Voice Assistant Project_

---

## 📝 Notes

- Make sure your microphone is enabled and working properly.

- Chrome browser must be installed for Selenium features to work.

- The assistant is tailored for Windows OS commands; adjust system calls for other operating systems as needed.



---

**This README.md includes:**

- Project overview
- Project Structure
- Features list
- Installation instructions
- How to run commands
- Developer info
- Notes

