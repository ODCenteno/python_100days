import tkinter as tk

"""
Leaning the TKinter basics: create a window and use of widgets and pack(), grid() and place()
"""


window = tk.Tk()
window.title('SuperGUI')
window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text='This is a Super Label', font=('helvetica', 24, 'bold'))
my_label.grid(column=0, row=0)


# Button

def button_clicked():
    new_text = input.get()
    my_label['text'] = f'{new_text}'

test_button = tk.Button(text='Hit me', command=button_clicked)
test_button.grid(column=1, row=1)

def spell_it():
    text = input.get()
    label = tk.Label()
    label['text'] = f'{text}'
    label.grid(column=2, row=4)

second_button = tk.Button(text='new button', command=spell_it)
second_button.grid(column=3, row=3)

# Entry

input = tk.Entry(width=12)
input.grid(column=2, row=1)
print(input.get())




window.mainloop()
