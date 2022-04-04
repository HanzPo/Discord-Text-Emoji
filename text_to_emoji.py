import pyperclip
from tkinter import *
from tkinter.ttk import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Text to Discord Emoji Text Converter")
        self.resizable(width=False, height=False)
        self.string_value = StringVar()
        self.result_value = StringVar()

        self.make_widgets()
    
    def make_widgets(self):
        padding = {'padx' : 2, 'pady' : 2}
        self.text_entry = Entry(width=50, textvariable=self.string_value).grid(column=0, row=0, **padding)
        self.convert_button = Button(width=10, text="Convert", command=self.convert_text).grid(column=1, row=0, **padding)
        self.result_entry = Entry(width=50, textvariable=self.result_value).grid(column=0, row=1, **padding)
        self.copy_button = Button(width=10, text="Copy", command=self.copy_text).grid(column=1, row=1, **padding)

    def convert_text(self):
        #List for numeric emojis
        numberEmojis = [':zero: ', ':one: ', ':two: ', ':three: ', ':four: ', ':five: ', ':six: ', ':seven: ', ':eight: ', ':nine: ']

        #Converts user input to text
        text_chars = list(self.string_value.get())

        #Loops through each character and converts it to emoji format accordingly
        for i in range(len(text_chars)):
            if text_chars[i] == '?':
                text_chars[i] = ':grey_question: '
            elif text_chars[i] == '!':
                text_chars[i] = ':grey_exclamation: '
            elif text_chars[i].isnumeric() == True:
                text_chars[i] = numberEmojis[int(text_chars[i])]
            elif text_chars[i].isalpha() == True:
                text_chars[i] = ':regional_indicator_' + text_chars[i] + ': '
            else:
                pass
        
        self.result_value.set(''.join(text_chars))
    
    def copy_text(self):
        pyperclip.copy(self.result_value.get())

app = App()
app.mainloop()
