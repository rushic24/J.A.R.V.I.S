import speech_recognition as sr
import pyttsx3


def take_Command():
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command1 = listener.recognize_google(voice,language='en-in')
                command1 = command1.lower()  
                if 'jarvis' in command1: 
                    command1 = command1.replace('jarvis','')
                if 'java' in command1: 
                    command1 = command1.replace('java','')
                
            return command1
        except:
            return 'None'

def talk(text):
    # init function to get an engine instance for the speech synthesis 
    engine = pyttsx3.init()
    
    # say method on the engine that passing input text to be spoken
    engine.say('Hello sir, how may I help you, sir.')
    
    # run and wait method, it processes the voice commands. 
    engine.runAndWait()

while True:
    command = take_Command()
    talk(command)
    break
    print(command)