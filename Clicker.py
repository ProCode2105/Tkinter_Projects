import tkinter as tk
import time
root = tk.Tk()
root.geometry("500x400")
Score = 0
AddClickScore = 1
Notifications = ""
root.title("Clicker Game")

def AddScore():
    global Score
    global AddClickScore
    Score += AddClickScore
    Screlbl.config(text=f"Score: {Score}")

def Reset():
    global Score
    Score = 0
    Screlbl.config(text=f"Score: {Score}")
    Notifications = f"You have reset the game. @ {time.strftime("%H:%M")}"

def ExtraClck():
    AddClickScore += 1
    clckbtn.config(text=f"Click Me For {AddClickScore} Point(s)!")

Screlbl=tk.Label(root, text=f"Score: {Score}")

clckbtn = tk.Button(root, text=f"Click Me For {AddClickScore} Point(s)!", command=AddScore)

resetbtn = tk.Button(root, text="RESET", command=Reset)

extraclckbtn = tk.Button(root, text="Click me for 1 more click.", command=ExtraClck)

notificationsLbl = tk.Label(root, text=f"Notifications: {Notifications}")

Screlbl.pack()
clckbtn.pack()
resetbtn.pack()
notificationsLbl.place(relx=1.0, rely=0.0,anchor='ne')

root.mainloop()


