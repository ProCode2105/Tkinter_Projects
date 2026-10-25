import customtkinter as ctk
import LPMHome

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("gold")

root = ctk.CTk()
root.configure(fg_color="lightblue") 
root.geometry("400x600")
root.title("LPM Account")

FilePath = "LPMAccountFiles/UsernameAndPassword.txt"

def OpenHome():
    root.destroy()
    LPMHome.Launch(LUsername = LUsername, LPassword = LPassword)

def SignUp():
    global SUUsername
    global Alerts
    global SUPassword
    SUUsername = SUUsernameEntry.get()
    SUPassword = SUPasswordEntry.get()
    if Save == "Yes":
        if SUUsername and SUPassword:
            Username = SUUsernameEntry.get()
            SUUsernameEntry.delete(0, ctk.END)
            Password = SUPasswordEntry.get()
            SUPasswordEntry.delete(0, ctk.END)
            with open(FilePath, "r") as f:
                for line in f:
                    saved_username, _ = line.strip().split(":")
                    if Username == saved_username:
                        Alerts = "That username is already taken!"
                        AlertsLbl.configure(text=f"{Alerts}", text_color="red")
                        return False

            with open(FilePath, "a") as f:
                f.write(f"{Username}:{Password}\n")
            Alerts = "Registration successful"
            AlertsLbl.configure(text=f"{Alerts}", text_color="green")
        else:
            Alerts = "Please enter a username and password"
            AlertsLbl.configure(text=f"{Alerts}", text_color="red")
    else:
        SUUsernameEntry.delete(0, ctk.END)
        SUPasswordEntry.delete(0, ctk.END)
        Alerts = ""
        AlertsLbl.configure(text=f"{Alerts}", text_color="red")
def Login():
    global LUsername
    global LPassword
    if Save == "Yes":
        LUsername = LUsernameEntry.get()
        LUsernameEntry.delete(0, ctk.END)
        LPassword = LPasswordEntry.get()
        LPasswordEntry.delete(0, ctk.END)
        if LUsername and LPassword:
            with open(FilePath, "r") as f:
                for line in f:
                    stored_username, stored_password = line.strip().split(":")
                    if LUsername == stored_username and LPassword == stored_password:
                        AlertsLbl.configure(text="Login successful", text_color="green")
                        root.after(1000, lambda: AlertsLbl.configure(text="Loading Window...", text_color="green"))
                        root.after(2500, OpenHome)

                        return True
            Alerts = "Invalid username or password"
            AlertsLbl.configure(text=f"{Alerts}", text_color="red")
        else:
            Alerts = "Please enter a username and password"
            AlertsLbl.configure(text=f"{Alerts}", text_color="red")
    else:
        LUsernameEntry.delete(0, ctk.END)
        LPasswordEntry.delete(0, ctk.END)
        Alerts = ""

def DontSave():
    global Save
    if Save == "No":
        Save = "Yes"
        DontSaveBtn.configure(text="Don't Save Username and Password")
    else:
        Save = "No"
        DontSaveBtn.configure(text="Save Username and Password")

Alerts = ""
Save = "Yes"
SUUsername = ""
SUPassword = ""
LUsername = ""
LPassword = ""

SUUsernameEntry = ctk.CTkEntry(root)
SUUsernameLbl = ctk.CTkLabel(root, text="Username:")
SUPasswordEntry = ctk.CTkEntry(root, show="*")
SUPasswordLbl = ctk.CTkLabel(root, text="Password:")
SignUpBtn = ctk.CTkButton(root, text="Sign Up", command=SignUp)

LUsernameEntry = ctk.CTkEntry(root)
LUsernameLbl = ctk.CTkLabel(root, text="Username:")
LPasswordEntry = ctk.CTkEntry(root, show="*")
LPasswordLbl = ctk.CTkLabel(root, text="Password:")
LoginBtn = ctk.CTkButton(root, text="Login", command=Login)

AlertsLbl = ctk.CTkLabel(root, text=f"{Alerts}", font=("Arial", 12),text_color="red")
DontSaveBtn = ctk.CTkButton(root, text="Don't Save Username and Password", command=DontSave)

SUUsernameLbl.pack(pady=10)
SUUsernameEntry.pack(pady=10)
SUPasswordLbl.pack(pady=10)
SUPasswordEntry.pack(pady=10)
SignUpBtn.pack(pady=10)

LUsernameLbl.pack(pady=10)
LUsernameEntry.pack(pady=10)
LPasswordLbl.pack(pady=10)
LPasswordEntry.pack(pady=10)
LoginBtn.pack(pady=10)

DontSaveBtn.pack(pady=10)
AlertsLbl.pack(ipadx=0.0, ipady=1.0, anchor="sw")

root.mainloop()