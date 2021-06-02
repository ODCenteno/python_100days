from tkinter import *
import math

# ----------- COLOR PALLET AND CONSTANTS

GREEN = '#98ca3f'
GRAPE = '#4b3f72'
SHADOWS = '#bfacb5'
RED = '#C43A32'
LIGHT_BLUE = '#33B1FF'
DEEP_BLUE = '#131F3D'
ORANGE = '#FF9F00'
WHITE = '#F7F7F7'
FONT_NAME = 'intro'
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ----------- TIMER RESET


def reset_timer():
    window.after_cancel(timer)  # Stop the timer count
    start_button.config(state="active")
    canvas.itemconfig(timer_text, text='00:00')
    work_label.config(text="Lets start")
    check_label.config(text='')
    # check_marks
    global reps
    reps = 0

# ----------- TIMER MECHANISM


def start_timer():
    global reps
    reps += 1

    start_button.config(state="disabled")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_dow(long_break_sec)
        work_label.config(text='Take a long break', fg=GRAPE)
    elif reps % 2 == 0:
        count_dow(short_break_sec)
        work_label.config(text='Take a short break', fg=SHADOWS)
    else:
        count_dow(work_sec)
        work_label.config(text='Time to focus', fg=LIGHT_BLUE)


# ----------- COUNTDOWN MECHANISM


def count_dow(count=(25 * 60)):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_dow, count - 1)
    else:
        start_timer()
        check_marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_marks += '✅'
        check_label.config(text=check_marks)

# ----------- UI SETUP

# Create a Window
window = Tk()
window.title('Platzidoro')
window.config(padx=50, pady=0, bg=DEEP_BLUE)

# Displaying an image using canvas
canvas = Canvas(width=200, height=224, bg=DEEP_BLUE, highlightthickness=0)
tomato_img =PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='25:00', fill=GREEN, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)

# count_dow(5)

# Buttons
start_button = Button(text='start', bg=ORANGE, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3, pady=10)
reset_button = Button(text='Reset', bg=ORANGE, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3, pady=10)

# Display Text as Labels
title_label = Label(text='Platzidoro Timer', fg=GREEN, bg=DEEP_BLUE, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0, pady=20)
check_label = Label(text='', bg=DEEP_BLUE, highlightthickness=0, font=(FONT_NAME, 50, 'normal'))
check_label.grid(column=1, row=4)
work_label = Label(text='Lets start...', fg=LIGHT_BLUE, bg=DEEP_BLUE, font=(FONT_NAME, 24, 'bold'))
work_label.grid(column=1, row=1, pady=20)

window.mainloop()

