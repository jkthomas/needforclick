from kivy.app import App
from kivy.lang import Builder
import Screen

Builder.load_file('needforclick.kv')


class NeedForClickApp(App):

    def build(self):
        return Screen.MainScreen()


if __name__ == '__main__':
    NeedForClickApp().run()
