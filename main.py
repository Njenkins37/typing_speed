from tkinter import *
from text import Sample_Text

display_timer = None


def start():
    global display_timer
    user_text.config(state=NORMAL)
    display_timer = window.after(1000, count_down, 60)


def count_down(count):
    timer.config(text=count)
    if count > 0:
        global display_timer
        display_timer = window.after(1000, count_down, count - 1)
    else:
        user_text.config(state=DISABLED)
        formatted_text = str(user_text.get(0.0, "end"))
        cpm = len(formatted_text)
        wpm = int(cpm / 5)
        dissected_text = str(sample_text)[:cpm - 1]
        acc_count = 0
        for index, char in enumerate(dissected_text):
            if char == formatted_text[index]:
                acc_count += 1
        text = f'You typed {cpm} characters per minute.\nYou typed approximately {wpm} words per minute.\nYour accuracy is {(acc_count / len(dissected_text) * 100)}%'
        stats_label = Label(text=text, bg='black', fg='white',
                         font=('Serif', 18, 'normal'))
        stats_label.grid(row = 1, column=3)


def reset():
    timer.config(text='60')
    generate_new_sample()
    global display_timer
    if display_timer is not None:
        window.after_cancel(display_timer)
        display_timer = None


def generate_new_sample():
    global sample_text
    sample_text = Sample_Text()
    canvas.itemconfig(typing_text, text=str(sample_text))


sample_text = Sample_Text()

window = Tk()
window.title("Typing Speed")
window.config(padx=100, pady=50, bg='black')

timer = Label(text='60', fg='white', bg='black', highlightthickness=0, font=('Serif', 35, 'bold'))
timer.grid(row=0, column=0, padx=10, pady=15)

canvas = Canvas(width=600, height=200, highlightthickness=1, bg='white')
typing_text = canvas.create_text(275, 110, text=str(sample_text), fill='black', font=('Serif', 14, 'normal'),
                                 width=520)
canvas.grid(row=0, column=1, padx=10, pady=10)

user_text = Text(window, height=15, width=85, bg="black", fg="white")
user_text.config(state=DISABLED)
user_text.grid(row=1, column=1, padx=10, pady=10)

start = Button(text='Start', font=('Serif', 12, 'normal'), command=start, highlightthickness=0)
start.grid(row=2, column=0, padx=10, pady=10)

reset = Button(text='Reset', font=('Serif', 12, 'normal'), command=reset, highlightthickness=0)
reset.grid(row=2, column=3, padx=10, pady=10)
window.mainloop()
