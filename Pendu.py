import random

allWords = open("words.txt" , "r" )

words = []
letters = []
for oneWord in allWords:
    words.append(oneWord.rstrip('\n'))
word = random.choice(words)

error = 0
wordList = []
myWordList = []
for x in word:
    wordList.append(x)

for x in word:
    myWordList.append("")

while error < 8 :
    letter = input('Choisissez une lettre : ')
    letters.append(letter)
    if len(letter) > 1 and letter == word:
        print('Vous avez gagné !')
        break

    for (index, i) in enumerate(word):
        if i in letters:
            myWordList[index] = i
            print(i, end=" ")
        else:
            print("_", end=" ")
            letterInWord = False

    if myWordList == wordList:
        print('Vous avez gagné !')
        break

    if letter not in word:
        error += 1
        print('Il vous reste {} tentative(s)' .format(8 - error))
        if error ==8:
            print('Perdu ! Le mot qui fallait trouvé était {}' .format(word))





