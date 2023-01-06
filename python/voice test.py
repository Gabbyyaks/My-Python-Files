




engine = pyttsx3.init('sapi5')
engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

( "0" for male voice text to speech, "1" for female voice. )


Main function 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<16:
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
     


def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("hello sir i am your voice assistant. how can i help you?")


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am having a good day sir")
speak("what can i do for you?")

def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "is" and "your" and "name"in text:
    speak("i don't have a name yet,")
speak("my programmer haven't programmed my name.")


//Else and IF statement to Run requested query

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
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

	
        elif 'open youtube' in query:
            speak("opening Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("opening Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("opening Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
       
	//elif 'play music' in query or "play song" or "music" or "open music" in query:
		speak("Ok opening music")//

	elif 'play music' in query or "play song" or "music" or "open music" in query: 
 	      speak ("ok, opening music")
		# music_dir = "C:\\Song"
		music_dir = "C:\Users\GABRIEL\Music"
		songs = os.listdir(music_dir)
		print(songs)
		random = os.startfile(os.path.join(music_dir, songs[1]))

	elif 'show time' in query: or "what's the time" in query:
		strTime = datetime.datetime.now().strfime("% H:% M:% S")
		speak("The time is {strTime}")

	elif  'send mail' in query: or "send email" in query:
	     try:
		  speak("email to who?")
		  to = input()
		  speak("what should i say")
		  content = takeCommand()
		  to = "Receiver email address"
		  sendEmail(to, content)
		  speak("the mail has been sent !")
	    except Exception as e:
		  print(e)
		  speak("AN ERROR OCCURRED! EMAIL NOT SENT, PLEASE CHECK FOR ERRORS AND TRY AGAIN")  
		














