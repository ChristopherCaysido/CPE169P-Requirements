from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App



class MainWidget(Widget):
    pass

class WidgetPropApp(App):
    def build(self):
        return MainWidget()

if __name__=='__main__':
    WidgetPropApp().run()