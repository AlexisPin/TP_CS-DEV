
#Alexis PINCEMIN
#30/11/2020
#Jeu du Pendu version console
#Lien gitbub https://github.com/AlexisPin/TP_CS-DEV

import random
#on ouvre le fichier contenant la liste de tout les mots / le fichier est dans le même répertoire que le code

continuer_partie = True
while continuer_partie:
    # varibales utiles
    words = []
    error = 0
    wordList = []
    myWordList = []
    bodyItems = [' \n -----','|','O', ' /', '|', '\\', '/', '\\']
    myBody = ['', '', '', '', '', '', '', '']


    # but : on choisi un mot aleatoire et on crée les variables nécessaires
    # sorties : word : mot choisi aléatoirement, wordList : liste des lettres de word ,
    # myWordList : liste qui contient les lettres trouvés par le joueur utile pour détecter si le joueur à gagné
    # letters : lettres déjà utilisé ici première lettre du mot
    def wordChoice() :
        allWords = open("words.txt", "r")
        allWordsSort = sorted(allWords)
        allWords.close()
        for oneWord in allWordsSort:
            words.append(oneWord.rstrip('\n'))
        word = random.choice(words)
        # on créer une liste avec les letters du mot choisi aléatoirement
        for x in word:
            wordList.append(x)
        # on donne déjà la première letter
        letters = [wordList[0]]
        # on créer une liste vide de la longueur de word qui sert à afficher le mot au fur et à mesure qu'on trouve les letters
        for _ in word:
            myWordList.append("")
        return word,wordList,myWordList,letters

    word,wordList,myWordList,letters = wordChoice()


    # but : vérifie si la letter est déjà utilisé,
    # entrée : letters : liste des lettres utilisés,
    # sorties : alreadyUse : varibales booléenne, letter : lettre choisie , letters : liste des lettres utilisés
    def checkAlreadyUse(letters): #vérifie si la letter est déjà utilisé

        alreadyUse = False
        if letter in letters:
            alreadyUse = True
            print('lettre déjà proposé')
        else:
            letters.append(letter)  # liste qui nous permet de stocker les letters utilisé
        return alreadyUse,letter,letters

    # but : afficher le mot en cours de recherche,
    # entrée : letters : liste des lettres utilisés,
    def wordToFind(letters):
        for (index, i) in enumerate(word):
            if i in letters:
                myWordList[index] = i  # on complète au fur et à mesure la liste du joueur
                print(i, end=" ")
            else:
                print("_", end=" ")


    # but : gérer le nombre d'erreur du joueur,
    # entrée : error : nombre d'erreur type : entier,
    # sorties : error : nombre d'erreur type : entier,
    def inscreaseError(error):
        if letter not in word and alreadyUse == False:
            myBody[error] = bodyItems[error]
            error += 1
            print('Il vous reste {} tentative(s)'.format(8 - error))
            if error == 8:
                print(' \n -----')
                print(' |   |')
                print(' |   O')
                print(' |  /|\\')
                print(' |  / \\')
                print('_|_')
                print('Perdu ! Le mot qui fallait trouvé était {}'.format(word))
        return error


    # but : vérifier la validité de la lettre
    # sortie : letter : lettre choisie par le joueur type str
    def checkLetter():
        letter = input('Choisissez une lettre : ')
        letter = letter.lower()
        if not letter.isalpha(): #vérifie sur letter est une lettre de a-z
            print("Letter non valide.")
            return checkLetter()
        else:
            return letter


    while error < 8:
        print('{}'.format(myBody[0]))
        print(' |   {}'.format(myBody[1]))
        print(' |   {}'.format(myBody[2]))
        print(' | {}{}{}'.format(myBody[3], myBody[4], myBody[5]))
        print(' |  {} {}'.format(myBody[6], myBody[7]))
        print('_|_')
        # on place ici la première letter
        wordToFind(letters)
        letter = checkLetter()
        alreadyUse,letter,letters = checkAlreadyUse(letters)
        # on parcours la liste contenant les letter du mot et on verifie si elles sont dans les letters utilisé
        wordToFind(letters)

        # si on écrit le mot directement on gagne ou on compare les deux listes celle du joueur et celle du mot défini au début
        if len(letter) > 1 and letter == word or myWordList == wordList:
            print('Vous avez gagné !')
            break
        error = inscreaseError(error)

    quitter = input("Souhaitez-vous quitter le jeu (o/n) ? ")
    if quitter == "o" or quitter == "O":
        print("Vous avez quittez le jeu.")
        continuer_partie = False
    else :
        continuer_partie = True



