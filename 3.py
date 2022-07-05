import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()

    if 'roll number' in command:
        talk('Your Roll Number is 1234')
    elif 'full name' in command:
        talk('Abcd Efg Hijk')
    elif 'birthdate' in command:
        talk('15 June 2001')
    elif 'city' in command:
        talk('Abc lives in Xyz ')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()