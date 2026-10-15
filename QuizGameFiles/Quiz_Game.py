import random
import customtkinter as Ctk
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
        print("Correct!")
        Score += 1
    else:
        print(f"Wrong! The answer is {Item["A"]}")

def QuizAlgorithm(Qset):   
    random.shuffle(Qset)
    
    for Item in Qset:
        print(Item["Q"])
        Answer = input("Your answer: ")
        CheckAns(Item, Answer)

def QuizEnd():
    if Length == "no":
        Screoutof = f"{Score} / {len(QuestionSet1)}"
    else:
        Screoutof = f"{Score} / {len(QuestionSet1) + len(QuestionSet2)}"
    
    print("Game Complete!")
    print(f"Your Score: {Screoutof}")
    
    with open("Highscore.txt", "w") as f:
        f.write(str(Score))
    print("Highscore Saved!")

Score = 0
Answer = ""
Length = "no"

QuizAlgorithm(QuestionSet1)

if Score <= 3 and Score >= 2:
    Length = "yes"
    print("----- NEXT ROUND -----")
    QuizAlgorithm(QuestionSet2)
QuizEnd()