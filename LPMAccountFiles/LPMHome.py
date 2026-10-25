import customtkinter as ctk

def Launch(LUsername, LPassword):
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("gold")

    global Username

    Username = LUsername

    root = ctk.CTk()
    root.configure(fg_color="gold") 
    root.geometry("400x600")
    root.title("LPM Home")

    WelcomeLbl = ctk.CTkLabel(root, text=f"Welcome, {Username}!", font=("Arial", 20, "bold"), text_color="blue")
    WelcomeLbl.pack(pady=20)

    root.mainloop()
