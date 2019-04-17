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

text1 = Label(root, text = 'DOUBLE SLIT DIFFRACTION', font =('Bahnschrift SemiBold',25,'bold'), fg = 'dark blue',bg = 'grey')
text1.place(x = 700/2 - 280, y = 100)


text3 = Label(root, text = '''A)Young’s double slit experiment gave definitive proof of the wave
character of light.\n
B)An interference pattern is obtained by the superposition of light from
two slits.\n
C)There is constructive interference when d sinθ = mλ, where d is the
distance between the slits,θ is the angle relative to the incident direction,
and m is the order of the interference.\n
D)There is destructive interference when d sinθ = (m + 1/2) λ
(for m = 0, 1, -1, 2, -2,...)\n
E)The number of fringes depends on the wavelength and slit separation. The
number of fringes will be very large for large slit separations. However, if
the slit separation becomes much greater than the wavelength, the intensity
of the interference pattern changes so that the screen has two bright lines
cast by the slits, as expected when light behaves like a ray. We also note that
the fringes get fainter further away from the center. ''',
font = ('Bahnschrift SemiBold',15),bg = 'grey',justify= LEFT)
text3.place(x=700/2 -320, y = 150)

def home():
    global root
    root.destroy()
    execfile('MainPage.py',globals())

def animation():
    global root
    root.destroy()
    execfile('DS_Animation1.py',globals())

#IMAGE
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)



backb = Image.open('left-arrow.png')
backb = backb.resize((75,75))
backbb = ImageTk.PhotoImage(backb)



Button(root,image=nextbb,height=75,width=75,borderwidth=0,bg='grey',activebackground='grey', command = animation).place(x=600,y=620)

Button(root,image=backbb,height=75,width = 75,borderwidth = 0,bg='grey',activebackground='grey',command = home).place(x=20,y=620)

root.mainloop()

