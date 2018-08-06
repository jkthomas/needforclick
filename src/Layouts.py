from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button


class SettingsLayout(BoxLayout):
    def __init__(self):
        super(BoxLayout, self).__init__()


class GameBoardLayout(GridLayout):
    def __init__(self):
        super(GridLayout, self).__init__()
        self.initialize_game_board(3)

    def initialize_game_board(self, grid_size):
        for column in range(grid_size):
            for position in range(grid_size):
                self.add_widget(
                    Button(
                        text=str(position*column)
                    )
                )


class ScreenLayout(BoxLayout):
    settings_layout = ObjectProperty()
    game_board_layout = ObjectProperty()

    def __init__(self):
        super(BoxLayout, self).__init__()
        # self.settings_layout = settings_layout
        # self.game_board_layout = game_board_layout
        # self.add_widget(self.settings_layout)
        # self.add_widget(self.game_board_layout)
