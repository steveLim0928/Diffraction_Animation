import Tkinter as tk

from numpy import arange, cos, pi
def DS_Graph1 (canvas, a, z, colour):

    fr = 5 #frequency

    x5 = arange(0,71)#70
    def smallamplitude1(x):
        Fs = 350
        y = -0.8*cos(2*pi*fr*(x)/Fs)
        a.plot(y+0.8,x5,color=colour)
        a.set_title('Double Slit Diffraction')
        a.set_ylim(-5,394)
        a.set_xlim(-0.04,8)
        a.axis('off')
    smallamplitude1(x5)

    x6 = arange(70,151)#80
    def smallamplitude1(x):
        Fs = 400
        y = -2.5*(cos(2*pi*fr*(x-(70))/Fs))
        a.plot(y+2.5,x6,color=colour)
    smallamplitude1(x6)

    x7 = arange(150,241)#90
    def smallamplitude1(x):
        Fs= 450
        y = -4*(cos(2*pi*fr*(x-(150))/Fs))
        a.plot(y+4,x7,color=colour)
    smallamplitude1(x7)

    x8 = arange(240,321)#80
    def smallamplitude1(x):
        Fs = 400
        y = -2.5*(cos(2*pi*fr*(x-(240))/Fs))
        a.plot(y+2.5,x8,color=colour)
    smallamplitude1(x8)

    x9 = arange(320,391)#70
    def smallamplitude1(x):
        Fs = 350
        y = -1*(cos(2*pi*fr*(x-(320))/Fs))
        a.plot(y+1,x9,color=colour)
    smallamplitude1(x9)    

    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



