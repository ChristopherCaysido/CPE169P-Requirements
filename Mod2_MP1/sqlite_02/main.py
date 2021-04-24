from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from fetchdata import DataAccess

class ExecuteSqlForm(BoxLayout):
    query_input = ObjectProperty()
    
    def execute_sql(self):
        da = DataAccess()
        print(self.query_input.text)
        result = da.executeQuery(self.query_input.text)
        print("""Result:\n'{}'""".format(result))    


class ChinookApp(App):
    def build(self):    
        return ExecuteSqlForm()

if __name__ == '__main__':
	ChinookApp().run()
