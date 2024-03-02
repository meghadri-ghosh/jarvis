import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0].id)
Assistant.setProperty('rate', 220)

def Speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f":{audio}")
    print(" ")
    Assistant.runAndWait()

Speak("Hey sir...")

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source, timeout=5)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language="en-in")
            print(f"you said : {query}")

        except Exception as Error:
            print(Error)
            return None

        return query

def TaskExe():
    def Music():
        Speak("tell me the name of the song")
        musicName = takecommand()
        pywhatkit.playonyt(musicName)
        Speak("enjoy sir")

    while True:
        query = takecommand()

        if 'hi' in query:
            Speak("at your service")
            Speak("how may I help you")

        elif 'how are you' in query:
            Speak("I am fine, what about you")

        elif 'you need some break' in query:
            Speak("OK sir, bye")
            Speak("Thanks for using me")
            break

        elif 'what are you doing' in query:
            Speak("I am advancing myself to assist you")

        elif 'bored' in query:
            Speak("Would you like to listen to some music")

        elif 'bye' in query:
            Speak("OK sir, bye")

        elif 'YouTube search' in query:
            Speak("OK sir, I found this by searching")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("done sir")

        elif 'Google search' in query:
            Speak("This is what I found on the web")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak("done sir")

        elif 'website' in query:
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            Speak("OK sir, doing")
            webbrowser.open(web2)
            Speak("this is what I got on the web")
            Speak("done")

        elif 'thank you' in query:
            Speak("Happy helping you sir....")
            Speak("May I have some rest")

        elif 'Facebook' in query:
            Speak("doing sir")
            webbrowser.open('https://www.facebook.com/')
            Speak("done sir")

        elif 'Instagram' in query:
            Speak("doing sir")
            webbrowser.open('https://www.instagram.com/_.the._.prophet_/')
            Speak("I am done sir, now you can enjoy")

        elif 'mail' in query:
            Speak("Launching sir")
            webbrowser.open('https://mail.google.com/mail/u/0/?ogbl#inbox')
            Speak("done sir")

        elif 'WhatsApp' in query:
            Speak("Wait sir, I am doing")
            webbrowser.open('https://web.whatsapp.com/')
            Speak("done sir...")

        elif 'music' in query:
            Music()

        elif 'screenshot' in query:
            kk = pyautogui.screenshot()
            kk.save('F:\\')

        elif 'any song you like' in query:
            web = 'https://www.youtube.com' + web
            webbrowser.open(web)



TaskExe()
