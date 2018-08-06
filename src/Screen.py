from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import Layouts


class MainScreen(Screen):
    main_layout = ObjectProperty()
    settings_layout = ObjectProperty()
    game_board_layout = ObjectProperty()

    def __init__(self):
        Screen.__init__(self)
        self.initialize_layout()

    def initialize_layout(self):
        self.settings_layout = Layouts.SettingsLayout()
        self.game_board_layout = Layouts.GameBoardLayout()

        # self.main_layout = Layouts.ScreenLayout()
        # self.main_layout.add_widget(self.settings_layout)
        # self.main_layout.add_widget(self.game_board_layout)
        self.add_widget(self.settings_layout)
