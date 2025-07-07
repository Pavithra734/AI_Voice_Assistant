import pyttsx3 as p
import speech_recognition as sr
import os
import datetime
import webbrowser
import psutil
import wikipedia
import pywhatkit
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


def get_number(prompt):
    while True:
        response = listen(prompt)
        if response:
            try:
                num = w2n.word_to_num(response)
                return float(num)
            except:
                try:
                    num = float(response)
                    return num
                except:
                    speak("Sorry, I didn't catch the number. Please repeat.")
        else:
            speak("Please say the number again.")


def open_browser(url):
    speak(f"Opening {url}")
    webbrowser.open(url)


def system_shutdown():
    speak("Shutting down the system.")
    os.system("shutdown /s /t 5")


def system_restart():
    speak("Restarting the system.")
    os.system("shutdown /r /t 5")


def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"Your battery is at {percent} percent.")
    else:
        speak("Sorry, I couldn't access battery information.")


def main_assistant():
    speak("Hello sir, I'm your AI assistant AVI REDDY.")
    
    while True:
        command = listen("What can I do for you?")
        if not command:
            continue

        if "exit" in command or "quit" in command:
            speak("Goodbye sir. Have a great day.")
            break

        elif "date" in command:
            today_date = datetime.datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
            speak("Today is " + today_date)

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "battery" in command and "percent" in command:
            battery_status()

        elif "information" in command or "what is" in command:
            topic = listen("What topic do you need information on?")
            if topic:
                try:
                    summary = wikipedia.summary(topic, sentences=2)
                    speak(summary)
                except:
                    speak("I couldn't find clear information, please be more specific.")

        elif "play" in command and ("song" in command or "music" in command or "video" in command):
            video = listen("What would you like me to play?")
            if video:
                speak(f"Playing {video} on YouTube.")
                player = MusicPlayer()
                player.play(video)

        elif "news" in command:
            speak("Here are the latest news headlines.")
            for item in news():
                print(item)
                speak(item)

        elif "fact" in command or "facts" in command:
            fact = randfacts.get_fact()
            speak("Did you know that, " + fact)

        elif "joke" in command or "jokes" in command:
            joke_text = joke()
            speak(joke_text[0])
            speak(joke_text[1])

        elif "temperature" in command or "weather" in command:
            city = listen("Please tell me the city name.")
            if city:
                city_actual, description, temperature = get_weather(city)
                if city_actual:
                    speak(f"The weather in {city_actual} is {description} with a temperature of {temperature} degree Celsius.")
                else:
                    speak("Sorry, I couldn't find weather information for that city.")

        elif "open notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad.exe")

        elif "close notepad" in command:
            speak("Closing Notepad.")
            os.system("taskkill /im notepad.exe /f")

        elif "open calculator" in command:
            speak("Opening Calculator.")
            os.system("calc.exe")

        elif "close calculator" in command or "close calc" in command:
            speak("Closing Calculator.")
            os.system("taskkill /im calculator.exe /f")

        elif "open chrome" in command:
            speak("Opening Chrome.")
            os.system("start chrome")

        elif "close chrome" in command:
            speak("Closing Chrome.")
            os.system("taskkill /im chrome.exe /f")

        elif "open youtube" in command:
            open_browser("https://www.youtube.com")

        elif "open google" in command:
            open_browser("https://www.google.com")

        elif "close browser" in command:
            speak("Closing the browser.")
            os.system("taskkill /im chrome.exe /f")

        elif "add" in command or "sum" in command or "add two numbers" in command:
            num1 = get_number("First number?")
            num2 = get_number("Second number?")
            result = num1 + num2
            speak(f"The sum is {result}")

        elif "subtract" in command or "minus" in command or "subtract two numbers" in command:
            num1 = get_number("First number?")
            num2 = get_number("Second number?")
            result = num1 - num2
            speak(f"The result is {result}")

        elif "multiply" in command:
            num1 = get_number("First number?")
            num2 = get_number("Second number?")
            result = num1 * num2
            speak(f"The product is {result}")

        elif "divide" in command:
            num1 = get_number("First number?")
            if num1 is None:
                speak("Couldn't understand. Please type the number.")
                num1 = float(input("Enter first number: "))
            num2 = get_number("Second number?")
            if num2 is None:
                speak("Couldn't understand. Please type the number.")
                num2 = float(input("Enter second number: "))
            if num2 == 0:
                speak("Division by zero is not allowed.")
            else:
                result = num1 / num2
                speak(f"The result is {result}")

        elif "shutdown" in command:
            confirm = listen("Are you sure you want to shutdown? Say yes to proceed.")
            if confirm and "yes" in confirm:
                system_shutdown()

        elif "restart" in command:
            confirm = listen("Are you sure you want to restart? Say yes to proceed.")
            if confirm and "yes" in confirm:
                system_restart()

        else:
            speak("Sorry, I did not understand that command.")


if __name__ == "__main__":
    main_assistant()
