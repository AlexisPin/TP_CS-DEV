
#Alexis PINCEMIN
#7/12/2020
#Jeu du Pendu version tkinter
#Lien gitbub https://github.com/AlexisPin/TP_CS-DEV
from tkinter import Frame , Label , Canvas , Button , Entry , Tk , PhotoImage , StringVar , Menu
import random
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
    return word, wordList, myWordList, letters, error

word, wordList, myWordList, letters, error = wordChoice()


# but : vérifie si la letter est déjà utilisé,
# entrée : letters : liste des lettres utilisés,
# sorties : alreadyUse : varibales booléenne, letter : lettre choisie , letters : liste des lettres utilisés
def checkAlreadyUse(letters):
    global alreadyUse, letter
    alreadyUse = False
    if letter in letters:
        alreadyUse = True
        infoMessage.set('lettre déjà proposé')

    elif letter != "":
        letters.append(letter)  # liste qui nous permet de stocker les letters utilisé
        proposeLetter = ""
        for i in letters:
            proposeLetter += " "+i+","
            alreadyUseLetters.set("Lettres déjà proposés :" + proposeLetter)

    if letter in word and letter not in letters[:-1] and letter != "":
        infoMessage.set("Bien joué le {} est correct" .format(letter))

    return alreadyUse, letter, letters


# but : afficher le mot en cours de recherche,
# entrée : letters : liste des lettres utilisés,
# sorties : inResearchWord : mot en cours de recherche type str
def wordToFind(letters):
    inResearchWord = ""
    for (index, i) in enumerate(word):
        if i in letters:
            myWordList[index] = i  # on complète au fur et à mesure la liste du joueur
            inResearchWord += i

        else:
            inResearchWord += " _"
    hideWord.set(inResearchWord)
    return inResearchWord

# but : gérer le nombre d'erreur du joueur,
# entrée : error : nombre d'erreur type : entier,
# sorties : error : nombre d'erreur type : entier,
def inscreaseError(error):
    global letter, alreadyUse
    if letter not in word and alreadyUse == False and letter != "":
        infoMessage.set("Dommage la lettre {} n'est pas dans le mot" .format(letter))
        error += 1
        stayTry.set('Il vous reste {} tentative(s)'.format(7 - error))
        if error == 7:
            item = Canevas.create_image(250, 250, image=image1)
            stayTry.set('Perdu ! Le mot qui fallait trouvé était {}'.format(word))
    if letter == "":
        stayTry.set('Il vous reste {} tentative(s)'.format(7 - error))

    return error

#but : afficher les éléments du pendu en fonction du nombre d'erreur
def displayCorp():
    if error == 6:
        item = Canevas.create_image(250, 250, image=image2)
    if error == 5:
        item = Canevas.create_image(250, 250, image=image3)
    if error == 4:
        item = Canevas.create_image(250, 250, image=image4)
    if error == 3:
        item = Canevas.create_image(250, 250, image=image5)
    if error == 2:
        item = Canevas.create_image(250, 250, image=image6)
    if error == 1:
        item = Canevas.create_image(250, 250, image=image7)
    if error == 0:
        item = Canevas.create_image(250, 250, image=image8)

#but : vérifier la validité de la lettre
#sortie : letter : lettre choisie par le joueur type str
def checkLetter():
    letter = myLetter.get()
    myLetter.set('')
    letter = letter.lower()
    #si la lettre n'est dans l'alphabet
    if not letter.isalpha() and letter != "":
        infoMessage.set('Lettre non valide')
        return -1
    else:
        return letter


#but : fonction pour rejouer qui appel la fonction de choix du mot
#sorties : word : mot choisi aléatoirement, wordList : liste des lettres de word ,
# letters : lettres déjà utilisé ici première lettre du mot, error : nombre d'erreur ici 0
def playAgain():
    global word, wordList, myWordList, letters, error
    word, wordList, myWordList, letters, error = wordChoice()
    infoMessage.set('Choisissez une lettre')
    alreadyUseLetters.set("Lettres déjà proposés : " + word[0])
    mainFunction()
    return word, wordList, myWordList, letters, error

#but afficher le score en fin de partie
def votreScore(error):
    if error > 0:
        valueScore.set('Votre score est de {}' .format(7-error))
    else:
        valueScore.set('Votre score est de 0')


