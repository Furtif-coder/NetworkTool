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

operation = ""
# functions command
def SelectOption(option):
    global operation
    #print(f"{option}")
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

# Option 3: full IP decimal to binary
def IpToBinary(userInput):
    converted = ipToBinary(userInput)
    if converted == -1:
        messagebox.showerror("Error!", "Write an IP with decimal bytes: a.b.c.d")
    else:
        messagebox.showinfo("Conversion full IP", f"{userInput} : {converted}")

# Option 4: decode a.b.c.d/mask
def DecodeIpMask(userInput):
    host, mask, network= readFullIP(userInput)
    message = f"Host : {host}\nSubnet Mask: {mask}\nNetwork: {network}\n"
    messagebox.showinfo(userInput, message)


def Action():
    userInput = entry.get()

    if len(userInput) == 0:
            messagebox.showerror("Empty entry", "Please write something") # Negative number
    else:
        if operation == 1:
            ToBinary(userInput)
        elif operation == 2:
            ToDecimal(userInput)
        elif operation == 3:
            IpToBinary(userInput)
        elif operation == 4:
            DecodeIpMask(userInput)
        else:
            messagebox.showinfo("Conversion", "Choose the type of conversion in the menu on top") 
# options of the menu
options = ["Decimal to Binary", "Binary to Decimal", "Decimal IP to Binary", "Decode a.b.c.d/Mask"]

# create a menubutton for conversion type
conversionType = tb.Menubutton(root, bootstyle = "success outlined", text="Conversion Type")
conversionType.pack(pady = 40)

# create a menu
menu = tb.Menu(conversionType)

# add option to menu
optionVar = tk.StringVar()
for option in options:
    menu.add_radiobutton(label=option, command = lambda option = option: SelectOption(option))

# associate the menu with the menu_button
conversionType['menu'] = menu

# Create an entry field
userInput = tk.StringVar()
entry = tb.Entry(root)
entry.pack(pady = 50)

# button
validate = tb.Button(root, text = "Validate", command = lambda: Action(), bootstyle = "warning outline")
validate.pack(pady = 10)

root.mainloop()