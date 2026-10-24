import customtkinter as ctk

def Launch(LUsername):
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("gold")

    root = ctk.CTk()
    root.configure(fg_color="lightblue") 
    root.geometry("400x600")
    root.title("LPM Home")

    WelcomeLbl = ctk.CTkLabel(root, text=f"Welcome, {LUsername}!", font=("Arial", 20))
    WelcomeLbl.pack(pady=20)

    root.mainloop()