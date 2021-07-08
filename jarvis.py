
from typing import Sequence
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir... Please tell me how may i help you")

def takeCommand():
    #Takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #Logic for execution tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            print('Opening Youtube...')
            speak('Opening Youtube...')
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            print('Opening Google...')
            speak('Opening Google...')
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak('Opening StackOverFlow...')
            webbrowser.open("stackoverflow.com")
        elif 'social media' in query:
            speak("What you want me to open:-Facebook or Instagram")
            print("What you want me to open:-Facebook/Instagram")
            query=takeCommand().lower()
            
            if 'facebook' in query:
                print("OPening Facebook...")
                speak("opening Facebook...")
                webbrowser.open("facebook.com")
            elif 'instagram' in query:
                print("opening Instagram...")
                speak("Opening Instagram...")
                webbrowser.open("instagram.com")
            else:
                continue
        
        elif 'play music' in query:
            speak("Playing Music...")
            musir_dir='D:\\Non Critical\\songs'
            songs=os.listdir(musir_dir)
            os.startfile(os.path.join(musir_dir,songs[0]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir...The time is ..{strTime}")
        elif 'code' in query:
            speak('Opening Visual Studio Code...')
            codepath="C:\\Users\\rijuc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'swiggy' in query:
            print('Opening swiggy...')
            speak('Opening swiggy...')
            webbrowser.open("swiggy.com")
        elif 'zomato' in query:
            print('Opening Zomato...')
            speak('Opening Zomato...')
            webbrowser.open("zomato.com")
        elif 'open video' in query:
            print("Playing Videos")
            speak('Playing Videos...')
            vid_dir="D:\\Django and Flask VAC\\Videos"
            videos=os.listdir(vid_dir)
            os.startfile(os.path.join(vid_dir,videos[1]))
        elif 'calculator' in query:
            print('Opening Calculator')
            speak('Opening Calculator...')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif 'shutdown' in query:
            speak("Do you wish to shutdown your computer ? (yes or no):")
            shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
  
            if shutdown == 'no':
                   exit()
            else:
                speak("Shutting Down....")
                os.system("shutdown /s /t 5")
        elif 'exit' in query:
            speak("Bye sir...See You Again...Have a nice Day..")
            exit()
        

            
