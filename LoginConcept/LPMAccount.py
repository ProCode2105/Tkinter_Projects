import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("gold")

root = ctk.CTk()
root.configure(fg_color="lightblue") 
root.geometry("400x550")
root.title("LPM Account")

def SignUp():
    global UsernameEntry
    global Username
    global Alerts
    global Password
    Username = UsernameEntry.get()
    Password = PasswordEntry.get()
    if Username and Password:
        Username = UsernameEntry.get()
        UsernameEntry.delete(0, ctk.END)
        Password = PasswordEntry.get()
        PasswordEntry.delete(0, ctk.END)
        with open("LoginConcept/UsernameAndPassword.txt", "a") as f:
            f.write(f"{Username}:{Password}\n")
    else:
        Alerts = "Please enter a username and password"
        AlertsLbl.configure(text=f"{Alerts}")

Alerts = ""

UsernameEntry = ctk.CTkEntry(root)
UsernameLbl = ctk.CTkLabel(root, text="Username:")
PasswordEntry = ctk.CTkEntry(root, show="*")
PasswordLbl = ctk.CTkLabel(root, text="Password:")
SignUpBtn = ctk.CTkButton(root, text="Sign Up", command=SignUp)
AlertsLbl = ctk.CTkLabel(root, text=f"{Alerts}", font=("Arial", 12),text_color="red")

UsernameLbl.pack(pady=10)
UsernameEntry.pack(pady=10)
PasswordLbl.pack(pady=10)
PasswordEntry.pack(pady=10)
SignUpBtn.pack(pady=10)
AlertsLbl.pack(ipadx=0.0, ipady=1.0, anchor="sw")

root.mainloop()