import tkinter as tk
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
    lbl.config(text=f"Score: {Score}")

def Reset():
    global Score
    Score = 0
    lbl.config(text=f"Score: {Score}")

lbl=tk.Label(root, text=f"Score: {Score}")

clckbtn = tk.Button(root, text="Click Me For More Points!", command=AddScore)

resetbtn = tk.Button(root, text="RESET", command=Reset)

notificationsLbl = tk.Label(root, text=f"Notifications: {Notifications}")

lbl.pack()
clckbtn.pack()
resetbtn.pack()
notificationsLbl.place(relx=1.0, rely=0.0,anchor='ne')

root.mainloop()


