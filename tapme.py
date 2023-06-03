import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ClickCounterApp(App):
    def __init__(self, **kwargs):
        super(ClickCounterApp, self).__init__(**kwargs)
        self.click_count = 0

    def on_button_click(self, instance):
        self.click_count += 1
        instance.text = f"Clicked: {self.click_count} times"

    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Click me!')
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    ClickCounterApp().run()
