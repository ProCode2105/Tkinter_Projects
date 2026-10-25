import random
import customtkinter as ctk

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root.configure(fg_color="royal blue") 
root.geometry("400x600")
root.title("General Knowledge Quiz")

QuestionSet1 = [
    {"Q" : "Who created the company 'Apple'?",
    "A" : "steve jobs"},
    {"Q" : "Which 2 people co-founded the company 'Microsoft'?",
    "A" : "bill gates and paul allen"},
    {"Q" : "What is the competition in football/soccer in which nations compete for a golden trophy called?",
    "A" : "world cup"}
]

QuestionSet2 = [
    {"Q" : "Who created the company 'Apple'?",
    "A" : "steve jobs"},
    {"Q" : "Which 2 people co-founded the company 'Microsoft'?",
    "A" : "bill gates and paul allen"},
    {"Q" : "What is the competition in football/soccer in which nations compete for a golden trophy called?",
    "A" : "world cup"}
]

def CheckAns(Item, Answer):
    global Score
    if Answer.lower() == Item["A"].lower():
        Alerts = "Correct!"
        AlertsLbl.configure(text = Alerts, text_color = "forest green")
        Score += 1
    else:
        Alerts = f"Wrong! The answer is {Item['A']}"
        AlertsLbl.configure(text=Alerts, text_color="red")

def QuizAlgorithm(Qset):   
    random.shuffle(Qset)
    for Item in Qset:
        Question = Item["Q"]
        QuestionLbl.configure(text = Question)
        Answer = AnsEntry.get()
        CheckAns(Item, Answer)

def QuizEnd():
    if Length == "no":
        Screoutof = f"{Score} / {len(QuestionSet1)}"
    else:
        Screoutof = f"{Score} / {len(QuestionSet1) + len(QuestionSet2)}"

    QuestionLbl.configure(text="Game Complete!", text_color="green")
    QuestionLbl.after(1000, lambda: QuestionLbl.configure(text="Calculating Score...", text_color="green"))

    root.after(2500, lambda: QuestionLbl.configure(text=f"Your Score: {Screoutof}", text_color="green"))
    
    with open("Highscore.txt", "w") as f:
        f.write(str(Score))
    #print("Highscore Saved!")

Score = 0
Answer = ""
Length = "no"
Question = ""
Alerts = ""

QuestionLbl = ctk.CTkLabel(root, text = Question, font = ("Arial", 20, "bold"), text_color = "sea green")
AnsEntry = ctk.CTkEntry(root, placeholder_text = "Enter your answer here", font = ("Arial", 15))
AlertsLbl = ctk.CTkLabel(root, text = Alerts, font = ("Arial", 15), text_color = "red")

QuestionLbl.pack(pady = 20)
AnsEntry.pack(pady = 10)
AlertsLbl.pack(pady = 10)

root.mainloop()

QuizAlgorithm(QuestionSet1)
QuizAlgorithm(QuestionSet2)
QuizEnd()