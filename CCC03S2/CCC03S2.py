def checkRhyme(string1, string2):

    string1 = string1[::-1]
    string2 = string2[::-1]
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()
  
    if string1 == string2:
        return True
    vowels = ["a", "e", "i", "o", "u"]
    vowelIndex1 = len(string1)
    vowelIndex2 = len(string2)
    for i in vowels:
        if string1.find(i) < vowelIndex1 and string1.find(i) !=-1:
            vowelIndex1 = string1.find(i)

        if string2.find(i) < vowelIndex2 and string2.find(i) !=-1:
            vowelIndex2 = string2.find(i)


    if string1[:vowelIndex1+1] == string2[:vowelIndex2+1]:
        return True
    else:
        return False

def checkLines(verse):

    if checkRhyme(verse[0],verse[1]) and checkRhyme(verse[0], verse[3]) and checkRhyme(verse[0], verse[2]):
        return "perfect"
    elif checkRhyme(verse[0],verse[1]) and checkRhyme(verse[2], verse[3]):
        return "even"
    elif checkRhyme(verse[0], verse[2]) and checkRhyme(verse[1], verse[3]):
        return "cross"
    elif checkRhyme(verse[0], verse[3]) and checkRhyme(verse[1], verse[2]):
        return "shell"
    else:
        return "free"


numVerse = int(input())
lines = []
wordlist = []
i = 1
while i<= numVerse*4:
    linewordlist = input().split()
    wordlist.append(linewordlist[-1])
    if i%4 == 0 and i!=0:
        print(checkLines(wordlist))
        wordlist.clear()
    i+=1