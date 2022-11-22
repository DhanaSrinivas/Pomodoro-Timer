from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_label.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps%8==0 :
        count_down(long_sec)
        title_label.config(text="break", fg=GREEN)

    elif reps%2==0 :
        count_down(short_sec)
        title_label.config(text="break", fg=PINK)

    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    min_count = int(count/60)
    sec_count = int(count%60)

    if sec_count < 10 :
        sec_count = f"0{sec_count}"

    canvas.itemconfig(timer_text, text = f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")



title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg="black", fg=RED)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

canvas = Canvas(width=200, height=223, bg="black", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 24, "bold"), bg="black", fg=GREEN)
check_label.grid(row=3, column=1)

window.mainloop()
