import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x550")
root.title("LPM Account")

def Login():
    global LoginEntry
    global Username
    Username = LoginEntry.get()
    if Username:
        Username = LoginEntry.get()
        LoginEntry.delete(0, ctk.END)
    else:
        print("Please enter a username.")

LoginEntry = ctk.CTkEntry(root)
LoginEntry.pack(pady=10)

PasswordEntry = ctk.CtkEntry(root)

LoginBtn = ctk.CTkButton(root, text="Login", command=Login)

LoginEntry.pack(pady=10)
LoginBtn.pack(pady=10)

root.mainloop()