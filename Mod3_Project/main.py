import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera



class MyApp(App):
    root_widget = BoxLayout()
    base_cam = Camera(index=1, resolution=(640,360), play=True)
    root_widget.add_widget(base_cam())
    return root_widget()



if __name__=='__main__':
    MyApp().run()