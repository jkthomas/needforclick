from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
import random


class NumberButton(Button):
    def __init__(self, text):
        super(NumberButton, self).__init__()
        self.text = str(text)


class Break(BoxLayout):
    def __init__(self):
        super(Break, self).__init__()


class SettingsLayout(BoxLayout):
    def __init__(self):
        super(SettingsLayout, self).__init__()
        self.add_widget(Button(text="Reset"))
        self.add_widget(Button(text="Options"))


class GameBoardLayout(GridLayout):
    numbers = []

    def __init__(self, grid_size):
        super(GameBoardLayout, self).__init__()
        self.numbers = self.initialize_numbers_array(grid_size)
        self.initialize_game_board()

    def initialize_numbers_array(self, grid_size):
        temp_numbers = list(range(1, grid_size * grid_size + 1))
        random.shuffle(temp_numbers)
        return temp_numbers

    def initialize_game_board(self):
        for number in self.numbers:
            self.add_widget(
                NumberButton(
                    text=number
                )
            )


class ScreenLayout(BoxLayout):
    settings_layout = ObjectProperty()
    break_point = ObjectProperty()
    game_board_layout = ObjectProperty()

    def __init__(self, settings_layout, game_board_layout):
        super(ScreenLayout, self).__init__()
        self.settings_layout = settings_layout
        self.break_point = Break()
        self.game_board_layout = game_board_layout
        self.add_widget(self.settings_layout)
        self.add_widget(self.break_point)
        self.add_widget(self.game_board_layout)
