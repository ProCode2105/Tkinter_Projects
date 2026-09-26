import tkinter as tk
root = tk.Tk()
score = 0
root.title("Clicker Game")

def AddScore():
    global score
    score += 1
    lbl.config(text=f"Score: {score}")

lbl=tk.Label(root, text=f"Score: {score}")

btn = tk.Button(root, text="Click Me For More Points!", command=AddScore)

lbl.grid(row=0, column=0)
btn.grid(row=1, column=0)

root.mainloop()


