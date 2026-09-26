import tkinter as tk

root = tk.Tk()
root.title("Simple App")

def OnClick():
    print("Testing!")
    lbl.config(text="Button Clicked!")

lbl = tk.Label(root, text="Print Testing with this button !=>")
lbl.grid(row=0, column=0)

#print(lbl.config().keys())

btn = tk.Button(root, text="Button 1", command=OnClick)
btn.grid(row=0, column=1)

root.mainloop()
