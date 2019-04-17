from Tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Main Page")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width/2) - (700/2)
y_coord = (screen_height/2) - (750/2) - 50



root.resizable(False , False)


#FRAME
f1 = Frame(root, width = 700,height = 750,bg = 'darkgrey')
f1.pack()
root.resizable(False , False)
root.geometry('%dx%d+%d+%d' % (700, 750, x_coord, y_coord))



image = Image.open('HYU2.png')
image = image.resize((700, 750), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
w,h = image.size

colour = ('#{:02x}{:02x}{:02x}').format(int(195), int(195), int(195))

#CANVAS
c= Canvas(f1,width = 700 ,height = 750)
c.pack()
c.create_image(w//2,h//2,image=photo)
c.create_text(200,70,text = "HYUGEN'S\nPRINCIPLE",font = ('Bahnschrift SemiBold',40,'underline'),fill = 'black',justify = LEFT)
c.create_text(250,250,text = '''A)Every point on a wavefront behaves as \n  a point source of spherical secondary \n  waves.
\nB)Since they all start from the same \n  wavefront,they are all in phase.''',font = ('Bahnschrift SemiBold',17),fill = 'black',justify = LEFT)
c.create_text(220,420,text = '''i. At a given instant there is \n  constructive interference along the\n  common tangent to the spheres.
\nii. destructive interference occurs \n    everywhere else.''',font = ('Bahnschrift SemiBold',15),fill = 'darkblue',justify = LEFT)
c.create_text(230,530,text = "C)The tangent shows the next position \n  of the wavefront.",font = ('Bahnschrift SemiBold',17),fill = 'black',justify = LEFT)
def theory():
    global root
    root.destroy()
    execfile("Theory.py", globals())

def animation():
    global root
    root.destroy()
    execfile("SS_Animation1.py", globals())



#IMAGE
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)

backb = Image.open('left-arrow.png')
backb = backb.resize((70,70))
backbb = ImageTk.PhotoImage(backb)

#BUTTON
Button(root, image = nextbb,height=75,width=75,borderwidth = 0,bg = colour, activebackground = colour, command = animation).place(x= 350, y = 600)
Button(root, image=backbb,height=75, width = 75,borderwidth = 0,bg = colour, activebackground = colour, command = theory).place(x=20, y =600)


root.mainloop()
