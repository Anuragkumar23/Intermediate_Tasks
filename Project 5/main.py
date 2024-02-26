
import pyttsx3
import speech_recognition as sr

import webbrowser
import os
import schedule
import smtplib
from email.message import EmailMessage
import feedparser
import wikipedia
import dateparser
from googletrans import Translator

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def set_reminder(task, date_time):
    # Schedule reminder
    schedule.every().day.at(date_time).do(send_notification, task)


def send_notification(task):
    # Send notification to user
    print(f"Reminder: {task}")


def send_email(recipient, subject, body):
    # Authenticate with email provider
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    password = 'your_password'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)

        # Compose email
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient

        # Send email
        server.send_message(msg)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak(" Assistance Jaitra activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("I am Jaitra developed by Anurag Kumar")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")

        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        if 'set reminder' in query:
            # Parse user input and set reminder
            speak("Please tell me what task you want to be reminded about.")
            task_description = take_command().lower()

            speak("When do you want to be reminded? Please specify the date and time.")
            reminder_date_time = take_command().lower()

            # Set reminder
            set_reminder(task_description, reminder_date_time)
            pass
        elif 'send email' in query:
            # Parse user input and send email
            speak("Who do you want to send the email to?")
            recipient = take_command().lower()

            speak("What is the subject of the email?")
            subject = take_command().lower()

            speak("What is the content of the email?")
            body = take_command().lower()

            # Send email
            send_email(recipient, subject, body)
            pass
        elif 'read news headlines' in query:
            # Read news headlines
            pass
        elif 'answer question' in query:
            # Parse user input and answer question
            pass
        elif 'translate text' in query:
            # Parse user input and translate text
            pass
        elif 'provide recommendations' in query:
            # Parse user input and provide recommendations
            pass
        elif 'voice notes' in query:
            # Parse user input and handle voice notes
            pass
        elif 'sleep' in query:
            exit(0)
