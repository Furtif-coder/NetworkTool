import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from functions import *
from random import choice


# creating the window & window settings
theme = choice(["darkly", "superhero", "cyborg", "vapor", "solar"])
root = tb.Window(themename = theme)
root.title("Network Tool by @furtif_coder")
root.geometry("500x320")
root.maxsize(width = 500, height = 320)
root.minsize(width = 500, height = 320)

# type of operation
operation = 0
# functions command

def SelectOption(option):
    global operation

    if option == "Decimal to Binary":
        operation = 1
    elif option == "Binary to Decimal":
        operation = 2
    elif option == "Decimal IP to Binary":
        operation = 3
    elif option == "Decode a.b.c.d/Mask":
        operation = 4

# Option 1: decimal to binary
def ToBinary(userInput):
    converted = toBinary(userInput)
    if converted == 1:
        messagebox.showerror("Conversion Error!", f"{userInput} is out of range [0,255]")
    elif converted == 2:
        messagebox.showerror("Conversion Error!", f"{userInput} contains unexpected alphanumeric characters")
    else:
        rep = messagebox.showinfo(title="Conversion", message=f"{userInput} in binary is: {converted}")

# Option 2: binary to decimal    
def ToDecimal(userInput):
    converted = toDecimal(userInput)
    if converted == -1: # Negative number
        messagebox.showerror("Conversion Error!", f"{userInput} is negative") 
    elif converted == -2: # More than 8 bits
        messagebox.showerror("Conversion Error!", f"You wrote: {userInput}\nMax length of a byte is 8 digits") 
    elif converted == -3: # Digit other than '0' or '1'
        messagebox.showerror("Conversion Error!", f"You wrote: {userInput}\nBinary digits only consist of '0' and '1'") 
    elif converted == -4: # Extra characters
        messagebox.showerror("Conversion Error!", f"'{userInput}' contains unexpected alphanumeric characters") 
    else:
        rep = messagebox.showinfo(title="Conversion", message=f"{userInput} in Decimal is: {converted}")

# Option 3: full IP decimal to binary
def IpToBinary(userInput):
    converted = ipToBinary(userInput)
    if converted == -1:
        messagebox.showerror("Conversion Error!", "Write an IP with decimal bytes: a.b.c.d\na, b, c, have to be integers in range [0, 255]")
    else:
        messagebox.showinfo("Conversion full IP", f"{userInput} : {converted}")

# Option 4: decode a.b.c.d/mask
def DecodeIpMask(userInput):
    try:
        host, mask, network= readFullIP(userInput)
        message = f"Host : {host}\nSubnet Mask: {mask}\nNetwork: {network}\n"
        messagebox.showinfo(userInput, message)
    except:
        messagebox.showerror("Conversion Error!", "Please write correct IP and a valid mask\na.b.c.d/mask")

# Convert button
def Action():
    userInput = entry.get()

    if len(userInput) == 0: # Empty entry
            messagebox.showerror("Empty entry", "Please write something")
    else:
        if operation == 1:
            ToBinary(userInput)
        elif operation == 2:
            ToDecimal(userInput)
        elif operation == 3:
            IpToBinary(userInput)
        elif operation == 4:
            DecodeIpMask(userInput)
        else: # Didn't pick a conversion type
            messagebox.showinfo("Conversion", "Choose the type of conversion in the menu on top")

# options of the menu
options = ["Decimal to Binary", "Binary to Decimal", "Decimal IP to Binary", "Decode a.b.c.d/Mask"]

# -- Creating widgets -- #
# create a menubutton for conversion type
conversionType = tb.Menubutton(root, bootstyle = "success outlined", text="Conversion Type")
conversionType.pack(pady = 40)

# create a menu inside Conversion type menubutton
menu = tb.Menu(conversionType)

# add option to menu
for option in options:
    menu.add_radiobutton(label=option, command = lambda option = option: SelectOption(option))

# associate the menu with the menu_button
conversionType['menu'] = menu

# Create an entry field
entry = tb.Entry(root)
entry.pack(pady = 50)

# Convert button
validate = tb.Button(root, text = "Convert", command = lambda: Action(), bootstyle = "warning outline")
validate.pack(pady = 10)

root.mainloop()
