from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5/60
SHORT_BREAK_MIN = 5/60
LONG_BREAK_MIN = 5/60
reps = 0
num_check = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global num_check
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        num_check += "✓"
        check_label.config(text=num_check)
    elif reps % 8 ==0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    #1/3/5/7 rep = 25min
    #8 rep = long break
    #2/4/6 rep = short break

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 45, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

#Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

#Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

#Checkmark label
check_label = Label(font=(FONT_NAME, 12, "normal"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)


window.mainloop()