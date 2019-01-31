# hello-gui.py

# Import everything required from the tkinter moduole
from tkinter import *

# Function called by clicking my_button:
def change_text():
    my_label.config(text='Hello World')

# Create the main tkinter window
window = Tk()
window.title('My application')

# Add an empty tkinter label widget and place it in a grid layout
my_label = Label(window, width=25, height=3, text='')
my_label.grid(row=0, column=0)

# Add a tkinter button widget, place it in th grid layout
# and attach the change_text() function
my_button = Button(window, text='Say Hi', width=10, command=change_text)
my_button.grid(row=1, column=0)

# A text entry box with a label
Label(window, text='Name:') .grid(row=0, column=0)
my_text_box = Entry(window, width=15)
my_text_box.grid(row=0, column=1)

# Enter the main event loop
window.mainloop()
