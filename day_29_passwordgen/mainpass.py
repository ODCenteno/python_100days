from tkinter import *
from tkinter import messagebox
import pyperclip

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
    entry_list = [website_entry.get(), user_entry.get(), password_entry.get()]
    save_list = f'{entry_list[0]} | {entry_list[1]} | {entry_list[2]}\n'

    if len(entry_list[0]) == 0 or len(entry_list[2]) == 0:
        messagebox.showinfo(title='Opps', message='Do not let any field empty')
    else:
        is_ok = messagebox.askokcancel(title='New Password Details',
                                       message=f'These are the details entered:\n\n'
                                               f'Website: {entry_list[0]}\n'
                                               f'Email/User: {entry_list[1]} '
                                               f'Password: {entry_list[2]}'
                                       )

        if is_ok:
            with open('data.txt', mode='a', encoding='utf-8') as data:
                data.write(save_list)
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')


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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, pady=5)
website_entry.focus()  # El cursor apunta a este Entry

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2, pady=5)
user_entry.insert(0, 'daniel.centeno.manzo@gmail.com')

password_entry = Entry(width=19)
password_entry.grid(column=1, row=3, columnspan=1, pady=5)

# Labels
website_label = Label(text='Website: ', font=('helvetica', 16))
website_label.grid(column=0, row=1, pady=5)

user_label = Label(text='Email/Username: ', font=('helvetica', 16))
user_label.grid(column=0, row=2, pady=5)

password_label = Label(text='Password: ', font=('helvetica', 16))
password_label.grid(column=0, row=3, pady=5)

# Buttons
generate_pass_button = Button(text='Generate Password', font=('helvetica', 12), command=call_password)
generate_pass_button.grid(column=2, row=3, pady=5)

add_button = Button(text='Add', width=36, font=('helvetica', 16), command=save)
add_button.grid(column=1, row=4, pady=5, columnspan=2)

window.mainloop()
