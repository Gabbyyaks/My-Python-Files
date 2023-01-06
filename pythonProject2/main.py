import speech_recognition as sr


# Set up the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# Calibrate the microphone
print("Calibrating microphone...")
with mic as source:
    r.adjust_for_ambient_noise(source)

# Define the commands that the assistant should recognize
commands = {
    "what is your name": "My name is Assistant.",
    "what time is it": "I'm sorry, I don't have the ability to check the time.",
    "what is the weather like": "I'm sorry, I don't have the ability to check the weather.",
    "goodbye": "Goodbye! Have a great day."
}

# Main loop
while True:
    print("Listening...")
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        if text in commands:
            print(commands[text])
        elif "goodbye" in text:
            print("Goodbye! Have a great day.")
            break
        else:
            print("I'm sorry, I don't know how to respond to that.")
    except sr.UnknownValueError:
        print("I'm sorry, I didn't understand what you said.")



