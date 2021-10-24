import calendar
import datetime
import re
from functions.browser import Browser
import pyttsx3
import speech_recognition as SR


class Base:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def greeting(self):
        self.speak("Hello sir Hope Doing Great")
        self.speak("Authenticate Yourself")
        self.authentication()

    def authentication(self):
        data = self.voice_conv()
        if re.search("567", data, re.IGNORECASE):

            self.speak("Welcome Namilakonda Rahul sir")
            self.gretting_time()
        elif re.search("420", data, re.IGNORECASE):
            self.speak("Welcome Sharath Sir")
            self.gretting_time()
        else:
            self.speak("Sorry you are not correct one")

    def speak(self, audio):
        print(audio)
        self.engine.say(audio)
        self.engine.runAndWait()

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
        work=self.voice_conv()
        self.works(work)