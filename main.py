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
    global timer, reps
    if timer != None:        # is there something to reset.
        window.after_cancel(timer)        # this will cancel the effect of window.after()
        timer = None

    #resetting other widgets...
    title_label.configure(text="Timer", fg=GREEN)
    canvas.itemconfigure(timer_text, text="00:00")
    check_mark.configure(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer
    if timer == None:   # this will protect from starting timer if it is already started.
        reps += 1

        if reps % 8 == 0:
            work_time = LONG_BREAK_MIN
            title_label.configure(text="BREAK!", fg=RED)
        elif reps % 2 == 0:
            work_time = SHORT_BREAK_MIN
            title_label.configure(text="break!", fg=PINK)
        else:
            work_time = WORK_MIN
            title_label.configure(text="Work!", fg=GREEN)

        pop_up(window)          # raise above all window
        count_down(work_time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)      #(time(ms), function to call, arguments to the function)
        # this "timer" is used to cancel the effect or simply reset the timer
    else:  # restart the timer again after each reps so it doesnot stop automatically.
        timer = None
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.configure(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)
# window.minsize(width=400, height=400)

# Title
title_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"))
title_label.configure(bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

# Tomato Image
image_path = "tomato.png"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # highlightthickness = 0 to remove canvas border showing up
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
# Timer text
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.configure(highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", fg=RED, command=reset_timer)
reset_button.configure(highlightthickness=0)
reset_button.grid(column=2, row=2)

# Checkmark label
check_mark = Label(bg=YELLOW, fg=GREEN, font=("", 15))  # text="✔" in count_down function
check_mark.grid(column=1, row=3)

# ---------------------------- POP UP ------------------------------- # 
def pop_up(window):         # raise above all window.
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)


window.mainloop()
