import webbrowser
import openai
import speech_recognition as sr
import os
import pyttsx3
import pygame
import datetime
import random
from config import apikey

chatstr=""
def chat(query):
  #todo :write a program to use open ai key
    global chatstr
    print(chatstr)
    openai.api_key = apikey
    chatstr += f"Garvit: {query}\n Brutus:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=0,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
  )
  #todo: wrap inside a try-catch block
    say(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt:{prompt} \n**********************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
# todo: wrap inside a try-catch block

#     print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("openai files"):
        os.mkdir("openai files")

    with open(f"openai files/{''.join(prompt.split('intelligence')[1:])} - {random.randint(1 , 544447325662)}", "w") as f:
        f.write(text)
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User:{query}")
            return query
        except Exception as e:
            return

if __name__ == '__main__':
    print('Welcome to Brutus A.I')
    say("Hello Garvit, I am Brutus your Desktop Assistant")
    pygame.init()
    pygame.mixer.init()

    while True:
        print("Listening.....")
        query = command()
        # say(query)
        # todo: add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in  query.lower():
                say(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])

                # sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                #          ["google", "https://www.google.com"], ]

        songs = ["raabta", "tum ho"]
        musicPath = [r"C:\Users\hp\Downloads\Raabta Agent Vinod 128 Kbps.mp3",
                 r"C:\Users\hp\Downloads\Tum Ho - Rockstar 128 Kbps.mp3"]
        # todo: add your fav music
        for song in songs:
            if f"Play {song}".lower() in query.lower():
                index = songs.index(song)
                say(f"Playing {song} Sir")
                pygame.mixer.music.load(musicPath[index])
                pygame.mixer.music.play()

# todo: to get the correct time
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir the time is {strfTime}")

        elif "artificial intelligence" .lower() in query.lower():
            say(f"Sir, I have written a response  in the open AI files directory")
            ai(prompt=query)
        elif "Brutus Quit".lower() in query.lower():
            say(
                "Brutus Quitting Sir"
            )
            exit()
        elif "Clear All Chats".lower() in query.lower():
            say("clearing all chats,Sir")
            chatstr=""
        else:
            chat(query)

