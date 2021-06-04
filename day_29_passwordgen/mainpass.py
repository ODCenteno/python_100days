from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from password_generator import create_password

GRAPE = '#4b3f72'
SHADOWS = '#bfacb5'
RED = '#C43A32'
LIGHT_BLUE = '#33B1FF'
DEEP_BLUE = '#131F3D'
ORANGE = '#FF9F00'
WHITE = '#F7F7F7'


# ------------ PASSWORD GENERATOR

def call_password():
    password_entry.delete(0, 'end')
    new_password = create_password()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ------------ SAVE PASSWORD

def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Opps', message='Do not let any field empty')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError as ferr:
            with open('data.json', "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ------------ SEARCH PASSWORD

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as ferr:
        messagebox.showinfo(title='Error loading the file', message=f'{ferr}')
    else:
        for (web, val) in data.items():
            print(f'this is web: {web}')
            if web == website:
                password = val['password']
                email = val['email']
                print(f'email: {email}, password: {password}.')
                messagebox.showinfo(title=web, message=f'email: {email}\npassword: {password}')
                break
            else:
                messagebox.showinfo(title=website, message=f'Can not find any data for {website}')
                break



# ------------ UI SETUP

# Window display
window = Tk()
window.minsize(width=220, height=220)
window.title('Password Generator')
window.config(padx=50, pady=50)

# Canva Setup
canva = Canvas(width=220, height=220, bg=SHADOWS, highlightthickness=0)
file_img = PhotoImage(file='logo.png')
canva.create_image(110, 110, image=file_img)
canva.grid(column=1, row=0, pady=5)

# Entry inputs
website_entry = Entry(width=23)
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()  # El cursor apunta a este Entry

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2, pady=5)
user_entry.insert(0, 'daniel.centeno.manzo@gmail.com')

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3, columnspan=1, pady=5)

# Labels
website_label = Label(text='Website: ', font=('helvetica', 16))
website_label.grid(column=0, row=1, pady=5)

user_label = Label(text='Email/Username: ', font=('helvetica', 16))
user_label.grid(column=0, row=2, pady=5)

password_label = Label(text='Password: ', font=('helvetica', 16))
password_label.grid(column=0, row=3, pady=5)

# Buttons
search_button = Button(text='Search', width=15, font=('helvetica', 12), command=find_password)
search_button.grid(column=2, row=1, pady=5)

generate_pass_button = Button(text='Generate Password', font=('helvetica', 12), command=call_password)
generate_pass_button.grid(column=2, row=3, pady=5)

add_button = Button(text='Add', width=36, font=('helvetica', 16), command=save)
add_button.grid(column=1, row=4, pady=5, columnspan=2)

window.mainloop()
