from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from fetchdata import DataAccess
import sqlite3

class ExecuteSqlForm(BoxLayout):
    query_input = ObjectProperty()
    
    def execute_sql(self):
        da = DataAccess()
        try:
            result = da.executeQuery(self.query_input.text)
            print("Result:\n'{}'".format(result))
        except sqlite3.OperationalError as error:
            print("There is an error in your statement please try again")
            popup = Popup(title='Test popup',
            content=Label(text='Hello world'),
            size_hint=(None, None), size=(400, 400))
            popup.open()

class ChinookApp(App):
    def build(self):    
        return ExecuteSqlForm()

if __name__ == '__main__':
	ChinookApp().run()
