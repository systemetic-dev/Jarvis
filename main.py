import speech_recognition as sr
import webbrowser
import pyttsx3
from openai import OpenAI
import os


engine = pyttsx3.init()
recognizer = sr.Recognizer()

# def aiprocess(command):
#     client = OpenAI(api_key= '')

#     completions = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": command},
#         ],
#     )
#     return completions.choices[0].message.content
def speak(text):
        engine.say(text)
        engine.runAndWait()

def processControl(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    else:
        # response = aiprocess(c)
        # speak(response)
        pass

if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            print(f"User said: {word}")
            if(word.lower() == "jarvis"):
                speak("yes sir?")
                with sr.Microphone() as source:
                    
                    print("jarvis Active")
                    
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processControl(command)
        except Exception as e:
            print(f"Error: {e}")