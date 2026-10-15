import random
import time
import customtkinter as ctk

# 1. Setup the beautiful system appearance theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x700")  # Made it slightly taller to fit everything perfectly!
root.title("Clicker Game Ultimate Edition 🎮")

# --- GAME VARIABLES ---
Score = 0
AddClickScore = 1
AutoClickersCount = 0  # Tracks how many auto-clickers you own
AutoClickerCost = 50   # Starting cost for the automatic helper

# Super Mode Variables
SuperModeActive = False
ProgressValue = 0.0    # Progress goes from 0.0 to 1.0


# --- GAME FUNCTIONS ---

# This handles when Super Mode wears off
def end_super_mode():
    global SuperModeActive, ProgressValue
    SuperModeActive = False
    ProgressValue = 0.0
    power_bar.set(0.0)
    # Reset colors back to standard blue
    clckbtn.configure(fg_color=["#3a7ebf", "#1f538d"], hover_color=["#325882", "#14375e"])
    notificationsLbl.configure(text="Super Mode ended! Back to normal.")


# The main engine for adding scores
def AddScore():
    global Score, AddClickScore, SuperModeActive, ProgressValue
    
    # Calculate how many points to add
    points_to_add = AddClickScore * 2 if SuperModeActive else AddClickScore
    Score += points_to_add
    Screlbl.configure(text=f"Score: {Score}")
    
    # Fill up the progress meter if not already in super mode
    if not SuperModeActive:
        ProgressValue += 0.05  # Requires 20 clicks to fill to 1.0
        if ProgressValue >= 1.0:
            SuperModeActive = True
            ProgressValue = 1.0
            # Change the button color to an awesome glowing purple/pink!
            clckbtn.configure(fg_color="#A349A4", hover_color="#7A307C")
            notificationsLbl.configure(text="🔥 SUPER MODE ACTIVATED! 2x POINTS FOR 5 SECONDS! 🔥")
            # Run our timer loop to end it in 5000 milliseconds (5 seconds)
            root.after(5000, end_super_mode)
            
        power_bar.set(ProgressValue)


# Quietly runs every 1 second to handle automatic clicking!
def auto_click_loop():
    global Score, AutoClickersCount
    if AutoClickersCount > 0:
        # Add 1 point per auto clicker owned every single second
        Score += AutoClickersCount
        Screlbl.configure(text=f"Score: {Score}")
    
    # This keeps the loop repeating indefinitely once every 1000ms (1 second)
    root.after(1000, auto_click_loop)


def BuyAutoClicker():
    global Score, AutoClickersCount, AutoClickerCost
    if Score >= AutoClickerCost:
        Score -= AutoClickerCost
        AutoClickersCount += 1
        Screlbl.configure(text=f"Score: {Score}")
        
        # Make the next one cost a bit more money so it gets harder!
        AutoClickerCost = int(AutoClickerCost * 1.5)
        autoclick_btn.configure(text=f"Buy Auto-Clicker (+1/sec) [Owned: {AutoClickersCount}] (Cost: {AutoClickerCost})")
        notificationsLbl.configure(text=f"Purchased an Auto-Clicker! It taps for you every second. @ {time.strftime('%H:%M')}")
    else:
        notificationsLbl.configure(text=f"Not enough points! You need {AutoClickerCost} points for an Auto-Clicker.")


def Reset():
    global Score, AddClickScore, AutoClickersCount, AutoClickerCost, ProgressValue, SuperModeActive
    Score = 0
    AddClickScore = 1
    AutoClickersCount = 0
    AutoClickerCost = 50
    ProgressValue = 0.0
    SuperModeActive = False
    
    Screlbl.configure(text=f"Score: {Score}")
    clckbtn.configure(text="🖱️\n\nCLICK ME!", fg_color=["#3a7ebf", "#1f538d"], hover_color=["#325882", "#14375e"])
    autoclick_btn.configure(text=f"Buy Auto-Clicker (+1/sec) [Owned: 0] (Cost: 50)")
    extraclckbtn.configure(text=f"Click me for 1 more click. (Cost: 10 Points)")
    power_bar.set(0.0)
    notificationsLbl.configure(text=f"Game completely reset! @ {time.strftime('%H:%M')}")


def ExtraClck():
    global AddClickScore, Score
    if Score >= 10:
        Score -= 10
        Screlbl.configure(text=f"Score: {Score}")
        AddClickScore += 1
        clckbtn.configure(text=f"🖱️\n\nCLICK ME!\n(+{AddClickScore})")
        notificationsLbl.configure(text=f"You purchased an extra click power! @ {time.strftime('%H:%M')}")
    else:
        notificationsLbl.configure(text=f"You need 10 points to purchase extra click power. You have {Score}.")


# --- WIDGET CREATION ---

# Score Display (Giant and Bold)
Screlbl = ctk.CTkLabel(root, text=f"Score: {Score}", font=("Impact", 36))
Screlbl.pack(pady=(30, 10))

# FEATURE 1: Giant Circular Emoji Clicker Button
clckbtn = ctk.CTkButton(
    root,
    text="🖱️\n\nCLICK ME!",
    font=("Impact", 24),
    command=AddScore,
    width=220,
    height=220,
    corner_radius=110,  # Corner radius equal to half the height makes a perfect circle!
)
clckbtn.pack(pady=15)

# FEATURE 2: Recharging Power-Up Meter
power_label = ctk.CTkLabel(root, text="Super Mode Charge Meter:", font=("Arial", 12, "italic"))
power_label.pack(pady=(5, 0))

power_bar = ctk.CTkProgressBar(root, width=320, height=15, progress_color="orange")
power_bar.set(0.0)
power_bar.pack(pady=(5, 20))

# FEATURE 3: Shop Frame Organizer
shop_frame = ctk.CTkFrame(root, width=420, height=160)
shop_frame.pack(pady=10, padx=20)
shop_frame.pack_propagate(False) # Prevents the frame from shrinking around its buttons

shop_title = ctk.CTkLabel(shop_frame, text="🛒 SYSTEM UPGRADES SHOP", font=("Arial", 14, "bold"))
shop_title.pack(pady=5)

extraclckbtn = ctk.CTkButton(
    shop_frame,
    text="Buy Manual Click Power +1 (Cost: 10 Points)",
    command=ExtraClck,
    width=380
)
extraclckbtn.pack(pady=5)

autoclick_btn = ctk.CTkButton(
    shop_frame,
    text=f"Buy Auto-Clicker (+1/sec) [Owned: {AutoClickersCount}] (Cost: {AutoClickerCost})",
    command=BuyAutoClicker,
    width=380,
    fg_color="green",
    hover_color="darkgreen"
)
autoclick_btn.pack(pady=5)

# Reset Button (Safely nestled right out of the way)
resetbtn = ctk.CTkButton(root, text="RESET GAME DATA", command=Reset, fg_color="red", hover_color="#8B0000", width=150)
resetbtn.pack(pady=15)

# Notifications log sitting cleanly at the bottom
notificationsLbl = ctk.CTkLabel(
    root,
    text="Welcome to the Clicker Upgrade! Start clicking your mouse!",
    wraplength=460,
    justify="center",
    font=("Courier", 12)
)
notificationsLbl.place(relx=0.5, rely=0.95, anchor="center")

# Start our background auto clicker clock ticking!
root.after(1000, auto_click_loop)

root.mainloop()
