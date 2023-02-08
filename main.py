import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as tb
from functions import *

# creating the window & window settings
root = tb.Window(themename = "superhero")
root.title("Network Tool by @furtif_coder")
root.geometry("500x320")
root.maxsize(width = 500, height = 320)
root.minsize(width = 500, height = 320)

# functions command²
def SelectOption(option):
    print(f"{option}")
    

def Calcul():
    userInput = entry.get()
    rep = messagebox.showinfo(title="Conversion", message=f"You typed {userInput}")
    print(rep)
    entry.config(text = "")
    
# create a menu for conversion type
conversionType = tb.Menubutton(root, bootstyle = "primary outlined", text = "Conversion Type")
conversionType.pack(pady = 40)

# conversion menue
conversionMenu = tb.Menu(conversionType)
# options of the menue
optionVar = tk.StringVar()
id = 0
options = ["Decimal to Binary", "Binary to Decimal", "IP Decimal to Binary", "Decode a.b.c.d/Mask"]
for option in options:
    conversionMenu.add_radiobutton(label = option, variable = optionVar, command = SelectOption)

# Associate the options menu with the menu type
conversionType['menu'] = conversionMenu

# Create an entry field
userInput = tk.StringVar()
entry = tb.Entry(root)
entry.pack(pady = 50)

# button
validate = tb.Button(root, text = "Validate",
                     command = lambda: Calcul(),
                     bootstyle = "info")
validate.pack(pady = 20)

root.mainloop()