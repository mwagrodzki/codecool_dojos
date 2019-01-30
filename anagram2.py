with open('anagrams.csv') as f:
    read_data = f.readlines()
f.closed

wordList = []
anagrams = {}

for data in read_data:
    data = data.replace('\n', '')
    key = ''.join(sorted(data))
    if key not in anagrams.keys():
        anagrams[key] = []
    anagrams[key].append(data)

for anagram in anagrams.keys():
    print(anagram + ": " +
          str(anagrams[anagram]).replace('[', '').replace(']', ''))
