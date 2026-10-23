import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("gold")

root = ctk.CTk()
root.geometry("400x550")
root.title("LPM Account")

def SignUp():
    global UsernameEntry
    global Username
    global Alerts
    Username = UsernameEntry.get()
    if Username:
        Username = UsernameEntry.get()
        UsernameEntry.delete(0, ctk.END)
        Password = PasswordEntry.get()
        PasswordEntry.delete(0, ctk.END)
    else:
        Alerts = "Please enter a username and password"
        AlertsLbl.configure(text=f"{Alerts}")

Alerts = ""

UsernameEntry = ctk.CTkEntry(root)
UsernameLbl = ctk.CTkLabel(root, text="Username:")
PasswordEntry = ctk.CTkEntry(root, show="*")
PasswordLbl = ctk.CTkLabel(root, text="Password:")
SignUpBtn = ctk.CTkButton(root, text="SignUp", command=SignUp)
AlertsLbl = ctk.CTkLabel(root, text=f"{Alerts}", font=("Arial", 12),text_color="red")

UsernameLbl.pack(pady=10)
UsernameEntry.pack(pady=10)
PasswordLbl.pack(pady=10)
PasswordEntry.pack(pady=10)
SignUpBtn.pack(pady=10)
AlertsLbl.pack(ipadx=0.0, ipady=1.0, anchor="sw")

root.mainloop()