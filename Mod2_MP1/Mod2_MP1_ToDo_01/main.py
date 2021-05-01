from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from fetchdata import DataAccess
import sqlite3

class ExecuteSqlForm(BoxLayout):
    query_input = ObjectProperty()
    def popup_callback(self):
        popup.close()
    def execute_sql(self):
        da = DataAccess()
        try:
            result = da.executeQuery(self.query_input.text)
            print("Result:\n'{}'".format(result))
        except sqlite3.OperationalError as error:
            print("There is an error in your statement please try again")
            popup = Popup(title='Sqlite Parsing Error',
            content=Label(text='Please edit the entered text'),
            size_hint=(None, None), size=(400, 400))
            popup.open()

class ChinookApp(App):
    def build(self):    
        return ExecuteSqlForm()

if __name__ == '__main__':
	ChinookApp().run()
