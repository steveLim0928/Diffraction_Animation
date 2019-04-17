
from Tkinter import*
from PIL import Image,ImageTk
root = Tk()
root.title("Theory")
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



#LABEL
text1 = Label(root, text = 'THEORY AND EQUATION', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
text1.place(x = 700/2 - 280, y = 50)

text1 = Label(root, text = 'SINGLE SLIT DIFFRACTION',fg = 'darkblue', font =('Bahnschrift SemiBold',25,'bold'), bg = 'grey')
text1.place(x = 700/2 - 280, y = 100)


text3 = Label(root, text = '''A)Happens when a wave pass through single slit.\n
B)Happens due to Hyugen’s Principle which states that every point on a
wave front may be regarded as a source of secondary spherical waves
which spread out with the wave velocity.\n
C)The central bright fringe is called the central or principal maximum,
while the lower ones on each side are called secondary or subsidiary \nmaxima.\n
D)A single slit produces an interference pattern
characterized by a broad central maximum with narrower
and dimmer maxima to the sides.\n
E)There is destructive interference for a single slit when D Sin θ  = mλ,
(for m = 1,-1,2,-2,3,.......),where D is the slit width, λ is the light’s wavelength,
θ is the angle relative to the original direction of the light, m is the order of
the minimum.(Note that there is no m=0 minimum)''',
font = ('Bahnschrift SemiBold',15),bg = 'grey',justify= LEFT)
text3.place(x=700/2 -320, y = 150)

text4 = Label(root,text = '''(Proceed to next slide to learn more about Hyugen's Principle)''',fg = 'darkblue', font =('Bahnschrift SemiBold',13),bg = 'grey')
text4.place(x = 110, y = 620)

def home():
    global root
    root.destroy()
    execfile('MainPage.py',globals())

def hyugen():
    global root
    root.destroy()
    execfile('HP.py',globals())


#IMAGE
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)

helpb = Image.open('information.png')
helpb = helpb.resize((70,70))
helpbb = ImageTk.PhotoImage(helpb)

backb = Image.open('left-arrow.png')
backb = backb.resize((75,75))
backbb = ImageTk.PhotoImage(backb)

Button(root,image=nextbb,height=75,width=75,borderwidth=0,bg='grey',activebackground='grey',command = hyugen).place(x=600,y=600)

Button(root,image=backbb,height=75,width = 75,borderwidth = 0,bg='grey',activebackground='grey',command = home).place(x=20,y=600)

root.mainloop()
