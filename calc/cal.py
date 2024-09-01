import kivy
from kivy import*
from kivy.app import App
from kivy.core import text
from kivy.core import window
from kivy.uix import textinput
from kivy.uix import label
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import  Window
from kivy.uix.image import Image 
from kivy.properties import ObjectProperty
from re import MULTILINE
Window.size=(320,510)
Builder.load_file("C:/Users/ptof/Desktop/html/python/kivy/cal.kv")
class cal(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def clear(self):
        self.ids.cal_input.text="0"

    def click_buttun(self,button):
        ci=self.ids.cal_input.text
        if ci=="0":
            self.ids.cal_input.text=" "
            self.ids.cal_input.text=f"{button}"
        else:
            self.ids.cal_input.text=f"{ci}{button}"

    def add(self):
        global n1
        global ci
        global mass
        ci=self.ids.cal_input.text
        n1=float(ci)
        self.ids.cal_input.text=" "
        mass="add"


    def min(self):
        global n1
        global ci
        global mass
        ci=self.ids.cal_input.text
        n1=float(ci)
        self.ids.cal_input.text=" "
        mass="min"

    def div(self):
        global n1
        global ci
        global mass
        ci=self.ids.cal_input.text
        n1=float(ci)
        self.ids.cal_input.text=" "
        mass="div"

    def multi(self):
        global n1
        global ci
        global mass
        ci=self.ids.cal_input.text
        n1=float(ci)
        self.ids.cal_input.text=" "
        mass="mul"

    def pow(self):
        global n1
        global ci
        global mass
        ci=self.ids.cal_input.text
        n1=float(ci)
        self.ids.cal_input.text=" "
        mass="pow"

    def det(self):
        global n1
        global ci
        global mass
        ci=self.ids.cal_input.text
        n1=float(ci)
        self.ids.cal_input.text=f"{-n1}"
        mass="det"

    def dot(self):
        global n1
        global ci
        global mass
        global f
        ci=self.ids.cal_input.text
        n1=ci
        if "." in n1:pass
        else:
                f=self.ids.cal_input.text=f"{n1}."
        mass="dot"

    def de(self):
        global n1
        global ci
        ci=self.ids.cal_input.text
        n1=ci
        self.ids.cal_input.text=f"{n1[ :-1]}"

    def eq(self):
        qn=self.ids.cal_input.text
        q=int(qn)
        if mass=="add":e=n1+q
        elif mass=="min":e=n1-q
        elif mass=="div":e=n1/q
        elif mass=="mul":e=n1*q
        elif mass=="pow":e=n1**q
        elif mass=="error":self.ids.cal_input.text="Error"
        else:self.ids.cal_input.text="Error"
        s=f"{e}"
        if s[-2:]==".0":v=s[:-2]
        else:v=s
        self.ids.cal_input.text=f"{v}"

    try:eq() 
    except:
        mass="error"
        print("error")

class calculator(App):
    def build(self):
        Window.clearcolor=(237/255,235/255,228/255,1)
        return cal()
if __name__=='__main__':calculator().run()
# (how to make Email sender by python,كيف تجعل الكمند لين يدعم العربية,كيف تجعل فيجول ستوديو  كود يدعم العربي)
