
with open('anagrams.csv') as f:
    read_data = f.readlines()
f.closed

dataList = []
anagramList = []
temporary = []

counter = 0
for data in read_data:
    data = data.replace('\n', '')
    dataList.append(data)
    anagramList.append(''.join(sorted(data)))
    temporary.append(counter)
    counter += 1


for i in range(len(dataList)):
    if temporary.count(i) != 0:
        words = ''
        anagram = anagramList[i]
        for j in range(len(anagramList)):
            if temporary.count(j) != 0:
                if anagram == anagramList[j]:
                    words = words + " " + dataList[j]
                    temporary.remove(j)
        print(words)
