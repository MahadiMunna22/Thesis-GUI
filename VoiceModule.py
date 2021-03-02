import os
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import globalFunc as gf
import global_var_of_ui as glui
import threading

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    try:
        tts.save(filename)
    except:
        os.remove('voice.mp3')
        tts.save(filename)
    playsound(filename)

def get_audio():
    print("waiting to hear ...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: "+str(e))
    return said

light = 0
fan = 0
bedh = 0
bedl = 0
bright = 0
bleft = 0
def SpeechToText():
    global light, fan, bedh, bedl, bright, bleft
    text = get_audio()
    if "light on" in text:

        if(light % 2 == 0):
            gf.select("Light")
            speak("Light is ON")
            print("light is on")
            light += 1
        else:
            speak("Light is already on")
    elif "light off" in text:
        if(light % 2 != 0):
            gf.select("Light")
            speak("Light is OFF")
            print("light is off")
            light += 1
        else:
            speak("Light is already off")

    if "fan on" in text or "fan on" in text or "turn on fan" in text:
        if(fan % 2 == 0):
            gf.select("Fan")
            speak("Fan is ON")
            print("Fan is on")
            fan += 1
        else:
            speak("Fan is already on")
    elif "fan off" in text or "fan of" in text or "pan off" in text or "turn off fan" in text:
        if(fan % 2 != 0):
            gf.select("Fan")
            speak("Fan is OFF")
            print("Fan is off")
            fan += 1
        else:
            speak("Fan is already off")

    if "fan speed up" in text:
        gf.select("Fan Speed Up")
        speak("Fan Speed is Up")
        fan = 1
    
    if "fan speed down" in text:
        gf.select("Fan Speed Down")
        speak("Fan Speed is down")
        fan = 1
    

    if "call nurse" in text or "help" in text:
        gf.select("Call Nurse")
        speak("Calling Nurse")

    if "call family" in text :
        gf.select("Call Family")
        speak("Calling Family")

    if "temperature up" in text or "temperature app" in text:
        gf.select("Hot")
        speak("temperature is increasing")
    
    if "temperature down" in text:
        gf.select("Cold")
        speak("temperature is decreasing")

    if "bed head up" in text:
        if(bedh % 2 == 0):
            gf.select("Bed Head")
            speak("Bed Head is Up")
            bedh += 1
        else:
            speak("Bed Head is already up")
    
    if "bed head down" in text:
        if(bedh % 2 != 0):
            gf.select("Bed Head")
            speak("Bed Head is Down")
            bedh += 1
        else:
            speak("Bed Head is already down")

    if "bed leg up" in text:
        if(bedl % 2 == 0):
            gf.select("Bed Leg")
            speak("Bed Leg is Up")
            bedl += 1
        else:
            speak("Bed Leg is already up")
    
    if "bed leg down" in text:
        if(bedl % 2 != 0):
            gf.select("Bed Leg")
            speak("Bed Leg is Down")
            bedl += 1
        else:
            speak("Bed Leg is already down")
    
    if "bed write up" in text or "bed right up" in text:
        if(bright % 2 == 0):
            gf.select("Bed Right")
            speak("Bed right is Up")
            bright += 1
        else:
            speak("Bed right is already up")
    
    if "bed right down" in text or "bed write down" in text:
        if(bright % 2 != 0):
            gf.select("Bed Right")
            speak("Bed right is Down")
            bright += 1
        else:
            speak("Bed right is already down")
    
    if "bed left up" in text or "bed lift up" in text:
        if(bleft % 2 == 0):
            gf.select("Bed Left")
            speak("Bed Left is Up")
            bleft += 1
        else:
            speak("Bed Left is already up")
    
    if "bed left down" in text:
        if(bleft % 2 != 0):
            gf.select("Bed Left")
            speak("Bed Left is Down")
            bleft += 1
        else:
            speak("Bed Left is already down")

    if "shutdown" in text:
        speak("shutting down")

    return text

def voiceModule():
    while True:
        text = SpeechToText()
        if "shutdown" in text or glui.stopVoice == True:
            glui.root.destroy()
            break
    return
