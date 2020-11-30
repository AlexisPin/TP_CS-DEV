
#Alexis PINCEMIN
#30/11/2020
#Jeu du Pendu version console

import random
#on ouvre le fichier contenant la liste de tout les mots / le fichier est dans le même répertoire que le code
allWords = open("words.txt" , "r" )

allWordsSort = sorted(allWords)
#varibales utiles
words = []

error = 0
wordList = []
myWordList = []
bodyItems = ['O','/','|','\\','/','\\','','']
myBody = ['','','','','','','','']

#on créer un liste de tout les mots contenu dans le fichiers
for oneWord in allWordsSort:
    words.append(oneWord.rstrip('\n'))
#on choisi un mot aléatoirement
word = random.choice(words)

#on créer une liste avec les lettres du mot choisi aléatoirement
for x in word:
    wordList.append(x)
#on donne déjà la première lettre
letters = [wordList[0]]
#on créer une liste vide de la longueur de word qui sert à afficher le mot au fur et à mesure qu'on trouve les lettres
for x in word:
    myWordList.append("")


while error < 8 :

    print(' \n -----')
    print(' |   |')
    print(' |   {}' .format(myBody[0]))
    print(' |  {}{}{}'.format(myBody[1],myBody[2],myBody[3]))
    print(' |  {} {}'.format(myBody[4], myBody[5]))
    print('_|_')

    # on parcours la liste contenant les lettre du mot et on verifie si elles sont dans les lettres utilisé
    for (index, i) in enumerate(word):
        if i in letters:
            myWordList[index] = i  # on complète au fur et à mesure la liste du joueur
            print(i, end=" ")
        else:
            print("_", end=" ")

    letter = input('Choisissez une lettre : ')
    #vérifie si la lettre est déjà utilisé
    alreadyUse = False
    if letter in letters:
        alreadyUse = True
        print('Lettre déjà proposé')
    else:
        letters.append(letter)  # liste qui nous permet de stocker les lettres utilisé


    # si on écrit le mot directement on gagne
    if len(letter) > 1 and letter == word:
        print('Vous avez gagné !')
        break

#on compare les deux listes celle du joueur et celle du mot défini au début
    if myWordList == wordList:
        print('Vous avez gagné !')
        break


    if letter not in word and alreadyUse == False:
        error += 1
        myBody[error-1] = bodyItems[error-1]
        print('Il vous reste {} tentative(s)' .format(8 - error))
        if error ==8:
            print('Perdu ! Le mot qui fallait trouvé était {}' .format(word))


allWords.close()


