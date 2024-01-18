from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class CustomScrollBar(BoxLayout):
    pass

class NameCombinationsGenerator(RelativeLayout):
    def __init__(self, **kwargs):
        super(NameCombinationsGenerator, self).__init__(**kwargs)

        # Add background image
        background_image = Image(source='background_image.jpg', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(background_image)

        self.spacing = 10
        self.padding = 10

        self.entry = TextInput(hint_text='Enter your name', multiline=False, font_size=18, size_hint=(1, None), height=40, pos_hint={'top': 1})
        self.generate_button = Button(text='Generate Combinations', on_press=self.on_generate_button_click,
                                      background_color=(0, 0.7, 0.9, 1), font_size=18, size_hint=(1, None), height=60, pos_hint={'top': 0.85})

        self.scroll_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.7), pos_hint={'top': 0.8})
        self.scroll_view.add_widget(self.scroll_layout)

        # Custom scroll bar
        custom_scroll_bar = CustomScrollBar()
        self.add_widget(custom_scroll_bar)

        # Add the text input and button at the top
        self.add_widget(self.entry)
        self.add_widget(self.generate_button)
        self.add_widget(self.scroll_view)

        # "More Tools" button
        more_tools_button = Button(text='More Tools', on_press=self.on_more_tools_button_click,
                                   background_color=(0.5, 0.7, 0.5, 1), font_size=18, size_hint=(1, None), height=60, pos_hint={'top': 0.1})
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
        # Show scrollbar after 10 buttons
        if len(self.scroll_layout.children) > 10:
            self.scroll_view.scroll_y = 1
        else:
            self.scroll_view.scroll_y = 0

    def show_error_dialog(self, message):
        error_label = Label(text=message, font_size=18)
        error_dialog = ModalView(size_hint=(None, None), size=(400, 200))
        error_dialog.add_widget(error_label)
        error_dialog.open()

    def on_generate_button_click(self, instance):
        user_name = self.entry.text
  
        if len(user_name) == 12:
            self.show_error_dialog("Name must be at least less than 12 characters.")
        elif len(user_name) > 12:
            self.show_error_dialog("Name must be at least less than 12 characters.")
        else:
            combinations = self.generate_combinations(user_name)

            # Clear previous content
            self.scroll_layout.clear_widgets()

            for i, combination in enumerate(combinations, start=1):
                copy_button = Button(text=combination, on_press=lambda idx=i, c=combination: self.on_copy_button_click(idx, c),
                                     size_hint_y=None, height=40, background_color=(0.9, 0.5, 0, 1))  # Adjust the color as needed
                self.scroll_layout.add_widget(copy_button)

            self.update_scrollbar_visibility()

    def on_copy_button_click(self, index, combination):
        try:
            # Extract text from the clicked copy button
            text_to_copy = combination
            Clipboard.copy(text_to_copy)
        except Exception as e:
            print(f"Error copying to clipboard: {e}")

    def on_more_tools_button_click(self, instance):
        # Add functionality for the "More Tools" button
        print("More Tools button clicked")

class NameCombinationsApp(App):
    def build(self):
        # Window.size = (350, 600)
        return NameCombinationsGenerator()

if __name__ == '__main__':
    NameCombinationsApp().run()
