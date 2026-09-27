import tkinter as tk
root = tk.Tk()
score = 0
root.title("Clicker Game")

def AddScore():
    global score
    score += 1
    lbl.config(text=f"Score: {score}")

def Reset():
    global score
    score = 0
    lbl.config(text=f"Score: {score}")

lbl=tk.Label(root, text=f"Score: {score}")

clckbtn = tk.Button(root, text="Click Me For More Points!", command=AddScore)

resetbtn = tk.Button(root, text="RESET", command=Reset)

lbl.pack()
clckbtn.pack()
resetbtn.pack()

root.mainloop()