#fonction principal qui appel chaque fonction dans l'ordre
def mainFunction():
    global letters, error, letter
    if 7-error == 0:
        return
    # on place ici la première letter
    wordToFind(letters)
    letter = checkLetter()
    if letter == -1:
        return
    alreadyUse, letter, letters = checkAlreadyUse(letters)
    # on parcours la liste contenant les letter du mot et on verifie si elles sont dans les letters utilisé
    wordToFind(letters)

    # si on écrit le mot directement on gagne ou on compare les deux listes celle du joueur et celle du mot défini au début
    if len(letter) > 1 and letter == word or myWordList == wordList:
        letters = wordList
        wordToFind(letters)
        votreScore(error)
        infoMessage.set('Vous avez gagné !')
    error = inscreaseError(error)
    displayCorp()


window = Tk()
window.title('Jeu du pendu')
width = 1200
height = 500
#on centre la fenêtre sur l'écran
widthScreen = window.winfo_screenwidth()
heightScreen = window.winfo_screenheight()
x = (widthScreen // 2) - (width // 2)
y = (heightScreen // 2) - (height // 2)
window.geometry('{}x{}+{}+{}' .format(width, height, x, y))
window.resizable(width=False, height=False)
window.config(bg='#2D9484')

leftFrame = Frame(window, bg='#9C4044')
leftFrame.grid(row=1, column=0, padx=(20, 250))

leftFrame1 = Frame(leftFrame)
leftFrame1.grid(row=1, column=0, padx=20,pady=(150, 0))

leftFrame2 = Frame(leftFrame, bg='#9C4044')
leftFrame2.grid(row=1, column=1, pady=(150, 0))

Canevas = Canvas(window, width=500, height=500, bg='#452569', highlightthickness=0)
Canevas.grid(row=1, column=1)

myLetter = StringVar()
letterEntry = Entry(leftFrame1,bg='white', fg='#000000', font=('Helvetica', 10), textvariable=myLetter)
letterEntry.grid(row=1, column=0)

proposeButton = Button(leftFrame2, text='Proposer', bg='white', fg='#3553B7', font=('Helvetica', 10), command=mainFunction)
proposeButton.grid(row=1, column=0)

#Label qui affiche le mot recherché
hideWord = StringVar()
hideWord.set(wordToFind(letters))
researchWord = Label(leftFrame, textvariable=hideWord, font=('Helvetica', 45), bg="#86BFCD")
researchWord.grid(row=0, columnspan=2)

#Label qui indique les nombre de tantatives restantes
stayTry = StringVar()
stayTry.set('Il vous reste {} tentative(s)'.format(7))
remainTry = Label(leftFrame, textvariable=stayTry, fg="#338AA0", bg='#000000')
remainTry.grid(row=4, columnspan=2, pady=(40, 0))

#Label pour afficher des informations sur la partie
infoMessage = StringVar()
infoMessage.set('Choisissez une lettre')
infoLabel = Label(leftFrame, textvariable=infoMessage)
infoLabel.grid(row=2, columnspan=2, pady=(10, 30))

#Label pour afficher les lettres utilisés
alreadyUseLetters = StringVar()
alreadyUseLetters.set("Lettres déjà proposés : " + letters[0])
useLetters = Label(leftFrame, textvariable=alreadyUseLetters)
useLetters.grid(row=3, columnspan=2, pady=(10, 10))

newGameButton = Button(leftFrame2, text="Rejouer", command=playAgain)
newGameButton.grid(row=1, column=1, padx=(50, 0))

valueScore = StringVar()
scoreMax = Label(leftFrame, textvariable=valueScore, bg='#9C4044', fg='#0046FF')
scoreMax.grid(row=6, columnspan=2, pady=(10, 0))
#on importe toutes les images
image1 = PhotoImage(master=window, file='image/mimage1.gif')
image2 = PhotoImage(master=window, file='image/mimage2.gif')
image3 = PhotoImage(master=window, file='image/mimage3.gif')
image4 = PhotoImage(master=window, file='image/mimage4.gif')
image5 = PhotoImage(master=window, file='image/mimage5.gif')
image6 = PhotoImage(master=window, file='image/mimage6.gif')
image7 = PhotoImage(master=window, file='image/mimage7.gif')
image8 = PhotoImage(master=window, file='image/mimage8.gif')

#initialisation du canvas avec une image vide
item = Canevas.create_image(250, 250, image=image8)

menuBar = Menu(window)
menuFile = Menu(menuBar, tearoff=0)
menuFile.add_command(label="Rejouer", command=playAgain)
menuFile.add_command(label="Quitter", command=window.quit)
menuBar.add_cascade(label="Fenêtre", menu=menuFile)
window.config(menu=menuBar)

window.mainloop()
