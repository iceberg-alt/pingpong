from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label

class Application(App):
    def build(self):
        return Label(text='go short')
    
    def btn(self):
        btn = Button.size(21,12)
        tab = Button.text = ('212')
        return Button
        

if __name__ == '__main__':
    Application().run()
    
print(Application)

