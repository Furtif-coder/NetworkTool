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

# functions command
def SelectOption(option):
    #print(f"{option}")
    pass

# Option 1: decimal to binary
def ToBinary(userInput):
    converted = toBinary(userInput)
    if converted == 1:
        messagebox.showerror("Error!", f"{userInput} is out of range [0,255]")
    elif converted == 2:
        messagebox.showerror("Error!", f"{userInput} contains unexpected alphanumeric characters")
    else:
        rep = messagebox.showinfo(title="Conversion", message=f"{userInput} in binary is: {converted}")

# Option 2: binary to decimal    
def ToDecimal(userInput):
    converted = toDecimal(userInput)
    if converted == 1: # Negative number
        messagebox.showerror("Error!", f"{userInput} is negative") 
    elif converted == 2: # More than 8 bits
        messagebox.showerror("Error!", f"You wrote: {userInput}\nMax length of a byte is 8 digits") 
    elif converted == 3: # Digit other than '0' or '1'
        messagebox.showerror("Error!", f"You wrote: {userInput}\nBinary digits only consist of '0' and '1'") 
    elif converted == 4: # Extra characters
        messagebox.showerror("Error!", f"'{userInput}' contains unexpected alphanumeric characters") 
    else:
        rep = messagebox.showinfo(title="Conversion", message=f"{userInput} in Decimal is: {converted}")




def Action():
    userInput = entry.get()
    option = 2
    if len(userInput) == 0:
            messagebox.showerror("Empty entry", f"{userInput} Please write something") # Negative number
    else:
        if option == 1:
            ToBinary(userInput)
        elif option == 2:
            ToDecimal(userInput)
            


   

# options of the menu
options = ["Decimal to Binary", "Binary to Decimal", "IP Decimal to Binary", "Decode a.b.c.d/Mask"]

# create a menubutton for conversion type
conversionType = tb.Menubutton(root, bootstyle = "primary outlined", text="Conversion Type")
conversionType.pack(pady = 40)

# create a menu
menu = tb.Menu(conversionType)

# add option to menu
optionVar = tk.StringVar()
for option in options:
    menu.add_radiobutton(label=option)




# conversion menu
#conversionMenu = tb.Menu(conversionType)




# Create an entry field
userInput = tk.StringVar()
entry = tb.Entry(root)
entry.pack(pady = 50)

# button
validate = tb.Button(root, text = "Validate",
                     command = lambda: Action(),
                     bootstyle = "secondary outline")
validate.pack(pady = 10)

root.mainloop()