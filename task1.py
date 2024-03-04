import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("This is Siri.Please tell me how may i help you")

def takecommand():
    #It takes  microphone input from the user and returns string output

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio =  r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        #logic for executing tasks  based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath="C:\Users\admin\Desktop\py\task1.py"
            os.startfile(codepath)

        
