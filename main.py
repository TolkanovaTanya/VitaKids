from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from random import choice


Window.clearcolor = 1, 1, 1, 1


class RecipeWindow(Screen):
    def __init__(self, **kwargs):
        super(RecipeWindow, self).__init__(**kwargs)
        self.images = ['RecipeWindow/img/1.jpeg', 'RecipeWindow/img/2.jpg', 'RecipeWindow/img/3.jpeg',
                       'RecipeWindow/img/4.jpeg', 'RecipeWindow/img/5.jpeg',
                       'RecipeWindow/img/6.jpg', 'RecipeWindow/img/7.jpg', 'RecipeWindow/img/8.jpg',
                       'RecipeWindow/img/9.jpeg', 'RecipeWindow/img/10.jpg']
        self.text_files = ['RecipeWindow/text/1.txt', 'RecipeWindow/text/2.txt', 'RecipeWindow/text/3.txt',
                           'RecipeWindow/text/4.txt', 'RecipeWindow/text/5.txt',
                           'RecipeWindow/text/6.txt', 'RecipeWindow/text/7.txt', 'RecipeWindow/text/8.txt',
                           'RecipeWindow/text/9.txt', 'RecipeWindow/text/10.txt']
        self.index = 0

        self.layout = BoxLayout(orientation='vertical')

        self.display = Image(source=self.images[self.index])
        self.layout.add_widget(self.display)

        inner_layout = BoxLayout(orientation='horizontal')

        self.label = Label(text=self.load_text(self.text_files[self.index]), color=(0, 0, 0, 1))
        inner_layout.add_widget(self.label)

        self.button = Button(text='>', on_press=self.switch, size_hint=(0.1, 0.1),
                             pos_hint={'right': 0.95, 'y': 0.05})
        inner_layout.add_widget(self.button)

        self.layout.add_widget(inner_layout)

        back_button = Button(text='Назад', size_hint_y=None, height=40, font_size='20sp')
        back_button.bind(on_release=self.switch_to_main)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def switch(self, instance):
        self.index = (self.index + 1) % 10
        self.display.source = self.images[self.index]
        self.label.text = self.load_text(self.text_files[self.index])

    def load_text(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text
        except FileNotFoundError:
            return "Нет файла"

    def switch_to_main(self, instance):
        self.manager.current = 'main_window'
        self.manager.transition.direction = 'right'


class ImageButton(ButtonBehavior, Image):
    pass


class HistoryWindow(Screen):
    def __init__(self, **kwargs):
        super(HistoryWindow, self).__init__(**kwargs)
        self.current_sound = None

    def play_sound(self, sound_path):
        if self.current_sound:
            self.current_sound.stop()

        sound = SoundLoader.load(sound_path)
        if sound:
            self.current_sound = sound
            sound.bind(on_stop=lambda s: self.stop_sound())
            sound.play()

    def stop_sound(self):
        if self.current_sound:
            self.current_sound.unbind(on_stop=self.stop_sound)
            self.current_sound = None

    def audio_vitamin_C(self):
        self.play_sound('HistoryWindow/wav/1.wav')

    def audio_vitamin_A(self):
        self.play_sound('HistoryWindow/wav/2.wav')

    def audio_vitamin_B12(self):
        self.play_sound('HistoryWindow/wav/3.wav')

    def audio_vitamin_D3(self):
        self.play_sound('HistoryWindow/wav/4.wav')

    def audio_vitamin_E(self):
        self.play_sound('HistoryWindow/wav/5.wav')

    def audio_vitamin_k(self):
        self.play_sound('HistoryWindow/wav/6.wav')

    def audio_vitamin_b6(self):
        self.play_sound('HistoryWindow/wav/7.wav')

    def audio_vitamin_pp(self):
        self.play_sound('HistoryWindow/wav/8.wav')


class TheoryWindow(Screen):
    def __init__(self, **kwargs):
        super(TheoryWindow, self).__init__(**kwargs)
        self.current_sound = None

    def play_sound(self, sound_path):
        if self.current_sound:
            self.current_sound.stop()

        sound = SoundLoader.load(sound_path)
        if sound:
            self.current_sound = sound
            sound.bind(on_stop=lambda s: self.stop_sound())
            sound.play()

    def stop_sound(self):
        if self.current_sound:
            self.current_sound.unbind(on_stop=self.stop_sound)
            self.current_sound = None

    def audio_vitamin_C(self):
        self.play_sound('TheoryWindow/wav/1.wav')

    def audio_vitamin_A(self):
        self.play_sound('TheoryWindow/wav/2.wav')

    def audio_vitamin_B12(self):
        self.play_sound('TheoryWindow/wav/3.wav')

    def audio_vitamin_D3(self):
        self.play_sound('TheoryWindow/wav/4.wav')

    def audio_vitamin_E(self):
        self.play_sound('TheoryWindow/wav/5.wav')

    def audio_vitamin_k(self):
        self.play_sound('TheoryWindow/wav/6.wav')

    def audio_vitamin_b6(self):
        self.play_sound('TheoryWindow/wav/7.wav')

    def audio_vitamin_pp(self):
        self.play_sound('TheoryWindow/wav/8.wav')

class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class PaintWindow(Screen):
    pass


class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.available_colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 0)]
        self.current_color = choice(self.available_colors)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.current_color)
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()

    def change_color(self):
        self.current_color = choice(self.available_colors)


kv = Builder.load_file("design.kv")


class BabiesApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    BabiesApp().run()
