#Alexis PINCEMIN
#30/11/2020
#Jeu du Pendu version console

import random

# varibales utiles
words = []
error = 0
wordList = []
myWordList = []

#but : on choisi un mot aleatoir et on crée les variables nécessaires
#sorties : word : mot choisi aléatoirement, wordList : liste des lettres de word ,
#myWordList : liste qui contient les lettres trouvés par le joueur utile pour détecter si le joueur à gagné
# letters : lettres déjà utilisé ici première lettre du mot, error : nombre d'erreur ici 0
def wordChoice():
    # varibales utiles
    words = []
    wordList = []
    myWordList = []
    error = 0
    # on ouvre le fichier contenant la liste de tout les mots / le fichier est dans le même répertoire que le code
    allWords = open("words.txt", "r")
    allWordsSort = sorted(allWords)
    allWords.close()
    # on créer un liste de tout les mots contenu dans le fichiers
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
    return word, wordList, myWordList, letters,error

word,wordList,myWordList,letters = wordChoice()

def checkAlreadyUse(letters): #vérifie si la letter est déjà utilisé

    alreadyUse = False
    if letter in letters:
        alreadyUse = True
        print('lettre déjà proposé')
    else:
        letters.append(letter)  # liste qui nous permet de stocker les letters utilisé
    return alreadyUse,letter,letters


def wordToFind(letters):
    for (index, i) in enumerate(word):
        if i in letters:
            myWordList[index] = i  # on complète au fur et à mesure la liste du joueur
            print(i, end=" ")
        else:
            print("_", end=" ")


def inscreaseError(error):
    global letter,alreadyUse
    if letter not in word and alreadyUse == False:
        error += 1
        print('Il vous reste {} tentative(s)'.format(8 - error))
        if error == 7:
            item = Canevas.create_image(150, 150, image=image1)
            print('Perdu ! Le mot qui fallait trouvé était {}'.format(word))
    return error

def displayCorp():
    global error
    if error == 6:
        item = Canevas.create_image(150, 150, image=image2)
    if error == 5:
        item = Canevas.create_image(150, 150, image=image3)
    if error == 4:
        item = Canevas.create_image(150, 150, image=image4)
    if error == 3:
        item = Canevas.create_image(150, 150, image=image5)
    if error == 2:
        item = Canevas.create_image(150, 150, image=image6)
    if error == 1:
        item = Canevas.create_image(150, 150, image=image7)
    if error == 0:
        item = Canevas.create_image(150, 150, image=image8)
        
        
def checkLetter():
    letter = input('Choisissez une lettre : ')
    letter = letter.lower()
    if not letter.isalpha(): #vérifie sur letter est une lettre de a-z
        print("Letter non valide.")
        return checkLetter()
    else:
        return letter

def mainFunction() :
    global letters,error
    # on place ici la première letter
    wordToFind(letters)
    letter = checkLetter()
    alreadyUse,letter,letters = checkAlreadyUse(letters)
    # on parcours la liste contenant les letter du mot et on verifie si elles sont dans les letters utilisé
    wordToFind(letters)

    # si on écrit le mot directement on gagne ou on compare les deux listes celle du joueur et celle du mot défini au début
    if len(letter) > 1 and letter == word or myWordList == wordList:
        print('Vous avez gagné !')
    error = inscreaseError(error)

