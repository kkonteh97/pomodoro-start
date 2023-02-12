from tkinter import *
import math
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
def reset_press():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    label.config(text="Timer", fg=GREEN)
    reps = 0
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_press():
    global reps
    reps += 1
    short_b = SHORT_BREAK_MIN * 60
    long_b = LONG_BREAK_MIN *60
    work = WORK_MIN*60
    if reps % 8 == 0:
        count_down(long_b)
        label.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_b)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(work)
        label.config(text="Work", fg=RED)
    print(reps)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_secs = (count%60)
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_secs}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_press()
        if reps % 2 == 0:
            check_label['text'] +="✔"




#---------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
window.minsize(width=500, height=200)

#_________________canvasTomato________________
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text  = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=2)

#_______________Timer Label_______________
label = Label()
label.config(text="Timer",font=(FONT_NAME, 30), bg=YELLOW,fg=GREEN)
label.grid(row=0,column=2)

#_____________________startButton___________________________
start_button = Button()
start_button.config(text="Start", font=(FONT_NAME, 10), command=start_press, fg="black")
start_button.grid(row=2, column=1)



#___________resetButton__________________________
reset_button = Button()
reset_button.config(text="Reset", font=(FONT_NAME, 10),command=reset_press, fg="black")
reset_button.grid(row=2, column=4)

#_____________checkmarklable_____________________
check_label = Label()
check_label.config(font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN)
check_label.grid(row=4, column=2)





window.mainloop()
