
import Tkinter as tk


from numpy import arange, sin, pi,cos 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure



def SS_Graph1 (canvas, a, z, colour):
    

    Fs = 5000#rate
    fr = 5 #frequency  
    sample = -5000
    x = arange(sample)
    y = cos(2*pi*fr*x/Fs)
    
    
    
        
    x0 = arange(-5,50)#55
    def smallamplitude1(x):
        Fs = 275
        y = -0.02*(cos(2*pi*fr*(x-(-5))/Fs))
        a.plot(y+0.02,x0,color=colour)
        a.set_title('Single Slit Diffraction')
        a.set_ylim(-10,360) 
        a.set_xlim(-0.004,0.7)
        a.axis('off')
    smallamplitude1(x0)


    x1 = arange(50,111)#60
    def smallamplitude1(x):
        Fs = 300
        y = -0.07*(cos(2*pi*fr*(x-50)/Fs))
        a.plot(y+0.07,x1,color=colour)
    smallamplitude1(x1)


    x2 = arange(110,241)#130
    def smallamplitude1(x):
        Fs = 650
        y = -0.3*(cos(2*pi*fr*(x-(110))/Fs))
        a.plot(y+0.3,x2,color=colour )
    smallamplitude1(x2) 

    x4 = arange(240,301)#60
    def smallamplitude1(x):
        Fs = 300
        y = -0.07*(cos(2*pi*fr*(x-240)/Fs)) 
        a.plot(y+0.07,x4,color=colour)
    smallamplitude1(x4)

    x5 = arange(300,356)#55
    def smallamplitude1(x):
        Fs = 275
        y = -0.02*(cos(2*pi*fr*(x-(300))/Fs))
        a.plot(y+0.02,x5,color=colour)
    smallamplitude1(x5)           
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



