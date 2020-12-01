from tkinter import *

window = Tk()
window.title('Jeu du pendu')
width = 1000
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
leftFrame1 = Frame(leftFrame)
leftFrame2 = Frame(leftFrame)


canvas = Canvas(window, width=500, height=500, bg='#452569', highlightthickness=0)
canvas.grid(row=1,column=1)
proposeButton = Button(leftFrame2,text = 'Proposer' , bg = 'white' , fg = '#3553B7' , font=('Helvetica', 10))
researchWord = Label(leftFrame, text="test de mon label - - - -")
remainTry = Label(leftFrame, text="il vous reste 8 essais", fg = "#FF0000" ,bg ='#338AA0')
letterEntry = Entry(leftFrame1,bg = 'white' , fg = '#000000' , font=('Helvetica', 10))
letterEntry.pack()
researchWord.grid(row = 0 ,columnspan = 2)
leftFrame.grid(row=1,column=0,padx = 128)
leftFrame1.grid(row = 1,column = 0,padx = 20,pady=(190,0))
leftFrame2.grid(row = 1,column = 1,pady=(190,0))
remainTry.grid(row = 2,columnspan = 2 , pady = (40,0))
proposeButton.pack()
window.mainloop()