import tkinter

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
    global reps
    reps = 0
    window.after_cancel(timer)
    title_lb.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_lb.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        title_lb.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_lb.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lb.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = count // 60
    count_sec = count % 60
    # 파이썬 동적 타이핑 이용
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # canvas.itemconfig(timer_text, text="%02d:%02d" % (count_min, count_sec)) # 문자 포매팅 이용
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_lb.config(text="✔" * (reps//2))


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_lb = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title_lb.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_lb = tkinter.Label(font=("Arial", 15), bg=YELLOW, fg=GREEN)
check_lb.grid(row=3, column=1)

window.mainloop()
