import pywinauto
from pywinauto import Application, Desktop
from time import sleep
import warnings
import pyautogui as pya
import os
import pyperclip

warnings.simplefilter("ignore", category=UserWarning)

class GuiDoesNotExists(Exception):
    def __str__(self):
        return "Gui deosn't exists."

class Client():
    
    def foreGroundDiscord(self): # it will make discord window top of all other windows

        windows = Desktop(backend="uia").windows()

        title = ""
        for w in windows:
            if "Discord" in str(w.window_text):
                title = str(w.window_text).split("'")[1]
                break

        app = None
        try:
            app = Application().connect(title_re=title)

        except (__import__("re").error, pywinauto.findwindows.ElementAmbiguousError):
            raise GuiDoesNotExists
            return

        hwin = app.top_window()

        hwin.set_focus()

        sleep(0.9)


    def getImgPath(self, name):
        return os.path.join( os.path.join(os.path.dirname(__file__), "gui"), name )

    def getLocation(self, name, confidence=None):
        if confidence:
            return pya.locateCenterOnScreen(self.getImgPath(name), confidence=confidence)
        else:
            return pya.locateCenterOnScreen(self.getImgPath(name))

    def click(self, name, clicks=1, confidence=None, button="left"):
        before = pya.position()

        if confidence:
            c = self.getLocation(name, confidence=confidence)
        else:
            c = self.getLocation(name)

        if not c:
            raise GuiDoesNotExists
            return

        pya.click(c, clicks=clicks, button=button)
        pya.moveTo(before)

    def clickTextBox(self):
        before = pya.position()
        tb = self.getLocation("textbox.PNG", confidence=0.5)

        if not tb:
            raise GuiDoesNotExists
            return

        pya.click(tb)
        pya.moveTo(before)

    def type(self, text, interval=None):
        if interval:
            self.clickTextBox()

            for t in text:
                pyperclip.copy(t)

                sleep(interval)

                pya.hotkey("ctrl", "v")

        else:

            self.clickTextBox()

            for t in text:
                pyperclip.copy(t)

                pya.hotkey("ctrl", "v")


    def send(self, text, interval=None):
        if interval:
            self.clickTextBox()

            for t in text:
                pyperclip.copy(t)

                sleep(interval)

                pya.hotkey("ctrl", "v")

            pya.press("enter")

        else:
        
            self.clickTextBox()

            pyperclip.copy(text)

            pya.hotkey("ctrl", "v")

            pya.press("enter")

    def quit(self):
        self.click("quit.PNG")

    def minimize(self):
        self.click("minimize.PNG")

    def maximize(self):
        self.click("maximize.PNG")

    def home(self):
        self.click("home.PNG", confidence=0.7)

    def mute(self):
        self.click("unmuted.PNG")

    def unmute(self):
        self.click("muted.PNG")

    def deaf(self):
        self.click("undeaf.PNG")

    def undeaf(self):
        self.click("deaf.PNG")

    def chill(self):
        self.click("chill.PNG", confidence=0.7)

    def joinLive(self):
        self.click("live.PNG", 2, 0.9)

    def acceptNitro(self):
        self.click("accept.PNG")

        sleep(0.1)
        
        self.click("iaccept.PNG")

    def disconnect(self):
        self.click("disconnect.PNG")