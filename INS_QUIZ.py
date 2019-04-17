
from Tkinter import*
from PIL import Image,ImageTk


root = Tk()
root.title("INSRUCTION!")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width/2) - (700/2)
y_coord = (screen_height/2) - (750/2) - 50
#CANVAS
c= Canvas(root,width = 700 ,height = 750).place(x= x_coord, y = y_coord)


#FRAME
f1 = Frame(root, width = 700,height = 750,bg = 'grey').pack()
root.resizable(False , False)
root.geometry('%dx%d+%d+%d' % (700, 750, x_coord, y_coord))

def mainpage():
    global root
    root.destroy()
    execfile("MainPage.py", globals())

def quiz():
    global root
    root.destroy()
    execfile("DiffQuiz.py", globals())
#IMAGE
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)

backb = Image.open('left-arrow.png')
backb = backb.resize((75,75))
backbb = ImageTk.PhotoImage(backb)

#LABEL
text1 = Label(root, text = 'INSTRUCTION FOR QUIZ', font =('Bahnschrift SemiBold',30,'underline'), bg = 'grey')
text1.place(x = 700/2 - 220, y = 50)
text2 = Label(root, text = '''1)This quiz contains 10 questions.\n
2)The time limit fot this quiz is 10 minutes.\n
3)This quiz cannot be stop once started.\n
4)Once you selected your answer, you will straight away be directed to the next
  question.\n
5)Once you selected your answer, you cannot go back to the previous question
  anymore.\n
7)Once the time is up, the quiz will stop automatically.\n
8)Any unanswered question will be considered as wrong.\n''',font = ('Bahnschrift SemiBold',15),bg = 'grey',justify= LEFT)
text2.place(x= 700/2-350,y=125)

text3= Label(root, text ="(CLICK THIS ARROW TO GO BACK)", font =('Bahnschrift SemiBold',10),fg='red',bg ='grey')
text3.place(x =10 , y =570)

text4= Label(root, text ="(CLICK THIS ARROW FOR QUIZ)", font =('Bahnschrift SemiBold',10),fg='red',bg ='grey')
text4.place(x =510 , y =570)

text5= Label(root, text = "GOOD LUCK!",font =('Bahnschrift SemiBold',30,'bold'), fg = 'dark blue',bg ='grey')
text5.place(x= 240,y=500)



#BUTTON
Button(root, image = nextbb,height=75,width=75,borderwidth = 0,bg = 'grey', activebackground = 'grey',command = quiz).place(x= 600, y = 600)
Button(root, image=backbb,height=75, width = 75,borderwidth = 0,bg = 'grey', activebackground = 'grey', command = mainpage).place(x=20, y =600)

root.mainloop()

