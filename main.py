import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import randfacts
import webbrowser
import time
import os
import subprocess
import winshell
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
        pass
    return command


def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        talk("Good morning")
    elif (hour >= 12) and (hour < 18):
        talk("Good afternoon")
    elif (hour >= 18) and (hour < 23):
        talk("Good evening")
    else:
        talk("You should go to sleep, but ")
    talk("How can I help you?")


def username():
    talk("Hello Sir, What should I call you?")
    uname = take_command()
    talk("Welcome")
    talk(uname)
    talk("How can i help you?")
    return uname


def date():
    now = datetime.datetime.now()

    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                    '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th',
                    '26th', '27th', '28th', '29th', '30th', '31st']

    talk("Today is " + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')


def open_program(browser):
    print(browser)
    if 'google' in browser:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Have fun to look up things")
        time.sleep(5)
    elif 'youtube' in browser:
        webbrowser.open_new_tab("https://www.youtube.com")
        talk("Have fun watching videos")
        time.sleep(5)
    elif 'netflix' in browser:
        webbrowser.open_new_tab("https://www.netflix.com")
        talk("Have fun watching movies or series")
        time.sleep(5)
    elif 'cs50' in browser:
        webbrowser.open_new_tab("https://cs50.harvard.edu/x/2022/")
        talk("Have fun with the best website")
        time.sleep(5)
    elif 'twitch' in browser:
        webbrowser.open_new_tab("https://www.twitch.tv")
        talk("Have fun watching gameplay")
        time.sleep(5)
    elif 'amazon' in browser:
        webbrowser.open_new_tab("https://www.amazon.de")
        talk("Do not buy to much")
        time.sleep(5)
    elif 'brave' in browser:
        code_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
        os.startfile(code_path)
    elif 'discord' in browser:
        code_path = "C:\\Users\\brand\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
        os.startfile(code_path)


def write_note():
    talk("What should i write, sir?")
    note = take_command()
    file = open('jarvis.txt', 'w')
    talk("Should i include date and time?")
    ans = take_command()
    if "of course" in ans or "yes" in ans or "sure" in ans:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(str_time)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)


def get_weather():
    API = "aad2f59ed971a5d32462b9c26deb0f74"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    talk("Of which city do you want to know the weather?")
    city = take_command()
    url = base_url + "appid=" + API + "&q=" + city
    res = requests.get(url)
    x = res.json()
    if x["code"] != "404":
        y = x["main"]
        temp = y["temp"]
        pressure = y["pressure"]
        humidity = y["humidity"]
        z = x["weather"]
        description = z[0]["description"]
        talk("Getting your Result")
        talk("Here you go")
        print("Temperature (in kelvin unit): " + str(temp) + "\n atmospheric pressure (in hPa unit): " + str(pressure)
              + "\n humidity (in percentage): " + str(humidity) + "\n description: " + str(description))


def run_jarvis():
    # while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            times = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + times)
        elif 'wikipedia' in command:
            talk("Searching wikipedia")
            person = command.replace('wikipedia', '')
            info = wikipedia.summary(person, 2)
            talk("According to wikipedia")
            print(info)
            talk(info)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'hello' in command:
            greet()
        elif 'random fact' in command:
            talk(randfacts.get_fact())
        elif 'date' in command:
            date()
        elif 'open' in command:
            open_program(command)
        elif 'write a note' in command:
            write_note()
        elif 'show note' in command:
            talk("Here are your notes, sir")
            file = open("jarvis.txt", "r")
            print(file.read())
            talk(file.read(4))
        elif 'sign out' in command or 'log off' in command:
            talk("Make sure to close everything.")
            time.sleep(5)
            talk("Do you really want to shut down?")
            ans = take_command()
            if 'yes' in ans or 'sure' in ans:
                subprocess.call(["shutdown", "/1"])
        elif 'restart pc' in command:
            subprocess.call(["shutdown", "/r"])
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            talk("Recycle Bin Recycled")
        elif "don't listen" in command or "stop listening" in command:
            talk("for how much seconds you want to stop jarvis from listening commands")
            sleep = int(take_command())
            time.sleep(sleep)
            print(sleep)
        elif 'news' in command:
            webbrowser.open_new_tab('https://news.google.com/')
            talk("Here are some of the latest news for you")
            time.sleep(5)
        elif 'can you search' in command or 'look up' in command:
            talk("Of course sir. What should i look up?")
            search = take_command()
            webbrowser.open_new_tab("https://www.google.com/search?q=" + search)
        elif 'why were you built' in command or "why" in command or "why were you build" in command:
            talk("I was built for the final project of CS50")
        elif 'where is' in command:
            location = command.replace("where is", "")
            talk("Give me a second.............")
            talk("I found it! Here is your location")
            talk(location)
            webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + "")
        elif 'thank you' in command:
            talk("You're welcome Sir.")
        else:
            talk('Please say it again, i did not understand you.')


run_jarvis()
