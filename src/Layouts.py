from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
import random
import gc


class TimeLabel(Label):
    def __init__(self, text):
        super(TimeLabel, self).__init__()
        self.text = str(text)


class NumberButton(Button):
    def __init__(self, id, text):
        super(NumberButton, self).__init__()
        self.id = str(id)
        self.text = str(text)


class Break(BoxLayout):
    time_label = TimeLabel("Time: 0.0 s")

    def __init__(self):
        super(Break, self).__init__()
        self.add_widget(self.time_label)


class SettingsLayout(BoxLayout):
    def __init__(self):
        super(SettingsLayout, self).__init__()
        refresh_button = Button(text="Reset")
        refresh_button.bind(on_release=self.restart_game)
        self.add_widget(refresh_button)
        options_button = Button(text="Increment Grid Size")
        options_button.bind(on_release=self.change_grid_size)
        self.add_widget(options_button)

    def restart_game(self, instance):
        self.parent.restart_game()

    def change_grid_size(self, instance):
        self.parent.change_grid_size()


class GameBoardLayout(GridLayout):
    grid_size = 3
    numbers = []

    def __init__(self, grid_size):
        super(GameBoardLayout, self).__init__()
        self.grid_size = grid_size
        self.initialize_numbers_array()
        self.initialize_game_board()

    def initialize_numbers_array(self):
        for i in range(0, self.grid_size * self.grid_size):
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
        if int(instance.text) == self.numbers.__len__():
            self.game_ended()
        else:
            self.numbers[int(instance.id) + 1].bind(on_press=self.button_hit)

    def refresh_buttons(self):
        for button in self.children:
            button.disabled = False

    def game_ended(self):
        self.numbers = []
        self.clear_widgets()
        gc.collect()
        self.initialize_numbers_array()
        self.initialize_game_board()

    def change_grid_size(self):
        if self.grid_size == 5:
            self.grid_size = 2
        else:
            self.grid_size += 1
        self.cols = self.grid_size
        self.game_ended()


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

    def restart_game(self):
        self.game_board_layout.refresh_buttons()

    def change_grid_size(self):
        self.game_board_layout.change_grid_size()