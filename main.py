from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import webbrowser
from kivy.metrics import sp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock

class NameCombinationsGenerator(Screen):
    def __init__(self, **kwargs):
        super(NameCombinationsGenerator, self).__init__(**kwargs)
        self.icon = "logo.ico"
        self.root_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)


        # Use RelativeLayout as the root layout
        self.root_layout = RelativeLayout()

        # List of background images
        background_image = Image(source='MyBRO.jpeg', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(background_image)

        self.entry = TextInput(hint_text='Enter your name', multiline=False, font_size=34, size_hint=(None, None), size=(300, 70), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.generate_button = MDRaisedButton(text='Generate Combinations', on_press=self.on_generate_button_click,
                                              theme_text_color="Custom", text_color=("white"), md_bg_color=(0, 0.7, 0.9, 1), size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.8})

        self.scroll_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.scroll_view.add_widget(self.scroll_layout)

        # Add the text input and button at the top
        self.root_layout.add_widget(self.entry)
        self.root_layout.add_widget(self.generate_button)
        self.root_layout.add_widget(self.scroll_view)

        # Set the root_layout as the root widget for the screen
        self.add_widget(self.root_layout)

        # "More Tools" button
        more_tools_button = MDRaisedButton(text='More Tools', on_press=self.on_more_tools_button_click,
                                           theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=(0.5, 0.7, 0.5, 1),
                                           size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.add_widget(more_tools_button)

        # Schedule the background change every 3 seconds
        # Clock.schedule_interval(self.change_background, 3)

    def change_background(self, dt):
        # Update the current image index
        self.current_image_index = (self.current_image_index + 1) % len(self.background_images)
        
        # Change the background image
        self.background_image.source = self.background_images[self.current_image_index]
            
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
                box_layout = BoxLayout(size_hint=(190, None), width=400, height=100, pos_hint={'center_x': 0.5, 'center_y': None})
                
                # Add an Image widget
                image = Image(source='logo.png', size_hint=(None, None), size=(50, 50))
                copy_button = MDRaisedButton(text=combination, on_press=lambda idx=i, c=combination: self.on_copy_button_click(idx, c),
                                            theme_text_color="Custom", text_color=("white"), md_bg_color=("black"), size_hint=(90, None))
                
                box_layout.add_widget(image)
                box_layout.add_widget(copy_button)
                self.scroll_layout.add_widget(box_layout)

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
        label = Label(text="Comming Soon", font_size=49, size_hint_y=None, height=40)


        about_developer_button = MDRaisedButton(text="See More", on_press=self.open_new_page,
                                        theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=(1, 0.7, 0.2, 1),
                                        size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.5})


        go_back_button = MDIconButton(icon="backarow.png", on_press=self.go_back,
                               theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=("black"),
                               pos_hint={'center_x': 0.15, 'center_y': 0.1})

        layout.add_widget(label)
        # layout.add_widget(about_developer_button)
        layout.add_widget(about_developer_button)
        layout.add_widget(go_back_button)

        # Set the background color using the canvas
        with layout.canvas.before:
            Color(0, 0, 0, 1)  # Set the color (black)
            self.background_rect = Rectangle(pos=layout.pos, size=layout.size)

        # Set the logo as the background
        image = Image(source='Backofmore.png', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(image)

        self.add_widget(layout)

        layout.bind(pos=self.update_rect, size=self.update_rect)

    def about_developer_function(self, instance):
        # Define the action for the "About Great Developer" button
        print("About Great Developer Button Clicked")

    def open_new_page(self, instance):
        # Open the New Page Screen
        app = MDApp.get_running_app()
        app.root.current = 'new_page'

    def go_back(self, instance):
        # Define the action for the "Go Back" button
        app = MDApp.get_running_app()
        app.root.current = 'generator'

    def update_rect(self, instance, value):
        self.background_rect.pos = instance.pos
        self.background_rect.size = instance.size
class TableScreen(Screen):
    def __init__(self, **kwargs):
        super(TableScreen, self).__init__(**kwargs)

        # Create a GridLayout for the table
        table_layout = GridLayout(cols=2, spacing=10, size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Add labels and values to the table
        labels_and_values = {
            "Name:": "Kishlay",
            "Age:": "13",
            "Website:": "firewa.com",
            "Favourite:": "Python",
            " ": "YouTube"
        }

        for label, value in labels_and_values.items():
            label_widget = Label(text=label, font_size=sp(20), halign='left', valign='middle')

            # Check if the label is "YouTube"
            if label.lower() == " ":
                button = MDRaisedButton(
                    text=value,
                    on_press=self.open_youtube_page,
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    md_bg_color=(1, 0.7, 0.2, 1),
                    size_hint=(None, None),
                    size=(300, 60),
                    pos_hint={'center_x': 0.5, 'center_y': 0.3},
                )
                table_layout.add_widget(label_widget)
                table_layout.add_widget(button)
            else:
                value_widget = Label(text=value, font_size=sp(20), halign='left', valign='middle')
                table_layout.add_widget(label_widget)
                table_layout.add_widget(value_widget)


        # Add the table layout to the screen
        self.add_widget(table_layout)

        # Add a "Go Back" button
        go_back_button = MDIconButton(icon="backarow.png", on_press=self.go_back,
                               theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=("black"),
                               pos_hint={'center_x': 0.15, 'center_y': 0.1})
        self.add_widget(go_back_button)

    def open_youtube_page(self, instance):
        # Open the YouTube page in a web browser
        webbrowser.open("https://www.youtube.com/@Fire_Wa")

    def go_back(self, instance):
        # Go back to the New Page Screen
        app = MDApp.get_running_app()
        app.root.current = 'new_page'

class NewPageScreen(Screen):
    def __init__(self, **kwargs):
        super(NewPageScreen, self).__init__(**kwargs)

        # Use a BoxLayout as the root layout
        self.root_layout = BoxLayout(orientation='vertical')

        # Add an icon button for "Go Back"
        go_back_button = MDIconButton(icon="backarow.png", on_press=self.go_back,
                                      theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=("black"),
                                      pos_hint={'center_x': 0.15, 'center_y': 0.1})
        self.root_layout.add_widget(go_back_button)

        show_table_button = MDRaisedButton(text="About Me", on_press=self.show_table,
                                           theme_text_color="Custom", text_color=(1, 1, 1, 1), md_bg_color=(1, 0.7, 0.2, 1),
                                           size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.root_layout.add_widget(show_table_button)

        # Create a RelativeLayout for the layout
        self.relative_layout = RelativeLayout()

        # Add a label with some text to the layout
        responsive_label = Label(text="UnderRated God Players", font_size='20sp', color=(1, 1, 1, 1),  pos_hint={'center_x': 0.5, 'center_y': 0.9})
        responsive_label2 = Label(text="COMMING SOON", font_size='20sp', color=(1, 1, 1, 1),  pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.relative_layout.add_widget(responsive_label)
        self.relative_layout.add_widget(responsive_label2)

        with self.relative_layout.canvas.before:
            Color(0, 0, 0, 0)  # Set the color (black)
            self.background_rect = Rectangle(pos=self.relative_layout.pos, size=self.relative_layout.size)

        # Set the logo as the background
        image = Image(source='bihari gamer.jpg', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.relative_layout.add_widget(image)

        self.root_layout.add_widget(self.relative_layout)

        self.relative_layout.bind(pos=self.update_rect, size=self.update_rect)
        self.add_widget(self.root_layout)

    def go_back(self, instance):
        # Go back to the More Tools Screen
        app = MDApp.get_running_app()
        app.root.current = 'more_tools'

    def show_table(self, instance):
        # Open the Table Screen
        app = MDApp.get_running_app()
        app.root.current = 'table_screen'

    def update_rect(self, instance, value):
        # Update the background rectangle position and size
        self.background_rect.pos = instance.pos
        self.background_rect.size = instance.size

class NameCombinationsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"
        self.icon = "logo.png"

        # Create a ScreenManager to manage multiple screens
        sm = ScreenManager()

        # Add the NameCombinationsGenerator screen
        generator_screen = NameCombinationsGenerator(name='generator')
        sm.add_widget(generator_screen)

        # Add the MoreToolsScreen
        more_tools_screen = MoreToolsScreen(name='more_tools')
        sm.add_widget(more_tools_screen)

        # Add the NewPageScreen
        table_screen = TableScreen(name='table_screen')
        sm.add_widget(table_screen)
        new_page_screen = NewPageScreen(name='new_page')
        sm.add_widget(new_page_screen)

        return sm

if __name__ == '__main__':
    NameCombinationsApp().run()
