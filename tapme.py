import time

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.progressbar import ProgressBar

from kivy.uix.button import Button

from kivy.uix.popup import Popup

from kivy.uix.label import Label

class TapMeApp(App):

    def build(self):

        # Hlavné rozloženie

        layout = BoxLayout(orientation='vertical')

        

        # Načítavací pás

        progress_bar = ProgressBar(max=100, size_hint=(1, 0.1))

        layout.add_widget(progress_bar)

        

        # Funkcia na animáciu načítavacieho pásu

        def animate_loading_bar():

            for i in range(101):

                progress_bar.value = i

                time.sleep(0.03)  # Simulácia načítania

            layout.remove_widget(progress_bar)

            show_button()

        

        # Spustenie animácie načítavacieho pásu

        animate_loading_bar()

        

        # Tlačidlo

        def show_button():

            button = Button(text='Klikni ma!', size_hint=(None, None), size=(200, 100),

                            background_color=(0, 1, 0, 1))

            button.bind(on_press=show_popup)

            layout.add_widget(button)

        

        # Popup s počtom kliknutí a časom

        def show_popup(instance):

            popup = Popup(title='Výsledok',

                          content=Label(text=f'Počet kliknutí: {click_count}\nČas: {click_time}'),

                          size_hint=(0.6, 0.4))

            popup.open()

        

        # Premenné pre počet kliknutí a čas

        click_count = 0

        click_time = ''

        

        # Zaznamenávanie kliknutí

        def count_clicks(instance):

            nonlocal click_count, click_time

            click_count += 1

            click_time = time.strftime('%H:%M:%S')

        

        # Pridanie zaznamenávania kliknutí

        self.button = layout.children[1]

        self.button.bind(on_press=count_clicks)

        

        return layout

if __name__ == '__main__':

    TapMeApp().run()

