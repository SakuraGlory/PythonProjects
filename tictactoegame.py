from idlelib import window
from tkinter import  *
import random


def next_trun(row, column):
    global Player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if Player == Players[0]:
            buttons[row][column]['text'] = Player

            if check_winner() is False:
                Player = Players[1]
                lable.config(text=(Players[1] + " turn"))
            elif check_winner() is True:
                lable.config(text=(Players[0] + "wins"))
            elif check_winner() == "Tie":
                lable.config(text=("Tie!"))
        else:
            buttons[row][column]['text'] = Player

            if check_winner() is False:
                Player = Players[0]
                lable.config(text=(Players[0] + " turn"))
            elif check_winner() is True:
                lable.config(text=(Players[1] + "wins"))
            elif check_winner() == "Tie":
                lable.config(text=("Tie!"))







def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return True

        elif empty_spaces() is False:
            return "Tie"

        else:
            return False


def empty_spaces():

    spaces = 9

    for row  in range (3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1

    if spaces ==0:
        return False
    else:
        return True


def new_game( ):
    pass


Window = Tk()
Window.title("Tic-Tac-Toe")
Players = ["x","o"]
Player = random.choice(Players)
buttons = [[0,0,0,],
           [0,0,0,],
           [0,0,0,]]
lable = Label(text= Player +"trun", font=('conosolas',40))
lable.pack(side="top")

reset_button = Button(text="Restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(Window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_trun(row, column))
        buttons[row][column].grid(row=row, column=column)



Window.mainloop()


