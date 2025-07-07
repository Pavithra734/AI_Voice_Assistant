import pyttsx3 as p
import speech_recognition as sr
import os
import datetime
import webbrowser
import psutil
import wikipedia
import randfacts
from word2number import w2n
from weather import get_weather
from YT_auto import MusicPlayer
from News import *
from jokes import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen(prompt=None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 1.2)
        if prompt:
            speak(prompt)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand.")
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return None


def open_browser(url):
    speak(f"Opening {url}")
    webbrowser.open(url)


def main_assistant():
    speak("Hello sir, I'm your Selenium-integrated assistant AVI REDDY.")
    
    while True:
        command = listen("What can I do for you?")
        if not command:
            continue

        if "exit" in command or "quit" in command:
            speak("Goodbye sir. Have a great day.")
            break

        elif "search" in command and "youtube" in command:
            video = listen("What should I search on YouTube?")
            if video:
                speak(f"Searching and playing {video} on YouTube.")
                player = MusicPlayer()
                player.play(video)

        elif "open youtube" in command:
            open_browser("https://www.youtube.com")

        elif "open google" in command:
            open_browser("https://www.google.com")

        elif "play" in command and "song" in command:
            song = listen("Which song should I play?")
            if song:
                speak(f"Playing {song} on YouTube.")
                player = MusicPlayer()
                player.play(song)

        elif "joke" in command:
            joke_text = joke()
            speak(joke_text[0])
            speak(joke_text[1])

        elif "news" in command:
            speak("Here are the latest news headlines.")
            for item in news():
                print(item)
                speak(item)

        elif "fact" in command:
            fact = randfacts.get_fact()
            speak("Did you know that, " + fact)

        elif "temperature" in command or "weather" in command:
            city = listen("Please tell me the city name.")
            if city:
                city_actual, description, temperature = get_weather(city)
                if city_actual:
                    speak(f"The weather in {city_actual} is {description} with a temperature of {temperature} degree Celsius.")
                else:
                    speak("Sorry, I couldn't find weather information for that city.")

        else:
            speak("Sorry, I did not understand that command.")


if __name__ == "__main__":
    main_assistant()
