import speech_recognition as sr

# create recognizer
def CommandListener():
    #create the speech recognizer
    recognizer = sr.Recognizer()
    print("Listening for speech...")

    with sr.Microphone() as source:
      audio = recognizer.listen(source)
      query = recognizer.recognize_google(audio)
      print(f'Listener says:{query}')     

 # functin invocation 
      CommandListener()