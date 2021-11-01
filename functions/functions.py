import os
import time
import webbrowser

# from functions.basic import Base
from functions.constants import Constant as cs
from playsound import playsound
from selenium import webdriver


class Functions():
    def __init__(self):
        pass

    def start(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_whatsapp(self, URL=cs.WHATSAPP):
        print("opening Whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
        time.sleep(30)
        # Closes After 30 Seconds
        os.system("TASKKILL /F /IM firefox.exe")

    def open_file_explorer(self):
        print("Open File Explorer")
        os.system("explorer")

    def open_browser(self, URL=cs.URL):
        self.driver.get(URL)

    def play_song(self):
        print("Playing Music")
        os.chdir("songs/")
        songs = os.listdir()
        for song in songs:
            playsound(song)
