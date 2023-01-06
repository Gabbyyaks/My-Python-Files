
import pyttx3 as


engine = pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


r = sr.Recognizer()

speak("hello sir i am your voice assistant. how can i help you?")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def username():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))



with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am having a good day sir")
speak("what can i do for you?")


def speak(text):
    engine.say(text)
    engine.runAndWait()


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "is" and "your" and "name" in text:
    speak("i don't have a name yet,")
speak("my programmer haven't programmed my name.")



if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        if 'wikipedia' in query:
            speak("Searching wikipedia...")

            query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)


