import calendar
import datetime
import re

import pyttsx3
import speech_recognition as SR
from functions.constants import Constant as C
from functions.functions import Functions


class Base(Functions):
    def __init__(self):
        super(Base, self).__init__()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def speak(self, audio):
        print(audio)
        self.engine.say(audio)
        self.engine.runAndWait()

    def greeting(self):
        self.speak("Hello sir Hope Doing Great")
        self.speak("Authenticate Yourself")
        self.authentication()
        # self.works()

    def authentication(self):
        print("Tell me Your ID")
        data = self.voice_conv()
        if re.search("567", data, re.IGNORECASE):

            self.speak("Welcome Namilakonda Rahul sir")
            self.gretting_time()
        elif re.search("420", data, re.IGNORECASE):
            self.speak("Welcome Sharath Sir")
            self.gretting_time()
        else:
            self.speak("Sorry you are not correct one")

    def voice_conv(self):
        r = SR.Recognizer()
        with SR.Microphone() as source:
            print("Listening")
            audio = r.listen(source)
            try:
                data = "" + r.recognize_google(audio)
                return data
            except Exception as e:
                print(e)

    def gretting_time(self):
        date = datetime.datetime.now().strftime("%H:%M:%S")
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        week = datetime.datetime.now().weekday()
        week = calendar.day_name[week]
        self.speak("Time  " + date)
        self.speak("Year  " + str(year))
        self.speak("Month is " + str(month))
        self.speak("Today is " + str(week))
        self.speak("What can i do for you sir")
        self.works()

    def works(self):
        flag = False
        # For The second time Usage
        if flag == True:
            print("AnyThing Else Sir")

        work = self.voice_conv()
        if re.search("Whatsapp", work, re.IGNORECASE):
            self.open_whatsapp()
            flag = True
            self.works()
        elif re.search("explorer", work, re.IGNORECASE):
            self.open_file_explorer()
            flag = True
            self.works()
        elif re.search("music", work, re.IGNORECASE):
            self.play_song()
            flag = True
            self.works()

        elif work.lower() in C.LEXIT:
            self.speak("Bye Sir Have a Good Day")
            return
        else:
            print("Sorry Try Again")
            self.works()
