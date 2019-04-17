import Tkinter as tk,ttk
from PIL import Image,ImageTk
import tkFont



global root
root = tk.Tk()
root.title('Quiz')
root.resizable(False , False)

style = ttk.Style()
style.configure("TRadiobutton", font=("Bahnschrift SemiBold",15),  foreground='darkblue', background = 'grey')
style.configure("TFrame", background = 'grey')
style.configure("TLabel", foreground='black',background = 'grey')

main_frame = ttk.Frame(root)
main_frame.grid(row = 0 , column = 0, sticky = "news")
main_frame1 = ttk.Frame(root)




class Quiz(object):
        def __init__(self, root, t, questions, correctAnswers, responses):
                global answer1
                self.root = root
                self.time = time = t
                self.answers = {}
                self.correctAnswers = correctAnswers
                self.questions = questions
                self.responses = responses
                answer1 = []
                
                timerValue = ttk.Label(main_frame, text = "{}:{:02d}".format(time // 60, time % 60),font=("Bahnschrift SemiBold",20), anchor = "e")
                timerValue.grid(row = 0, column = 0, sticky = "nsew")
                
                def countdown():
                        
                        if self.time > 0:
                                root.after(1000, countdown)
                                self.time -= 1
                                timerValue["text"] = "{}:{:02d}".format((self.time + 1) // 60, (self.time + 1) % 60)
                        else:

                                
                                self.showResults()
                    

                
                        
                countdown()
                self._questionNumber = questionNumber = 1
                self.questionHeader = questionHeader = ttk.Label(main_frame, text = "Question {}".format(questionNumber), font = ("Bahnschrift SemiBold", 40,"underline"), anchor = "center")
                questionHeader.grid(row = 1, column = 0, sticky = "nsew")

                self.question = question = ttk.Label(main_frame, text = questions[questionNumber - 1],font =("Bahnschrift SemiBold",20), anchor = "center")
                question.grid(row = 2, column = 0, sticky = "nsew")

                responseFrame = ttk.Frame(main_frame)
                responseFrame.grid(row =3,column = 0,sticky = "nsew")

                self.answer = answer = tk.StringVar() 
                self.answer.set("")
                self.responseButtons = []
                
                

                for index, text in enumerate(self.responses[self.questionNumber]):
                        def nextQuestion():
                                self.answers[self.questionNumber] = int(float(answer.get()))
                                answer1.append(answer.get())

                                if self.questionNumber < len(self.questions):
                                        self.questionNumber += 1
                                        self.answer.set("")
                                else:
                                        
                                        self.time = 0
                                        countdown()
                                        
                                        
                                        self.showResults()
                        button = ttk.Radiobutton(responseFrame, text = text, value = index + 1, variable = answer, command = nextQuestion)
                        
                        
                        
                        
                        
                        self.responseButtons.append(button)
                        button.pack(anchor = "w")
                

        @property
        def questionNumber(self):
                return self._questionNumber
        @questionNumber.setter
        def questionNumber(self, val):
                self._questionNumber = val
                self.questionHeader["text"] = "Question {}".format(self.questionNumber)
                self.question["text"] = self.questions[self.questionNumber - 1]

                for index, text in enumerate(self.responses[self.questionNumber]):
                        self.responseButtons[index].config(text = text)

        def showResults(self):
                global answer1,answered
                answered = 0
                amount = 0
                wrong = []
                for key in self.correctAnswers.keys():
                        if key in self.answers.keys():
                                if self.answers[key] == self.correctAnswers[key]:
                                        amount += 1
                                        answered += 1
                                else:
                                        wrong.append(key)
                                        answered += 1
                        else:
                                wrong.append(key)
                        
                        
                print amount, wrong
                def home():
                        global root
                        root.destroy()
                        execfile('MainPage.py',globals())
                def again():
                        global root
                        root.destroy()
                        execfile('INS_QUIZ.py',globals())
                def solution():
                        
                        global root
                        main_frame1.destroy()
                        Q1_ans()
                        #execfile('Explanation1.py',globals())
                
                
                        
                timerrun = False
                main_frame.destroy()
                
                main_frame1.grid(row = 0 , column = 0, sticky = "news")
                
                dataC = "Number of question(s) correct:"+str(amount)+ "/10"
                dataW = "Question number wrong:"+str(wrong)
                resultlabel_1 = tk.Label(main_frame1,text = "Result:",font=("Bahnschrift SemiBold",25),fg='black',height = 1,width = 60,bg = 'grey')
                resultlabel_1.grid(row=0,column=0,sticky='news')
                resultlabel_2 = tk.Label(main_frame1,text = dataC,font=("Bahnschrift SemiBold",20),fg='darkblue',height = 3,width = 60,bg = 'grey')
                resultlabel_2.grid(row=1,column=0,sticky='news')
                resultlabel_3 = tk.Label(main_frame1,text = dataW,font=("Bahnschrift SemiBold",20),fg='red',height = 3,width = 60,bg = 'grey')
                resultlabel_3.grid(row=2,column=0,sticky='news')
                Labelsol= tk.Label(main_frame1,text = '''(Click the "Solution" button to check the solution for each question)''',
                                   font=("Bahnschrift SemiBold",20),fg='black',height = 3,width = 60,bg = 'grey')
                Labelsol.grid(row=3,column=0,sticky='news')
                home= tk.Button(main_frame1,text = 'Home',font = ('Bahnschrift'),command = home).grid(row=4,sticky='e')
                quizb = tk.Button(main_frame1,text = 'Retry',font=(' Bahnschrift'),command = again).grid(row=4,sticky='w') 
                solb = tk.Button(main_frame1,text = 'Solution', font=(' Bahnschrift'),command = solution).grid(row=4)
                # Answer selected

global answer1
answer1 = []

              
                
                
##              self.root.quit()

Q1 =  'A single slit of width 0.5 mm is illuminated with monochromatic light (λ=680 nm).\nA screen is placed 1.8m from the slit to observe the fringe pattern.\n\
What is the angle between the second dark fringe (n=2) and the central maximum?'
Q1_ans = ['0.16°','0.17°','0.18°','0.19°']#A
Q2 = 'Fill in the blank:\nDestructive interference occurs when the crest of one wave lines up with\nthe _______ of another wave.'
Q2_ans = ['trough','crest','wavelength','amplitude'] #A
Q3 = 'In a single-slit diffraction experiment, the width of the slit through which light passes\n is reduced.\
What happens to the width of the central bright fringe?'
Q3_ans =['It stays the same','It becomes narrower','It becomes wider','Its behavior depends on the wavelength of the light']#C
Q4 = 'A single-slit diffraction pattern is formed on a distant screen. Assuming the angles\n\
involved are small, by what factor will the width of the central bright spot on the screen\n\
changes if the slit width is doubled?'#B
Q4_ans =['It will be cut to one quarter of its original size','It will be cut in half','It will double','It will become four times as large']
Q5 = 'Light from a monochromatic source  shines through a double slit onto a screen 5.00m away.\n\
The slits are 180mm apart. The dark bands on the screen are measured to be 1.70cm apart.\n\
What is the wavelength of the incident light?'
Q5_ans =['0.457mm','0.306mm','0.392mm','0.612mm']#D
Q6 ='In a double slit experiment, if the seperation between the two slits is 0.050mm and the\n\
distance from the slits to a screen is 2.5m, find the spacing between the first-order and\n\
second-order bright fringes when coherent light of wavelength 600nm illuminates the slits.'
Q6_ans = ['1.5cm','3.0cm','4.5cm','6.0cm']#B
Q7 = '''Supposed that Young’s experiment is performed with blue-green light of 500 nm.
The slits are 1.2 mm apart, and the viewing screen is 5.4 m from the slits.
How far apart are the bright fringes?'''
Q7_ans = ['2.25mm', '2.46mm', '2.50mm',' 3.00mm']#A
Q8 = 'What term describes the phenomenon as a wave spreads into the region behind an \nobtruction?'
Q8_ans = ['Superposition','Dispersion','Diffraction','Refraction']#C
Q9 = '''A single slit, which is 0.050 mm wide, is illuminated by light of 550 nm wavelength.\n\
What is the angular separation between the first two minima on either side of
the central maximum?'''
Q9_ans = ['0.36°','0.47°','0.54°','0.63°']#D
Q10 = 'Two waves of equal amplitude destructively interfere, resulting in a wave with zero amplitude.\n\
What is the phase difference between the two waves?'
Q10_ans = ['(π/4) rad','(π/2) rad','(π) rad','(3π/2) rad']#C




quiz = Quiz(root, int(8* 60),
            [Q1,Q2,
             Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10],
            {1: 1, 2: 1, 3:3,4:2 ,5:4, 6:2 , 7:1 ,8:3, 9:4, 10:3}, {1: Q1_ans, 2: Q2_ans, 3:Q3_ans, 4:Q4_ans,5:Q5_ans,6:Q6_ans,7:Q7_ans,8:Q8_ans,9:Q9_ans,10:Q10_ans})

frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')

def Q1_ans():
    global root, answer1, frame1, answered
    frame1.destroy()

    root.resizable(False , False)

    root.geometry('700x770')
    root.title("Q1 Solution")
    root.config(background = 'grey')
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 1(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''A single slit of width 0.5 mm is illuminated with monochromatic light (λ=680 nm).\nA screen is placed 1.8m from the slit to observe the fringe pattern.What is the
angle between the second dark fringe (n=2) and the central maximum?''', font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nIn order to get the angle, the single slit formula, a sin θ = nλ is applied,
where a = 0.5mm, n = 2 and λ=680nm.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    

    a = tk.Radiobutton(frame1, text ='0.16°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    a.place(x=0 , y = 180)
            
    b = tk.Radiobutton(frame1, text ='0.17°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'grey', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 210)
        
        
    c = tk.Radiobutton(frame1, text ='0.18°',state = 'disabled',font =('Bahnschrift SemiBold',15), 
                                              fg = 'red', bg = 'grey', activebackground = 'grey',
                                            disabledforeground = 'white')
    c.place(x=0 , y = 240)
        
        
    d = tk.Radiobutton(frame1, text ='0.19°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'grey', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 270)

    while answered >= 1:
            if answer1[0] == '2':
                b.config(disabledforeground = 'red')
            if answer1[0] == '3':
                c.config(disabledforeground = 'red')
            if answer1[0] == '4':
                d.config(disabledforeground = 'red')
            break
    else:
        a.config(disabledforeground = '#ADD8E6')
        
    B1.place_forget()
    
    B3.config(command = Q2_ans)
   
    
def Q2_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q2 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 2(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''Fill in the blank:
Destructive interference occurs when the crest of one wave lines up with\nthe _______ of another wave.''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nConstructive interference occurs when two crests/ troughs meet with each
other. Hence, destructive interference will occur when a crest and a trough
meet together.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='trough',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    a.place(x=0 , y = 180)
    b =tk.Radiobutton(frame1, text ='crest',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 210)
    c =tk.Radiobutton(frame1, text ='wavelength',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    c.place(x=0 , y = 240)
    d =tk.Radiobutton(frame1, text ='amplitude',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 270)
    while answered >= 2:
            if answer1[1] == '2':
                b.config(disabledforeground = 'red')
            if answer1[1] == '3':
                c.config(disabledforeground = 'red')
            if answer1[1] == '4':
                d.config(disabledforeground = 'red')
            break
    else:
        a.config(disabledforeground = '#ADD8E6')
    B1.place(x=20, y =600)
    B1.config(command = Q1_ans)
    B3.config(command = Q3_ans)
    
    
def Q3_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q3 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 3(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''In a single-slit diffraction experiment, the width of the slit through which light
passes is reduced. What happens to the width of the central bright fringe?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nAccording to the equation, s= (nλD)/d, the width of the slit, a is inversely
proportional to the fringe width,d. Thus, when the width of the slit,a is
reduced, the fringe width,d will increase.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='It stays the same',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 180)
    b =tk.Radiobutton(frame1, text ='It becomes narrower',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 210)
    c =tk.Radiobutton(frame1, text ='It becomes wider',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    c.place(x=0 , y = 240)
    d =tk.Radiobutton(frame1, text ='Its behavior depends on the wavelength of the light',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 270)

    while answered >= 3:
            if answer1[2] == '1':
                a.config(disabledforeground = 'red')
            if answer1[2] == '2':
                b.config(disabledforeground = 'red')
            if answer1[2] == '4':
                d.config(disabledforeground = 'red')
            break
        
    else:
        c.config(disabledforeground = '#ADD8E6')
        
    B1.place(x=20, y =600)
    B1.config(command = Q2_ans)
    B3.config(command = Q4_ans)
    

def Q4_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q4 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 4(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''A single-slit diffraction pattern is formed on a distant screen. Assuming
the angles involved are small, by what factor will the width of the central
bright spot on the screen changes if the slit width is doubled?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nAccording to the single slit formula, d sin θ = nλ and  x= θD,
the width of the slit,a is inversely proportional to the fringe width,x, thus when
the width of the slit,a is doubled, the fringe width will reduced to half.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='It will be cut to one quarter of its original size',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 180)
    b =tk.Radiobutton(frame1, text ='It will be cut in half',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    b.place(x=0 , y = 210)
    c =tk.Radiobutton(frame1, text ='It will double',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    c.place(x=0 , y = 240)
    d =tk.Radiobutton(frame1, text ='It will become four times as large',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 270)

    while answered >= 4:
            if answer1[3] == '1':
                a.config(disabledforeground = 'red')
            if answer1[3] == '3':
                c.config(disabledforeground = 'red')
            if answer1[3] == '4':
                d.config(disabledforeground = 'red')
            break
        
    else:
        b.config(disabledforeground = '#ADD8E6')
        
    B1.place(x=20, y =600)
    B1.config(command = Q3_ans)
    B3.config(command = Q5_ans)
    

def Q5_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q5 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 5(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''Light from a monochromatic source  shines through a double slit onto a
screen 5.00m away. The slits are 180mm apart. The dark bands on the screen
are measured to be 1.70cm apart. What is the wavelength of the incident light?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nThe formula of Young's double slit diffraction, y= (nλD)/d is applied. The
formula is reaaranged to λ= (yd)/(nD) and the values where y = 180mm,
d= 180mm, n=1 and D= 5m, are substituted in order to find the wavelength
of the incident light.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='0.457mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 180)
    b =tk.Radiobutton(frame1, text ='0.306mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 210)
    c =tk.Radiobutton(frame1, text ='0.392mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    c.place(x=0 , y = 240)
    d =tk.Radiobutton(frame1, text ='0.612mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    d.place(x=0 , y = 270)
    while answered >= 5:
            if answer1[4] == '1':
                a.config(disabledforeground = 'red')
            if answer1[4] == '2':
                b.config(disabledforeground = 'red')
            if answer1[4] == '3':
                c.config(disabledforeground = 'red')
            break
        
    else:
        d.config(disabledforeground = '#ADD8E6')
        
    B1.place(x=20, y =600)
    B1.config(command = Q4_ans)
    B3.config(command = Q6_ans)
    

def Q6_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q6 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 6(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''In a double slit experiment, if the seperation between the two slits is 0.050mm
and the distance from the slits to a screen is 2.5m, find the spacing between
the first-order and second-order bright fringes when coherent light of
wavelength 600nm illuminates the slits.''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nThe formula for Young's double slit diffraction, y= (nλD)/d is applied and
the values where λ= 600nm, D= 2.5m and d= 0.05mm are substituted into the
equation. Values of n = 1 and n= 2 is applied to the formula respectively. Lastly,
the spacing between the fringe width of the first and second order is found by
subtracting the value of y1 from y2.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='1.5cm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 200)
    b =tk.Radiobutton(frame1, text ='3.0cm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    b.place(x=0 , y = 230)
    c =tk.Radiobutton(frame1, text ='4.5cm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    c.place(x=0 , y = 260)
    d =tk.Radiobutton(frame1, text ='6.0cm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 290)

    while answered >=6:
            if answer1[5] == '1':
                a.config(disabledforeground = 'red')
            if answer1[5] == '3':
                c.config(disabledforeground = 'red')
            if answer1[5] == '4':
                d.config(disabledforeground = 'red')
            break
        
    else:
        b.config(disabledforeground = '#ADD8E6')
    B1.place(x=20, y =600)
    B1.config(command = Q5_ans)
    B3.config(command = Q7_ans)
    

def Q7_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q7 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 7(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''Supposed that Young's experiment is performed with blue-green light of 500nm.
The slits are 1.2 mm apart, and the viewing screen is 5.4 m from the slits.
How far apart are the bright fringes?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nThe bright fringe width can be found by applying the Young's double slit formula,
y=(nλD)/d, where n =1, λ= 500nm, D= 5.4m and d=1.2mm.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='2.25mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    a.place(x=0 , y = 200)
    b =tk.Radiobutton(frame1, text ='2.46mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 230)
    c =tk.Radiobutton(frame1, text ='2.50mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    c.place(x=0 , y = 260)
    d =tk.Radiobutton(frame1, text ='3.00mm',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 290)

    while answered >=7:
            if answer1[6] == '2':
                b.config(disabledforeground = 'red')
            if answer1[6] == '3':
                c.config(disabledforeground = 'red')
            if answer1[6] == '4':
                d.config(disabledforeground = 'red')
            break
        
    else:
        a.config(disabledforeground = '#ADD8E6')
    B1.place(x=20, y =600)
    B1.config(command = Q6_ans)
    B3.config(command = Q8_ans)
   

def Q8_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q8 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 8(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''What term describes the phenomenon as a wave spreads into the region \nbehind an obtruction?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nDiffraction is a phenomenon that refers to spreading out of waves when
they move through a gap or round an obstacle.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='Superposition',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 200)
    b =tk.Radiobutton(frame1, text ='Dispersion',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 230)
    c =tk.Radiobutton(frame1, text ='Diffraction',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    c.place(x=0 , y = 260)
    d =tk.Radiobutton(frame1, text ='Refraction',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 290)

    while answered >=8:
            if answer1[7] == '1':
                a.config(disabledforeground = 'red')
            if answer1[7] == '2':
                b.config(disabledforeground = 'red')
            if answer1[7] == '4':
                d.config(disabledforeground = 'red')
            break
        
    else:
        c.config(disabledforeground = '#ADD8E6')
    B1.place(x=20, y =600)
    B1.config(command = Q7_ans)
    B3.config(command = Q9_ans)
    

def Q9_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q9 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 9(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''A single slit, which is 0.050mm wide, is illuminated by light of 550nm wavelength.
What is the angular separation between the first two minima on either side of
the central maximum?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nThe formula for single slit diffraction, a sin θ=nλ is applied,
and the values where a = 0.05mm, λ= 550nm are substituted into the equation.
The value of n= 1 and n=2 are applied respectively into the equation. Lastly,
the angular seperation is obtained by substracting θ1 from θ2.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='0.36°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 200)
    b =tk.Radiobutton(frame1, text ='0.47°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 230)
    c =tk.Radiobutton(frame1, text ='0.54°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    c.place(x=0 , y = 260)
    d =tk.Radiobutton(frame1, text ='0.63°',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    d.place(x=0 , y = 290)

    while answered >=9:
            if answer1[8] == '1':
                a.config(disabledforeground = 'red')
            if answer1[8] == '2':
                b.config(disabledforeground = 'red')
            if answer1[8] == '3':
                c.config(disabledforeground = 'red')
            break
        
    else:
        d.config(disabledforeground = '#ADD8E6')
    B1.place(x=20, y =600)
    B1.config(command = Q8_ans)
    B3.place(x=600,y=600)
    B3.config(command = Q10_ans)
   

def Q10_ans():
    global frame1, answered
    frame1.destroy()
    
    frame1 = tk.Frame(root, width = 700, height = 550, bg = 'grey')
    frame1.pack()
    
    root.title("Q10 Solution")
    #LABEL
    text1 = tk.Label(frame1, text = 'Question 10(Solution)', font =('Bahnschrift SemiBold',30,'bold','underline'), bg = 'grey')
    text1.place(x = 180, y = 50)
    
    text2 = tk.Label(frame1, text = '''Two waves of equal amplitude destructively interfere, resulting in a wave
with zero amplitude. What is the phase difference between the two waves?''',
                  font =('Bahnschrift SemiBold',15,'bold'),fg='darkblue',bg = 'grey',justify='left')
    text2.place(x =0, y = 100)
    
    
    text4 = tk.Label(frame1, text= '''Solution:\nTwo waves will cancel to zero amplitude when the relative shift between
them is half a period. This corresponds to half of 2π, which gives the correct
answer of π.''',font =('Bahnschrift SemiBold',15,'bold'),fg='black',bg = 'grey',justify='left')
    text4.place(x=0, y = 380)
    #RADIOBUTTON
    a = tk.Radiobutton(frame1, text ='(π/4) rad',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    a.place(x=0 , y = 200)
    b =tk.Radiobutton(frame1, text ='(π/2) rad',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    b.place(x=0 , y = 230)
    c =tk.Radiobutton(frame1, text ='(π) rad',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'lime')
    c.place(x=0 , y = 260)
    d =tk.Radiobutton(frame1, text ='(3π/2) rad',state = 'disable',font =('Bahnschrift SemiBold',15), 
                                              fg = 'darkgreen', bg = 'grey', activebackground = 'grey',
                                             disabledforeground = 'white')
    d.place(x=0 , y = 290)

    while answered >= 10:
            if answer1[9] == '1':
                a.config(disabledforeground = 'red')
            if answer1[9] == '2':
                b.config(disabledforeground = 'red')
            if answer1[9] == '4':
                d.config(disabledforeground = 'red')
            break
        
    else:
        c.config(disabledforeground = '#ADD8E6')
    B1.place(x=20, y =600)
    B1.config(command = Q9_ans)
    B3.place_forget()
    
    
    
def home():
        global root
        root.destroy()
        execfile('MainPage.py',globals())


    
        
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)

backb = Image.open('left-arrow.png')
backb = backb.resize((70,70))
backbb = ImageTk.PhotoImage(backb)

homeb = Image.open('homeB.png')
homeb = homeb.resize((75,75))
homebb = ImageTk.PhotoImage(homeb)


B1 = tk.Button(root, image=backbb,height=75, width = 75,borderwidth = 0,bg = 'grey', activebackground = 'grey', command = Q1_ans)
B1.place(x=20, y =600)

B2 = tk.Button(root,image=homebb,height=75,width = 75,borderwidth = 0,bg='grey',activebackground='grey',command=home)
B2.place(x=300,y=600)

B3 = tk.Button(root,image=nextbb,height=75,width=75,borderwidth=0,bg='grey',activebackground='grey',command=Q2_ans)
B3.place(x=600,y=600)  

red_a = tk.Label(root, text='(',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey', fg = 'black')
red_a.place(x=5,y=690)
red = tk.Label(root, text='Red',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey', fg = 'red')
red.place(x=15,y=690)
red_b = tk.Label(root, text='indicates wrong answer)',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey', fg = 'black')
red_b.place(x = 60, y = 690) 

text3_a = tk.Label(root, text='(',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey')
text3_a.place(x=5,y=715)
text3 = tk.Label(root, text = 'Green', font =('Bahnschrift SemiBold',15,'bold'),fg='lime', bg = 'grey')
text3.place(x=15,y=715)
text3_b = tk.Label(root, text='indicates correct answer)',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey')
text3_b.place(x = 80 ,y = 715) 

blue_a = tk.Label(root, text='(',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey', fg = 'black')
blue_a.place(x=5,y=740)
blue = tk.Label(root, text='Light Blue',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey', fg = '#ADD8E6')
blue.place(x=15,y=740)
blue_b = tk.Label(root, text='indicates unanswered questions\' answer)',font =('Bahnschrift SemiBold',15,'bold'), bg = 'grey', fg = 'black')
blue_b.place(x = 110, y = 740)  
    

root.mainloop()
