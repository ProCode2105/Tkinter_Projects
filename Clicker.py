import tkinter as tk
root = tk.Tk()
score = 0
root.title("Clicker Game")

def AddScore():
    global score
    score += 1
    lbl.config(text=f"Score: {score}")

def ResetScore():
    global score
    score = 0
    lbl.config(text=f"Score: {score}")

lbl=tk.Label(root, text=f"Score: {score}")

clckbtn = tk.Button(root, text="Click Me For More Points!", command=AddScore)

resetbtn = tk.Button(root, text="RESET SCORE", command=ResetScore)

lbl.grid(row=0, column=0)
clckbtn.grid(row=1, column=0)
resetbtn.grid(row=2, column=0)

root.mainloop()


