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
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    status_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    count_tomato.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 == 1:
        count_down(WORK_MIN * 60)
        status_label.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        status_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        status_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1, count_down, count - 1)
    else:
        start_timer()
        count_pomodoro = REPS // 2
        marks = count_pomodoro * "✔"
        count_tomato.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)

status_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
status_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

count_tomato = Label(fg=GREEN, bg=YELLOW)
count_tomato.grid(column=1, row=3)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()


# text="✔"
