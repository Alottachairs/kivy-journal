'''
Python project for journal application
By: David Elliott

Project started = 11/17/22
Alpha version completed = ""


Goal: Use Kivy to create a journal GUI for text entries and saves.
'''
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from functools import partial
import time



class JournalApp(App):

    
    def build(self):

        title = Label(text="Journal" '\n' +time.ctime(),
                    bold=True,
                    outline_color=(0.2,0.4,1,1),
                    outline_width=5,
                    size_hint=(1,.2))

        self.text_input = TextInput(text="What's on your mind?",
                    background_color=(0.7,1,1,1))

        submit_btn = Button(text="Submit!",
                    size_hint=(1,.2),
                    outline_color=(.8,0.3,0,1),
                    outline_width=5) 
        submit_btn.bind(on_press=partial(self.submit_entry))
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(title)
        layout.add_widget(self.text_input)
        layout.add_widget(submit_btn)
        Window.size = (300,600)

        return layout 

    def submit_entry(self,instance):
        #print(self.text_input.text)
        with open('entrys/journal.txt', 'a') as f:
            f.write(time.ctime() + '\n' + self.text_input.text + '\n\n')
        self.text_input.text = ''

if __name__ == '__main__':
    JournalApp().run()