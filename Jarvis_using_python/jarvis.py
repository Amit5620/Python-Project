import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# function to convert the text into speech and play the speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to wish the master as good morning , afternoon etc.. and special day wishes
def wishMe():
    hour = int(datetime.datetime.now().hour)
    date = str(datetime.date.today())
    print(date)
    if '12-25' in date:
        speak("Merry Christmas , Sir ")

    elif '01-01' in date:
        speak("Happy New Year , Sir")

    if hour >= 0 and hour < 12:
        speak("Good Morning , Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon , Sir")

    else:
        speak("Good Evening , Sir ")

    speak("I am Jarvis your virtual Artificial Intelligence and i am here to assist you with a variety of task with best i can , 24 hours a day 7 days a week. System is now fully operational. How may i help you")


# Function to take command from the user in audio format and convert it to text/string format
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia , ")
            print(results)
            speak(results)

        elif 'your name' in query:
            speak("I am Jarvis your virtual Artificial Intelligence and i am here to assist you with a variety of task with best i can ,24 hours a day 7 days a week. System is now fully operational.")

        # todo 1: update your name in place of <name>
        elif 'my name ' in query:
            speak("Sir , Your name is <name>")

        # todo 2: update your birthday here in place of <birthday> in the format of dd-mm
        elif 'my birthday' in query:
            speak("Sir , Your Birthday is on <birthday>. ")

        elif 'wake up' in query:
            speak("Ready at your service Sir . How may i help you . ")

        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        # todo 3: update the directory where you have your songs on your local machine , in the place of <music directory>
        elif 'music' in query:
            music_dir = '<music directory>'
            songs = os.listdir(music_dir)
            speak("Playing Music..")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.date.today()
            speak(f"Sir , Today is {strDate}")

        elif 'thank you' in query:
            speak("It's my pleasure sir ")

        # todo 4: update the directory of vs code in place of <vs code path>
        elif 'open code' in query:
            path = "<vs code path>"
            speak("opening visual studio code")
            os.startfile(path)

        # todo 5: update the directory of chrome in place of <chrome_path>
        elif 'open chrome' in query:
            path = "<chrome_path>"
            speak("opening chrome")
            os.startfile(path)

        elif 'good night ' in query:
            speak("Good night Sir , Sweet  dreams. ")

        elif 'search ' in query:
            query = query.replace('search', "")
            speak(f"Searching on google for {query} ")
            search = "google.com/search?=" + query
            print(search)
            webbrowser.open(search)

# You can also add more functions to it as per your use...