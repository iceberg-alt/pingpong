from kivy.app import App
from kivy.uix.widget import Widget


class pingponggame(Widget):
    pass

class pingpongapp(App):
    def build(self):
        
        return pingponggame()
    
if __name__ == '__main__':
    pingpongapp().run()
