import os.path
import openai
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
from config import apikey

# Initialize the text-to-speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that helps users write resignation emails to their bosses."
            },
            {
                "role": "user",
                "content": prompt  # Use the user's input as the prompt
            }
        ],
        temperature=0.7,  # Adjust temperature as needed for desired randomness.
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)  # Write the AI response to the file

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()  # Convert the input to lowercase for easier comparison
        except Exception as e:
            return "Sorry, I couldn't catch that."

while True:
    s = "hello I am Jarvis A.I"
    speaker.Speak(s)
    print("Listening...")
    text = takecommand()
    speaker.Speak(text)
    while True:
        print("listening...")
        text = takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["wikipedia", "https://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "the time" in text:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Sir the Time is {hour} hours and {min} minutes")
        if "using Artificial intelligence".lower() in text.lower():
            ai(prompt=text)  # Use the user's input as the prompt for AI
