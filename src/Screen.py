from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import Layouts

# Global variable only for testing purposes, will be removed in release version
grid_size = 3


class MainScreen(Screen):
    main_layout = ObjectProperty()
    settings_layout = ObjectProperty()
    game_board_layout = ObjectProperty()

    def __init__(self):
        Screen.__init__(self)
        self.initialize_layout()

    def initialize_layout(self):
        self.settings_layout = Layouts.SettingsLayout()
        self.game_board_layout = Layouts.GameBoardLayout(grid_size)
        self.main_layout = Layouts.ScreenLayout(self.settings_layout, self.game_board_layout)

        self.add_widget(self.main_layout)
