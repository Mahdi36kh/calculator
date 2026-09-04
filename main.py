from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.display = TextInput(
            text='0',
            multiline=False,
            readonly=True,
            halign='right',
            font_size=45,
            size_hint=(1, 0.25),
            background_color=(0.95, 0.95, 0.95, 1)
        )
        self.main_layout.add_widget(self.display)
        buttons_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', 'DEL', '='
        ]
        for text in buttons:
            btn = Button(
                text=text,
                font_size=28,
                background_color=(0.2, 0.6, 0.9, 1) if text in ['=', 'C', 'DEL'] else (0.3, 0.3, 0.3, 1)
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
        self.main_layout.add_widget(buttons_layout)
        return self.main_layout

    def on_button_press(self, instance):
        btn_text = instance.text
        current = self.display.text
        if btn_text == 'C':
            self.display.text = '0'
        elif btn_text == 'DEL':
            if len(current) > 1 and current != 'Error':
                self.display.text = current[:-1]
            else:
                self.display.text = '0'
        elif btn_text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = 'Error'
        else:
            if current in ['0', 'Error']:
                self.display.text = btn_text
            else:
                self.display.text += btn_text

if __name__ == '__main__':
    CalculatorApp().run()
