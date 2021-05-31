from tkinter import *

"""
Making a Mile to Kilometer converter.
"""

def main():
    window = Tk()
    window.title('Km to Mile Converter')
    window.minsize(width=400, height=150)
    window.config(padx=20, pady=20)

    def make_calcule():
        value = user_input.get()
        km = float(value) * 1.609
        conversion_result_label.config(text=f'{km}')


    # Input Entry
    user_input = Entry(width=7)
    user_input.grid(column=1, row=0)

    # Labels
    label_i = Label(text='Amount to convert ->')
    label_i.grid(column=0, row=0, padx=10, pady=5)

    mile_label = Label(text='Miles')
    mile_label.grid(column=2, row=0, padx=10, pady=5)

    km_label = Label(text='Km')
    km_label.grid(column=2, row=1, padx=10, pady=5)

    is_equal_label = Label(text='Is equal to: ')
    is_equal_label.grid(column=0, row=1, padx=5)

    conversion_result_label = Label(text='0')
    conversion_result_label.grid(column=1, row=1)

    # Buttons
    calculate_button = Button(text='Calculate', command=make_calcule)
    calculate_button.grid(column=1, row=2, padx=10, pady=10)

    window.mainloop()


if __name__ == '__main__':
    main()
