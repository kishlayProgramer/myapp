from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.core.clipboard import Clipboard

class NameCombinationsGenerator(Screen):
    def __init__(self, **kwargs):
        super(NameCombinationsGenerator, self).__init__(**kwargs)

        self.spacing = 10
        self.padding = 10

        self.entry = TextInput(hint_text='Enter your name', multiline=False, font_size=18, size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.generate_button = MDRaisedButton(text='Generate Combinations', on_press=self.on_generate_button_click,
                                              theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=(0, 0.7, 0.9, 1), size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.8})

        self.scroll_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.scroll_view.add_widget(self.scroll_layout)

        # Add the text input and button at the top
        self.add_widget(self.entry)
        self.add_widget(self.generate_button)
        self.add_widget(self.scroll_view)

        # "More Tools" button
        more_tools_button = MDRaisedButton(text='More Tools', on_press=self.on_more_tools_button_click,
                                           theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=(0.5, 0.7, 0.5, 1), size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.add_widget(more_tools_button)

    def generate_combinations(self, name, limit=12):
        length = len(name)
        combinations = []

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "ㅤ" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "ㅤ" * i + name
                combinations.append(combination)
        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "⠋" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "⠋" * i + name
                combinations.append(combination)
        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "⠏" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "⠏" * i + name
                combinations.append(combination)
        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "⠁" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "⠁" * i + name
                combinations.append(combination)
        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "⠍" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "⠍" * i + name
                combinations.append(combination)
        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "⠆" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "⠆" * i + name
                combinations.append(combination)
        if length < limit:
            for i in range(1, limit - length + 1):
                combination = name + "⠊" * i
                combinations.append(combination)

        if length < limit:
            for i in range(1, limit - length + 1):
                combination = "⠊" * i + name
                combinations.append(combination)

        return combinations

    def update_scrollbar_visibility(self):
        if len(self.scroll_layout.children) > 10:
            self.scroll_view.scroll_y = 1
        else:
            self.scroll_view.scroll_y = 0

    def show_error_dialog(self, message):
        error_dialog = MDDialog(
            text=message,
            size_hint=(0.7, 0.3)
        )
        error_dialog.open()

    def on_generate_button_click(self, instance):
        user_name = self.entry.text
  
        if len(user_name) == 12 or len(user_name) > 12:
            self.show_error_dialog("Name must be less than 12 characters.")
        else:
            combinations = self.generate_combinations(user_name)

            self.scroll_layout.clear_widgets()

            for i, combination in enumerate(combinations, start=1):
                copy_button = MDRaisedButton(text=combination, on_press=lambda idx=i, c=combination: self.on_copy_button_click(idx, c),
                                             theme_text_color="Custom", text_color=("black"), md_bg_color=("purple"), size_hint_y=None, height=40,
                                             pos_hint={'center_x': 0.5, 'center_y': None})
                self.scroll_layout.add_widget(copy_button)

            self.update_scrollbar_visibility()

    def on_copy_button_click(self, index, combination):
        try:
            Clipboard.copy(combination)
        except Exception as e:
            print(f"Error copying to clipboard: {e}")

    def on_more_tools_button_click(self, instance):
        # Open the More Tools Screen
        app = MDApp.get_running_app()
        app.root.current = 'more_tools'

class MoreToolsScreen(Screen):
    def __init__(self, **kwargs):
        super(MoreToolsScreen, self).__init__(**kwargs)

        # Add elements for additional tools
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Additional Tools", font_size=18, size_hint_y=None, height=40)
        button1 = Button(text="Tool 1", on_press=self.tool1_function, size_hint_y=None, height=40)
        button2 = Button(text="Tool 2", on_press=self.tool2_function, size_hint_y=None, height=40)
        go_back_button = Button(text="Go Back", on_press=self.go_back, size_hint_y=None, height=40)

        layout.add_widget(label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(go_back_button)

        self.add_widget(layout)

    def tool1_function(self, instance):
        print("Tool 1 function")

    def tool2_function(self, instance):
        print("Tool 2 function")

    def go_back(self, instance):
        app = MDApp.get_running_app()
        app.root.current = 'generator'

class NameCombinationsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"

        # Create a ScreenManager to manage multiple screens
        sm = ScreenManager()

        # Add the NameCombinationsGenerator screen
        generator_screen = NameCombinationsGenerator(name='generator')
        sm.add_widget(generator_screen)

        # Add the MoreToolsScreen
        more_tools_screen = MoreToolsScreen(name='more_tools')
        sm.add_widget(more_tools_screen)

        return sm

if __name__ == '__main__':
    NameCombinationsApp().run()
