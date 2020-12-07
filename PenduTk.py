
#Alexis PINCEMIN
#3/12/2020
#Jeu du Pendu version tkinter
#TO-DO : lettre déjà proposé première lettre apparait directement, affichage mimage , fix probleme checkletter recursif


from tkinter import Frame , Label , Canvas , Button , Entry , Tk , PhotoImage , StringVar
import random

# on choisi un mot
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


word, wordList, myWordList, letters,error = wordChoice()


def checkAlreadyUse(letters):  # vérifie si la letter est déjà utilisé
    global alreadyUse,letter
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
def checkLetter():

    letter = myLetter.get()

    myLetter.set('')
    letter = letter.lower()
    if not letter.isalpha() and letter != "":
        infoMessage.set('Lettre non valide')
        exec()
    else:
        return letter
def playAgain():
    global word,wordList,myWordList,letters,error
    word, wordList, myWordList, letters,error = wordChoice()
    infoMessage.set('Choisissez une lettre')
    alreadyUseLetters.set("Lettres déjà proposés : " +word[0])
    mainFunction()
    return word,wordList,myWordList,letters,error


def mainFunction():
    global letters,error,letter
    # on place ici la première letter
    wordToFind(letters)
    letter= checkLetter()
    alreadyUse, letter, letters = checkAlreadyUse(letters)
    # on parcours la liste contenant les letter du mot et on verifie si elles sont dans les letters utilisé
    wordToFind(letters)

    # si on écrit le mot directement on gagne ou on compare les deux listes celle du joueur et celle du mot défini au début
    if len(letter) > 1 and letter == word or myWordList == wordList:
        infoMessage.set('Vous avez gagné !')
    error = inscreaseError(error)
    displayCorp()

window = Tk()
window.title('Jeu du pendu')
width = 1250
height = 500

widthScreen = window.winfo_screenwidth()
hightScreen = window.winfo_screenheight()
x = (widthScreen // 2) - (width // 2)
y = (hightScreen// 2) - (height // 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.geometry()
window.resizable(width=False, height=False)
window.config(bg = '#3553B7')
leftFrame = Frame(window , bg = '#3553B7')
leftFrame.grid(row=1,column=0,padx = (20,250))
leftFrame1 = Frame(leftFrame)
leftFrame1.grid(row = 1,column = 0,padx = 20,pady=(150,0))
leftFrame2 = Frame(leftFrame,bg = '#3553B7')
leftFrame2.grid(row = 1,column = 1,pady=(150,0))

Canevas = Canvas(window, width=500, height=500, bg='#452569', highlightthickness=0)
Canevas.grid(row=1,column=1)
myLetter = StringVar()
letterEntry = Entry(leftFrame1,bg = 'white' , fg = '#000000' , font=('Helvetica', 10),textvariable = myLetter)
letterEntry.grid(row = 1 ,column = 0)
proposeButton = Button(leftFrame2,text = 'Proposer' , bg = 'white' , fg = '#3553B7' , font=('Helvetica', 10), command  = mainFunction)
proposeButton.grid(row = 1 ,column = 0)
hideWord = StringVar()
hideWord.set(wordToFind(letters))
researchWord = Label(leftFrame, textvariable=hideWord,font=('Helvetica', 45),bg="#86BFCD")
researchWord.grid(row = 0 ,columnspan = 2)
stayTry = StringVar()
stayTry.set('Il vous reste {} tentative(s)'.format(7))
remainTry = Label(leftFrame, textvariable=stayTry, fg = "#FF0000" ,bg ='#338AA0')
remainTry.grid(row = 4,columnspan = 2 , pady = (40,0))

infoMessage = StringVar()
infoMessage.set('Choisissez une lettre')
errorLabel = Label(leftFrame, textvariable=infoMessage)
errorLabel.grid(row = 2 ,columnspan = 2,pady = (10,30))
alreadyUseLetters = StringVar()
alreadyUseLetters.set("Lettres déjà proposés : " + letters[0])
useLetters = Label(leftFrame, textvariable=alreadyUseLetters)
useLetters.grid(row = 3 ,columnspan = 2,pady = (10,10))
newGameButton = Button(leftFrame2 , text = "Rejouer",command = playAgain)
newGameButton.grid(row = 1 , column = 1,padx = (40,0))
image1 = PhotoImage(master=window, file='image/mimage1.gif')
image2 = PhotoImage(master=window, file='image/mimage2.gif')
image3 = PhotoImage(master=window, file='image/mimage3.gif')
image4 = PhotoImage(master=window, file='image/mimage4.gif')
image5 = PhotoImage(master=window, file='image/mimage5.gif')
image6 = PhotoImage(master=window, file='image/mimage6.gif')
image7 = PhotoImage(master=window, file='image/mimage7.gif')
image8 = PhotoImage(master=window, file='image/mimage8.gif')
item = Canevas.create_image(250,250,image=image8)

window.mainloop()