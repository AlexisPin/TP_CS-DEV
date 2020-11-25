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
bodyItems = ['O','/','|','\\','/','\\','']
myBody = ['','','','','','','']
for x in word:
    wordList.append(x)

for x in word:
    myWordList.append("")

while error < 7 :
    alreadyUse = False
    print(' \n -----')
    print(' |   |')
    print(' |   {}' .format(myBody[0]))
    print(' |  {}{}{}'.format(myBody[1],myBody[2],myBody[3]))
    print(' |  {} {}'.format(myBody[4], myBody[5]))
    print('_|_')
    letter = input('Choisissez une lettre : ')
    if letter in letters:
        alreadyUse = True
        print('Letrre déjà proposé')
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

    if letter not in word and alreadyUse == False:
        error += 1
        myBody[error-1] = bodyItems[error-1]
        print('Il vous reste {} tentative(s)' .format(7 - error))
        if error ==7:
            print('Perdu ! Le mot qui fallait trouvé était {}' .format(word))





