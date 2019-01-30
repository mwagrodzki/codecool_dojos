import json
import sys

def loadFile():
    try:
        f = open('workfile', 'r')
    except FileNotFoundError:
        f = open('workfile', 'w')
        f.close()
        f = open('workfile', 'r')
    return f
def loadList():
    try:
        ideas = json.load(f)
    except json.decoder.JSONDecodeError:
        ideas = []
    return ideas

def addIdea(ideaList):
    idea = input("What is your new idea: ")
    ideaList.append(idea)
def printIdeas(ideaList):
    print()
    print("Your ideabank:")
    for i in range(len(ideaList)):
        print(str(i+1)+". "+ideaList[i])
def saveIdeas(ideaList, ideaFile):
    ideaFile.close()
    ideaFile = open('workfile', 'w')
    json.dump(ideaList, ideaFile)

def main():
    f = loadFile()
    ideas = loadList()

    if len(sys.argv) == 1:
        addIdea(ideas)
        printIdeas(ideas)
        saveIdeas(ideas, f)
    else:
        if sys.argv[1] == "--list":
            printIdeas(ideas)
        elif sys.argv[1] == "--delete":
            ideas.pop(int(sys.argv[2])-1)
            printIdeas(ideas)
            saveIdeas(ideas, f)

    f.close()

main()