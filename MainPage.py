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
f1 = Frame(root, width = 700,height = 750,bg = 'skyblue')
f1.pack()
root.resizable(False , False)
root.geometry('%dx%d+%d+%d' % (700, 750, x_coord, y_coord))



image = Image.open('MPBG.jpg')
image = image.resize((700, 750), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
w,h = image.size

#CANVAS
c= Canvas(f1,width = 700 ,height = 750)
c.pack()
c.create_image(w//2,h//2,image=photo)
c.create_text(350,180,text = "LIGHT\nDIFFRACTION",font = ('Bahnschrift SemiBold',70,'underline'),fill = 'white',justify = CENTER)

def back():
    global root
    root.destroy()
    
    execfile('welcomemessage.py',globals())
def quiz_ins():
    global root
    root.destroy()
    
    execfile('INS_QUIZ.py',globals())
def helpB():
    
    execfile('helpmessage1.py',globals())
def theory():
    global root
    root.destroy()
    
    execfile('Theory.py',globals())
def theory2():
    global root
    root.destroy()

    execfile('theory2.py',globals())
  

#IMAGE
backb = Image.open('left-arrow.png')
backb = backb.resize((75,75))
backbb = ImageTk.PhotoImage(backb)


helpb = Image.open('information.png')
helpb = helpb.resize((70,70))
helpbb = ImageTk.PhotoImage(helpb)

#BUTTON
Button(root, image=backbb,height=75, width = 75,borderwidth=0,bg='black',activebackground='black',command = back).place(x=30,y=610)

Button(root, image=helpbb,height=75, width=75,borderwidth=0,bg='black',activebackground='black',command = helpB).place(x= 600,y=600)
Button(root, text="Quiz",font=('Bahnschrift'),height=3, width=20, borderwidth=5, command = quiz_ins).place(x= 230,y = 550)
Button(root, text="Single Slit",font=('Bahnschrift'),height=3,width=20,borderwidth = 5, command = theory).place(x=230,y=350)
Button(root, text="Double Slit",font=('Bahnschrift'),height=3,width=20,borderwidth=5, command = theory2).place(x=230,y=450)

root.mainloop()

