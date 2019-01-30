import sys

exceptionList = ['be', 'see', 'flee', 'knee']
vowels = 'aeiouy'
wordList = sys.argv[1:]

for word in wordList:
    length = len(word)
    ending = word[-3:]
    
    if word.endswith('ie'): # die, lie, tie, vie
        word = word[:-2] +"ying"
    elif word.endswith('e') and not word in exceptionList: #become, have, bake, smile
        word = word[:-1] +"ing"
    elif ending[0] not in vowels and ending[1] in vowels and ending[2] not in vowels: #begin, stop, open
        word += word[length-1:] + "ing"
    else: 
        word += "ing"

    print(word)