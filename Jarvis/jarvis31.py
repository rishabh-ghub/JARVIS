import pyttsx3
import speech_recognition as sr
import time
from datetime import date
import vlc
engine = pyttsx3.init()
engine.say("good morning mister stark")
while(1):
    engine.say("what do you want me to do")
    engine.runAndWait()
    print('eg:play music,what is the time,recognze my face,etc')
    s=sr.Recognizer()
    with sr.Microphone() as source:
        print('please speak now')
        s.adjust_for_ambient_noise(source)
        data=s.listen(source)
    d=s.recognize_google(data)
    print(d)
    if(d=='play music' or d=='play song' or d=='i want to hear the song'):
        engine.say("what is your mood")
        data=s.listen(source)   
        t=s.recognize_google(data)
        print(t)
        if(t=='happy' or t=='i m happy'):
            p=vlc.MediaPlayer(r"E:\PYTHON\Programs class\Music Player\prog\happy")
        elif(t=='sad' or t=='i m sad'):
            p=vlc.MediaPlayer(r"E:\PYTHON\Programs class\Music Player\prog\sad")
        elif(t=='angry' or t=='i m angry'):
            p=vlc.MediaPlayer(r"E:\PYTHON\Programs class\Music Player\prog\angry")
        elif(t=='fear' or t=='i m fear'):
            p=vlc.MediaPlayer(r"E:\PYTHON\Programs class\Music Player\prog\fear")
        elif(t=='neutral' or t=='i m neutral'):
            p=vlc.MediaPlayer(r"E:\PYTHON\Programs class\Music Player\prog\neutral")
           

    elif(d=='what is the time' or d=='show me the time' or d=='time'):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        engine.say(current_time )
    elif(d=='what is date' or d=='date'):
           today = date.today()
           engine.say(today)
           
