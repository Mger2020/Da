from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.output_label = Label(text="[color=00ff00]напиши своё имя[/color]", markup=True)
        layout.add_widget(self.output_label)

        self.input_field = TextInput(multiline=False)
        layout.add_widget(self.input_field)

        
        button = Button(text="Ввод")
        button.bind(on_press=self.process_input)
        layout.add_widget(button)

        return layout

    def process_input(self, instance):
        user_input = self.input_field.text

        self.output_label.text = user_input
        
        if user_input.isalpha():
            self.output_label.text = f"[color=00ff00]привет {user_input}![/color]" 
            self.input_field.text = ""
        else:
            self.output_label.text = "[color=ff0000]имя пиши, а не белеберду всякую[/color]"         
            self.input_field.text = ""

if __name__ == '__main__':
    TextInputApp().run()
