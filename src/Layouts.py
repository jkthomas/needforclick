from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
import random


class NumberButton(Button):
    def __init__(self, id, text):
        super(NumberButton, self).__init__()
        self.id = str(id)
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
        self.initialize_numbers_array(grid_size)
        self.initialize_game_board()

    def initialize_numbers_array(self, grid_size):
        for i in range(0, grid_size * grid_size):
            number_button = NumberButton(
                id=i,
                text=(i+1)
            )
            self.numbers.append(number_button)

        self.numbers[0].bind(on_press=self.button_hit)

    def initialize_game_board(self):
        shuffled_buttons = random.sample(self.numbers, self.numbers.__len__())
        for button in shuffled_buttons:
            self.add_widget(button)

    def button_hit(self, instance):
        instance.disabled = True
        if (int(instance.id) + 1) == self.numbers.__len__():
            for button in self.children:
                button.disabled = False
        else:
            self.numbers[int(instance.id) + 1].bind(on_press=self.button_hit)


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
