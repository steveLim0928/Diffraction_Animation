from Tkinter import*
from PIL import Image,ImageTk
#import winsound

#winsound.PlaySound('Directed by Robert B. Weide.wav',winsound.SND_ASYNC|winsound.SND_LOOP)



root = Tk()
root.title("WELCOME!")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width/2) - (700/2)
y_coord = (screen_height/2) - (750/2) - 50


#FRAME
f1 = Frame(root, width = 700,height = 750,bg = 'skyblue')
f1.pack()
root.resizable(False , False)
root.geometry('%dx%d+%d+%d' % (700, 750, x_coord, y_coord))


image = Image.open('WMB.jpg')
image = image.resize((700, 750))
photo = ImageTk.PhotoImage(image)
w,h = image.size

#CANVAS
c= Canvas(f1,width = 700 ,height = 750)
c.pack()
c.create_image(w//2,h//2,image=photo)
c.create_text(350,50,text = "Welcome to this workshop!",font = ('Bahnschrift SemiBold',20),fill = 'darkblue',justify = CENTER)
c.create_text(350,200,text = "LIGHT\nDIFFRACTION",font = ('Bahnschrift SemiBold',70,'underline'),fill = 'black',justify = CENTER)
c.create_text(300,450,text = '''The topic that will be discussed in this \nworkshop is light diffraction!\n
We will be touching on single slit and \ndouble slit diffraction.\nHope you guys enjoy!''',font = ('Bahnschrift SemiBold',20),fill = 'white',justify = LEFT)
def mainpage():
    global root
    root.destroy()
    execfile("MainPage.py", globals())

def helpmessage():
    
    execfile("helpmessage2.py", globals())



#IMAGE
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)

helpb = Image.open('information.png')
helpb = helpb.resize((70,70))
helpbb = ImageTk.PhotoImage(helpb)

colour = ('#{:02x}{:02x}{:02x}').format(int(195), int(195), int(195))


#BUTTON
Button(root, image = nextbb,height=75,width=75,borderwidth = 0,bg = colour, activebackground = colour, command = mainpage).place(x= 600, y = 600)
Button(root, image=helpbb,height=75, width = 75,borderwidth = 0,bg = colour, activebackground = colour, command = helpmessage).place(x=20, y =600)

root.mainloop()
