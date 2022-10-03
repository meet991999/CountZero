import random
import tkinter

win = tkinter.Tk()
win.minsize(width=600, height=400)
win.resizable(False, False)
win.config(bg="#1f9ae0")
win.title("Rock Paper Scissors.....")

computer_options = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}


def button_disable():
    rock_button.config(state="disabled")
    papper_button.config(state="disabled")
    scissors_button.config(state="disabled")


def isrock():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = "Wohoo! You Won"
    else:
        match_result = "Computer Win"
    c_lable.config(text=match_result)
    player_lable.config(text="Rock")
    computer_lable.config(text=value)
    button_disable()


def ispaper():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Paper":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Amazingg..You won"
    c_lable.config(text=match_result)
    player_lable.config(text="Paper")
    computer_lable.config(text=value)
    button_disable()


def isscissor():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Computer Win"
    elif value == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "You Win... :D"
    c_lable.config(text=match_result)
    player_lable.config(text="Scissor")
    computer_lable.config(text=value)
    button_disable()


def reset():
    rock_button.config(state="active")
    papper_button.config(state="active")
    scissors_button.config(state="active")
    player_lable.config(text="player")
    computer_lable.config(text="computer")
    c_lable.config(text="")


# first Two row
title_lable = tkinter.Label(text="Rock Paper Scissors", font=('Century', 20, 'bold'))
title_lable.config(height=3, bg="#1f9ae0")
title_lable.grid(column=1, row=0)

player_lable = tkinter.Label(text="Player", font=('Century', 15, 'bold'))
player_lable.config(padx=60, bg="#1f9ae0", height=3)
player_lable.grid(column=0, row=1)

vs_lable = tkinter.Label(text="Vs", font=('Century', 15, 'bold'), bg="#1f9ae0")
vs_lable.grid(column=1, row=1)

computer_lable = tkinter.Label(text="Computer", font=('Century', 15, 'bold'), bg="#1f9ae0")
computer_lable.grid(column=2, row=1)

# input Row
# player_input_lable = tkinter.Label(text="Player chose Nothing",font=('Century',10, 'bold'),bg="#1f9ae0")
# player_input_lable.config(pady=40)
# player_input_lable.grid(column=0,row=2)
#
# computer_input_lable = tkinter.Label(text="Computer chose Nothing",font=('Century',10, 'bold'),bg="#1f9ae0")
# computer_input_lable.grid(column=2,row=2)


# Buttons row
rock_button = tkinter.Button(text="Rock", font=('Century', 15, 'bold'), bg="#747f8b", fg="white", command=isrock)
rock_button.grid(column=0, row=3)

papper_button = tkinter.Button(text="Paper", font=('Century', 15, 'bold'), bg="#747f8b", fg="white", command=ispaper)
papper_button.grid(column=1, row=3)

scissors_button = tkinter.Button(text="Scissors", font=('Century', 15, 'bold'), bg="#747f8b", fg="white",
                                 command=isscissor)
scissors_button.grid(column=2, row=3)

# for space
c_lable = tkinter.Label(text="", bg="#1f9ae0", font=('Century', 15, 'bold'))
c_lable.config(height=4)
c_lable.grid(column=1, row=4)

Reset_button = tkinter.Button(text="Reset", font=('Century', 15, 'bold'), bg="#747f8b", fg="white", command=reset)
Reset_button.grid(column=1, row=5)

win.mainloop()

# bg=#747f8b
