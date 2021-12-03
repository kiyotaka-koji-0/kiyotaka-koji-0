import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init("sapi5", False)
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def speak(audio):
    print("   ")
    engine.say(audio)
    print("J.A.R.V.I.S "f": {audio}")
    print("   ")
    engine.runAndWait()

def tackcommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("reconizing.....")
            qury = command.recognize_google(audio, language="en-in")
            print(f"You Said : {qury}")
        except Exception as Error:
            return "none"
        
        return qury.lower()

def taskexe():

    while True:
        qury = tackcommand()

        if "jarvis" in qury:
            speak("hello sir , i am jarvis")
            speak("ji sir")
        elif "how are you" in qury:
            speak("me thik ho sir")
            speak("aapp kenseee he")

        elif "youtube search" in qury:
            qury =  qury.replace("jarvis", "")
            qury = qury.replace("youtube search", "")
            speak("sir topic kya ha")
            name3 = tackcommand()
            web  = "https://www.youtube.com/results?search_query=" + name3
            webbrowser.open(web)
            speak("done sir")
        elif "web" in qury:
            speak("sir website ka name")
            name = tackcommand()
            qury = qury.replace("jarvis", "")
            qury = qury.replace("open", "")
            web = "https://www." + name + ".com"
            webbrowser.open(web)
            speak("done sir")
        elif "google" in qury:
            speak("ok sir")
            name1 = tackcommand()
            web1 = "https://" + name1 + ".google.com"
            webbrowser.open(web1)
            speak("done sir")
        elif "bye" in qury:
            speak("ok sir bye sir")
            break
        elif "search" in qury:
            speak("sir what thing you want to search")
            name2 = tackcommand()
            web2 = "https://www.google.com/search?q=" + name2
            webbrowser.open(web2)
            speak("done sir")
        elif "addition" in qury:
           
            speak("sir please tell the first number")
            name4 = int(tackcommand())
            speak("sir please tell the second number")
            name5 = int(tackcommand())
            cal1 = speak(name4 + name5)
            speak("sir the calculation completed")

        elif "subtract" in qury:
           
            speak("sir please tell the first number")
            name6 = int(tackcommand())
            speak("sir please tell the second number")
            name7 = int(tackcommand())
            cal2 = speak(name6 - name7)
            speak("sir the calculation completed")

        elif "multiply" in qury:
           
            speak("sir please tell the first number")
            name8 = int(tackcommand())
            speak("sir please tell the second number")
            name9 = int(tackcommand())
            cal3 = speak(name8 * name9)
            speak("sir the calculation completed")
        
        elif "divide" in qury:
           
            speak("sir please tell the first number")
            name10 = int(tackcommand())
            speak("sir please tell the second number")
            name11 = int(tackcommand())
            cal4 = speak(name10 / name11)
            speak("sir the calculation completed")
     

taskexe()
