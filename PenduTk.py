from tkinter import *

window = Tk()
window.title('Jeu du pendu')
width = 800
height = 650

widthScreen = window.winfo_screenwidth()
hightScreen = window.winfo_screenheight()
x = (widthScreen // 2) - (width // 2)
y = (hightScreen// 2) - (height // 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.geometry()
window.config(bg = '#3553B7')
leftFrame = Frame(window ,width=400, height=650, bg = '#647099')

canvas = Canvas(window, width=400, height=650, bg='#452569', highlightthickness=0)
canvas.grid(row=0,column=1)
proposeButton = Button(leftFrame,text = 'Proposer' , bg = 'white' , fg = '#3553B7' , font=('Helvetica', 10))
researchWord = Label(leftFrame, text="test de mon label - - - -")
letterEntry = Entry(leftFrame,bg = 'white' , fg = '#000000' , font=('Helvetica', 10))
letterEntry.pack()
researchWord.pack()
leftFrame.grid(row=0,column=0,sticky =W)
proposeButton.pack()
window.mainloop()