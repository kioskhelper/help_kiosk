

from gtts import gTTS
import os
import speech_recognition as sr
import time
import playsound
#list size


def speak(text ,lang="ko", speed=False):
    tts = gTTS(text=text, lang=lang , slow=speed)
    tts.save("./tts.mp3")
    os.system("afplay " + "./tts.mp3")

menulist = [] 
Recognizer = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
    audio = Recognizer.listen(source)
        
try:
    data = Recognizer.recognize_google(audio , language="ko")
        
except:
    speak("이해하지 못하는 말이에요")
    print("ljasdljhasd")


count =0 
    
print(data)

    
    
