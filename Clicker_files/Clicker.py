import random
import time
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x650")

Score = 0
AddClickScore = 1
Notifications = ""
root.title("Clicker Game")


def AddScore():
    global Score
    global AddClickScore
    Score += AddClickScore

    Screlbl.configure(text=f"Score: {Score}")


def Reset():
    global Score
    global Notifications
    Score = 0
    Screlbl.configure(text=f"Score: {Score}")
    Notifications = f"You have reset the game. @ {time.strftime('%H:%M')}"
    notificationsLbl.configure(text=Notifications)


def ExtraClck():
    global AddClickScore
    global Score
    if Score >= 10:
        Score -= 10
        Screlbl.configure(text=f"Score: {Score}")
        notificationsLbl.configure(
            text=f"You have purchased an extra click. @ {time.strftime('%H:%M')}"
        )
        AddClickScore += 1
    else:
        notificationsLbl.configure(
            text=f"You do not have enough clicks to purchase an extra click. You have {Score} points. @ {time.strftime('%H:%M')}"
        )

    clckbtn.configure(text=f"Click Me For {AddClickScore} Point(s)!")


Screlbl = ctk.CTkLabel(root, text=f"Score: {Score}", font=("Arial", 20, "bold"))

clckbtn = ctk.CTkButton(
    root, text=f"Click Me For {AddClickScore} Point(s)!", command=AddScore
)

resetbtn = ctk.CTkButton(root, text="RESET", command=Reset, fg_color="red")

extraclckbtn = ctk.CTkButton(
    root,
    text="Click me for 1 more click. (Cost: 10 Points)",
    command=ExtraClck,
)

notificationsLbl = ctk.CTkLabel(
    root,
    text=f"Notifications: {Notifications}",
    wraplength=490,
    justify="left",
    font=("consolas", 15, "bold"),
)

Screlbl.pack(pady=10)
clckbtn.pack(pady=10)
resetbtn.pack(pady=10)

extraclckbtn.place(relx=0.0, rely=1.0, anchor="sw")
notificationsLbl.place(relx=1.0, rely=0.93, anchor="se")

root.mainloop()

