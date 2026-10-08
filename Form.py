import tkinter as Tk

root = Tk.Tk()
root.geometry("400x550")
root.title("Form Application")

def Submit():
    global Text
    Text = Entry1.get()
    if Text:
        TextList.insert(Tk.END, Text)
        Entry1.delete(0, Tk.END)


frame = Tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

Entry1 = Tk.Entry(frame)
Entry1.grid(row=0, column=0, padx=2.5, pady=2.5)

SubmitBtn = Tk.Button(frame, text="Submit", command=Submit)
SubmitBtn.grid(row=1, column=0)

TextList = Tk.Listbox(frame)
TextList.grid(row=2, column=0)

root.mainloop()