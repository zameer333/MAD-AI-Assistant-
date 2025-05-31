import speech_recognition as sr
import pyttsx3 
import wikipedia
from datetime import datetime
import webbrowser


engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language = "en-in")
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not hear you..")
            return ""
        except sr.RequestError:
            speak("There seems to be an issue with my services.")
            return ""

def process_query(query):
    if "time" in query:
        current_time = datetime.now().strftime('%H:%M:%S')
        response = f"The current time is {current_time}."
        speak(response)
        print(response)
    elif "search wikipedia for" in query:
        topic = query.replace("search wikipedia for", "").strip()
        response = search_wikipedia(topic)
        speak(response)
        print(response)
    elif "open google" in query:
        webbrowser.open("http://www.google.com")
        speak("Opening Google.")
        print("Opening Google.")
    elif "Byee" in query: 
        speak("Goodbye!")
        exit()
    else:
        response = "I'm sorry, I don't understand that command."
        speak(response)
        print(response)


def search_wikipedia(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"The topic is ambiguous. Did you mean: {', '.join(e.options[:5])}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    speak("Hello Zameer, this is your assistant MAD. How can I help you?")
    while True:
        query = listen()
        if query:
            process_query(query)       