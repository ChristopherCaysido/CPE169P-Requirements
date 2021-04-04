
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera



class MyApp(App):
    def build(self):
        root_widget = BoxLayout(
            orientation = 'vertical',
            # padding = 40,
            # spacing = 10,
            # size_hint=(1,1),
            # pos_hint={'center_x':0.5}
        )
        anothaOne = BoxLayout()
        anothaTwo = BoxLayout()
        texture_size=(None,None)
        btn1 = Button(text="Sample")
        # btn2 = Button(text="Sample")
        # btn3 = Button(text="Sample")
        # btn4 = Button(text="Sample")
        btn5 = Button(text="Sample")
        # btn6 = Button(text="Sample")
        # btn7 = Button(text="Sample")
        # btn8 = Button(text="Sample")
        # cam = Camera(index=0)
        # cam2 = Camera(index=1)
        anothaOne.add_widget(btn1)
        # anothaOne.add_widget(btn2)
        # anothaOne.add_widget(btn3)
        # anothaOne.add_widget(btn4)
        # anothaOne.add_widget(cam)
        anothaTwo.add_widget(btn5)
        # anothaTwo.add_widget(btn6)
        # anothaTwo.add_widget(btn7)
        # anothaTwo.add_widget(btn8)
        # anothaTwo.add_widget(cam2)
        root_widget.add_widget(anothaOne)
        root_widget.add_widget(anothaTwo)
        # Label(text=
        # "[b][color=3D88EE]Mapua University[/color][/b]\n[color=3D88EE]Computer Engineering[/color]",
        # font_size='20sp',
        # halign="right",
        # valign="top",
        # markup=True)
        return root_widget

if __name__ == '__main__':
    MyApp().run()
        