import random

questions = ["Are you at least 14 y.o.?", "Do you want to use sauna?", "Are you a student?", "Are you a man?"]
jokes = ["What’s the best thing about Switzerland? \n I don’t know, but the flag is a big plus.", 
        "I invented a new word! \n Plagiarism!", 
        "Did you hear about the mathematician who’s afraid of negative numbers? \n He’ll stop at nothing to avoid them.",
        "Why do we tell actors to “break a leg?” \n Because every play has a cast."]

def tellJoke():
    print(" ")
    print(jokes[random.randrange(0,len(jokes)-1)])
    print(" ")

def answer2(index):
    while True:
        ans = input(questions[index]+" (Yes/No) ")
        if ans == 'Yes' or ans == 'No':
            break
    if index == 0:
        if ans == 'Yes':
            return True
        elif ans == "No":
            print("You can't join the gym")
            return False
    if index == 1:
        if ans == 'Yes':
            print("The price is 1500PLN")
            return False
        elif ans == "No":
            return True
    if index == 2:
        if ans == 'Yes':
            print("The price is 300PLN")
            return False
        elif ans == "No":
            return True
    if index == 3:
        if ans == 'Yes':
            print("The price is 750PLN")
            return False
        elif ans == "No":
            print("The price is 500PLN")
            return False

for i in range(len(questions)):
    if answer2(i):
        tellJoke()
    else:
        break