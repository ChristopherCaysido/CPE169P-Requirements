#main.py
import json
import os
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget

Window.size = (500,350)


class JSONStore(BoxLayout):
    json_file = ''
    def createJSON(self):
        dict_input = self.ids.dict_input.text
        json_file = json.dumps(dict_input)
        json_text = json.loads(json_file)
        self.ids.data_ouput.text = json_text
        return json_file
        
        


class todo3App(App):
    jsonMethod = JSONStore()
    def build(self):
        jsonStore = JSONStore()
        return jsonStore

if __name__=='__main__':
    todo3App().run()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict)
