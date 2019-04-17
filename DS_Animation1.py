import Tkinter
import tkMessageBox
from PIL import ImageTk, Image
import Double_slit_red1 as DSr
import Double_slit_orange1 as DSo
import Double_slit_yellow1 as DSy
import Double_slit_green1 as DSg
import Double_slit_blue1 as DSb
import Double_slit_indigo1 as DSi
import Double_slit_purple1 as DSp


import Calculation2


import DS_Graph as DSG
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tkinter.Tk()
root.title('Double Slit Animation')
root.geometry("1150x550")
root.resizable(False, False)

# Values --------------------------------------------------------------------
global x
x = 50

global status
status = True

global reset
reset = False

# To allow the animation z value be resetted
global reset_z
reset_z = False

# ---------------------------------------------------------------------------

global x2
x2 = 1


def start_animation():
    global reset, reset_z, num, gap, x, offset, width, canvas3, x2, canvas4, colour 
    
    get_result()
    
    colour = True
    
    reset = True
    
    start_button.config(state = 'disable')
    pause_button.config(state = 'normal')
    reset_button.config(state = 'normal')

    #gap_slider.config(state = 'disable')
    screen_offset_slider.config(state = 'disable')
    width_slider.config(state = 'disable')
    
    width_calculation_value()
    offset_calculation_value()
    

    gap = 20
    

    offset = ((offset * 100) - 100) * 2
    
    for i in range(1, 8):
        colour_choice[i].config(state = 'disable')
    
    while reset == True:

        if reset == True and status == True:
            
            if v.get() == 0 and colour == True:
                reset_animation()
                return tkMessageBox.showinfo('Colour Error', 'Please choose a colour')
            
            elif num == 1:
                
                
                if x == 50:
                    x = 70
                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSr.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSr.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSr.screen2(canvas2, 'red')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSr.red_scene_1(canvas2, 60, 'red', x)
                    
                    canvas2.create_text(102, 25, text = '665nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 30, 71, 40, fill = 'black')
                    canvas2.create_line(131, 30, 131, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 35, 131, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 35, 78, 38, fill = 'black')
                    canvas2.create_line(71, 35, 78, 32, fill = 'black')
                    canvas2.create_line(124, 38, 131, 35, fill = 'black')
                    canvas2.create_line(124, 32, 131, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSr.barrier(canvas2, gap, width)
                    # screen(canvas)
                   
                    if x2 < 290 + offset:
                        DSr.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSr.colour_screen(canvas3)
                        x2 += 1
                        
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 51)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.45),dpi=100)
                        a = f.add_subplot(111)
                        
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 20, 'red')
                    
                    # screen2(canvas, colour)
                    DSr.screen2(canvas2, 'red')
                    
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSr.red_scene_2(canvas2, 'red', gap, reset_z, offset)
                    
                    canvas2.create_text(102, 25, text = '665nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 30, 71, 40, fill = 'black')
                    canvas2.create_line(131, 30, 131, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 35, 131, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 35, 78, 38, fill = 'black')
                    canvas2.create_line(71, 35, 78, 32, fill = 'black')
                    canvas2.create_line(124, 38, 131, 35, fill = 'black')
                    canvas2.create_line(124, 32, 131, 35, fill = 'black')
                    
                    
                    reset_z = False
                    
                    
                 
               
                # Window ---------------------------------------------------------
                root.after(7)
                
                
                canvas2.update()

            elif num == 2:
                
                

                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSo.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSo.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSo.screen2(canvas2, 'orange')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSo.orange_scene_1(canvas2, 55, 'orange', x)
                    
                    canvas2.create_text(62, 25, text = '630nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(31, 30, 31, 40, fill = 'black')
                    canvas2.create_line(91, 30, 91, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(31, 35, 91, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(31, 35, 38, 38, fill = 'black')
                    canvas2.create_line(31, 35, 38, 32, fill = 'black')
                    canvas2.create_line(84, 38, 91, 35, fill = 'black')
                    canvas2.create_line(84, 32, 91, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSo.barrier(canvas2, gap, width)
                    # screen(canvas)
                    
                    if x2 < 290 + offset:
                        DSo.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSo.colour_screen(canvas3)
                        x2 += 1
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 56)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.40),dpi=100)
                        a = f.add_subplot(111)
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 20, 'orange')
                        
                    # screen2(canvas, colour)
                    DSo.screen2(canvas2, 'orange')
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSo.orange_scene_2(canvas2, 'orange', gap, reset_z, offset)
                    
                    canvas2.create_text(62, 25, text = '630nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(31, 30, 31, 40, fill = 'black')
                    canvas2.create_line(91, 30, 91, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(31, 35, 91, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(31, 35, 38, 38, fill = 'black')
                    canvas2.create_line(31, 35, 38, 32, fill = 'black')
                    canvas2.create_line(84, 38, 91, 35, fill = 'black')
                    canvas2.create_line(84, 32, 91, 35, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
                
            elif num == 3:
                
                

                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSy.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSy.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSy.screen2(canvas2, 'yellow')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSy.yellow_scene_1(canvas2, 50, 'yellow', x)
                    
                    canvas2.create_text(77, 25, text = '600nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(51, 30, 51, 40, fill = 'black')
                    canvas2.create_line(101, 30, 101, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(51, 35, 101, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(51, 35, 58, 38, fill = 'black')
                    canvas2.create_line(51, 35, 58, 32, fill = 'black')
                    canvas2.create_line(94, 38, 101, 35, fill = 'black')
                    canvas2.create_line(94, 32, 101, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSy.barrier(canvas2, gap, width)
                    # screen(canvas)
                    
                    if x2 < 290 + offset:
                        DSy.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSy.colour_screen(canvas3)
                        x2 += 1
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 56)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.40),dpi=100)
                        a = f.add_subplot(111)
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 10, 'yellow')
                    
                    # screen2(canvas, colour)
                    DSy.screen2(canvas2, 'yellow')
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSy.yellow_scene_2(canvas2, 'yellow', gap, reset_z, offset)
                    
                    canvas2.create_text(77, 25, text = '600nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(51, 30, 51, 40, fill = 'black')
                    canvas2.create_line(101, 30, 101, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(51, 35, 101, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(51, 35, 58, 38, fill = 'black')
                    canvas2.create_line(51, 35, 58, 32, fill = 'black')
                    canvas2.create_line(94, 38, 101, 35, fill = 'black')
                    canvas2.create_line(94, 32, 101, 35, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
                
            elif num == 4:
                


                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSg.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSg.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSg.screen2(canvas2, 'teal')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSg.green_scene_1(canvas2, 45, 'teal', x)
                    DSg.screen2(canvas2, 'teal')
                    
                    canvas2.create_text(97, 25, text = '550nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 30, 71, 40, fill = 'black')
                    canvas2.create_line(121, 30, 121, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 35, 121, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 35, 78, 38, fill = 'black')
                    canvas2.create_line(71, 35, 78, 32, fill = 'black')
                    canvas2.create_line(114, 38, 121, 35, fill = 'black')
                    canvas2.create_line(114, 32, 121, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSg.barrier(canvas2, gap, width)
                    # screen(canvas)
                    
                    if x2 < 290 + offset:
                        DSg.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSg.colour_screen(canvas3)
                        x2 += 1
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 56)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.40),dpi=100)
                        a = f.add_subplot(111)
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 10, 'teal')
                        
                    # screen2(canvas, colour)
                    DSg.screen2(canvas2, 'teal')
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSg.green_scene_2(canvas2, 'teal', gap, reset_z, offset)
                    DSg.screen2(canvas2, 'teal')
                    
                    canvas2.create_text(97, 25, text = '550nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 30, 71, 40, fill = 'black')
                    canvas2.create_line(121, 30, 121, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 35, 121, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 35, 78, 38, fill = 'black')
                    canvas2.create_line(71, 35, 78, 32, fill = 'black')
                    canvas2.create_line(114, 38, 121, 35, fill = 'black')
                    canvas2.create_line(114, 32, 121, 35, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
                
            elif num == 5:
                
                

                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSb.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSb.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSb.screen2(canvas2, 'blue')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSb.blue_scene_1(canvas2, 40, 'blue', x)
                    
                    canvas2.create_text(75, 25, text = '470nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(51, 30, 51, 40, fill = 'black')
                    canvas2.create_line(91, 30, 91, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(51, 35, 91, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(51, 35, 58, 38, fill = 'black')
                    canvas2.create_line(51, 35, 58, 32, fill = 'black')
                    canvas2.create_line(84, 38, 91, 35, fill = 'black')
                    canvas2.create_line(84, 32, 91, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSb.barrier(canvas2, gap, width)
                    # screen(canvas)
                    if x2 < 290 + offset:
                        DSb.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSb.colour_screen(canvas3)
                        x2 += 1
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 56)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.40),dpi=100)
                        a = f.add_subplot(111)
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 10, 'blue')  
                        
                    # screen2(canvas, colour)
                    DSb.screen2(canvas2, 'blue')
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSb.blue_scene_2(canvas2, 'blue', gap, reset_z, offset)
                    
                    canvas2.create_text(75, 25, text = '470nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(51, 30, 51, 40, fill = 'black')
                    canvas2.create_line(91, 30, 91, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(51, 35, 91, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(51, 35, 58, 38, fill = 'black')
                    canvas2.create_line(51, 35, 58, 32, fill = 'black')
                    canvas2.create_line(84, 38, 91, 35, fill = 'black')
                    canvas2.create_line(84, 32, 91, 35, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
                
            elif num == 6:
                
                

                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSi.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSi.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSi.screen2(canvas2, 'indigo')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSi.indigo_scene_1(canvas2, 35, 'indigo', x)
                    
                    canvas2.create_text(65, 25, text = '425nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(41, 30, 41, 40, fill = 'black')
                    canvas2.create_line(76, 30, 76, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(41, 35, 76, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(41, 35, 48, 38, fill = 'black')
                    canvas2.create_line(41, 35, 48, 32, fill = 'black')
                    canvas2.create_line(69, 38, 76, 35, fill = 'black')
                    canvas2.create_line(69, 32, 76, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSi.barrier(canvas2, gap, width)
                    # screen(canvas)
                    
                    if x2 < 290 + offset:
                        DSi.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSi.colour_screen(canvas3)
                        x2 += 1
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 56)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.40),dpi=100)
                        a = f.add_subplot(111)
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 10, 'indigo')
                    
                    # screen2(canvas, colour)
                    DSi.screen2(canvas2, 'indigo')
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSi.indigo_scene_2(canvas2, 'indigo', gap, reset_z, offset)
                    
                    canvas2.create_text(65, 25, text = '425nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(41, 30, 41, 40, fill = 'black')
                    canvas2.create_line(76, 30, 76, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(41, 35, 76, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(41, 35, 48, 38, fill = 'black')
                    canvas2.create_line(41, 35, 48, 32, fill = 'black')
                    canvas2.create_line(69, 38, 76, 35, fill = 'black')
                    canvas2.create_line(69, 32, 76, 35, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
                
            elif num == 7:
                
                

                if x <= 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSp.barrier(canvas2, gap, width)
                    # screen(canvas)
                    DSp.screen(canvas2, offset)
                    # screen2(canvas, colour)
                    DSp.screen2(canvas2, 'violet')
                    # red_scene_1(canvas, wavelength, colour, x)
                    DSp.purple_scene_1(canvas2, 30, 'violet', x)
                    DSp.screen2(canvas2, 'violet')
                    
                    canvas2.create_text(95, 25, text = '400nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 30, 71, 40, fill = 'black')
                    canvas2.create_line(101, 30, 101, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 35, 101, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 35, 78, 38, fill = 'black')
                    canvas2.create_line(71, 35, 78, 32, fill = 'black')
                    canvas2.create_line(93, 38, 100, 35, fill = 'black')
                    canvas2.create_line(93, 32, 100, 35, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    canvas2.delete('all')
                    # barrier(canvas, gap_size)
                    DSp.barrier(canvas2, gap, width)
                    # screen(canvas)
                    
                    if x2 < 290 + offset:
                        DSp.screen(canvas2, offset)
                        x2 += 1
                    if x2 == 290 + offset:
                        canvas3 = Tkinter.Canvas(upper_frame, width = 45, height = 335, 
                                                 bg = 'light grey', highlightbackground = 'black')
                        canvas3.place(x = 576 + offset, y = 55)
                        DSp.colour_screen(canvas3)
                        x2 += 1
                        
                        canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                                                 bg = 'black', highlightbackground = 'black')
                        canvas4.place (x = 687, y = 56)
                        
                        graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
                        graph_label.place(x = 10, y = 140)
                        
                        f = Figure(figsize=(2.1,3.40),dpi=100)
                        a = f.add_subplot(111)
                        f.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
                        f.set_facecolor('black')
                        graph_canvas = FigureCanvasTkAgg(f, master = canvas4)
                        graph_canvas.get_tk_widget().place(x = 2, y = 0)
                        DSG.DS_Graph1(graph_canvas, a, 10, 'violet')
                        
                    # screen2(canvas, colour)
                    DSp.screen2(canvas2, 'violet')
                    # red_scene_2(canvas, colour, gap_size, a)
                    DSp.purple_scene_2(canvas2, 'violet', gap, reset_z, offset)
                    
                    canvas2.create_text(95, 25, text = '400nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 30, 71, 40, fill = 'black')
                    canvas2.create_line(101, 30, 101, 40, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 35, 101, 35, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 35, 78, 38, fill = 'black')
                    canvas2.create_line(71, 35, 78, 32, fill = 'black')
                    canvas2.create_line(93, 38, 100, 35, fill = 'black')
                    canvas2.create_line(93, 32, 100, 35, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
            
            
        else:
            break

def pause_animation():
    global status, x2

    if status:
            status = False
            pause_button.config(text = "Resume" , bg = "lime", \
                                state = 'normal', fg = "black")
        
    else:
        status = True
        pause_button.config(text = "Pause" , bg = "yellow", \
                                state = 'normal', fg = "black")

        # continue the animation
        x2 = x2
        start_animation()
        

def reset_animation():
    global reset, status, x, reset_z, canvas3, x2, canvas4, v, num, colour

    status = True

    reset = False
    
    colour = False

    canvas2.delete('all')
    
    canvas4.destroy()

    x = 50

    reset_z = True
    
    v.set(0)
    num = 0
    
    for i in range(1, 8):
        colour_choice[i].config(state = 'normal')
    
    if x2 >= 290 + offset:
        canvas3.destroy()
    x2 = 1
    
    DSr.barrier(canvas2, gap, width)
    DSr.screen(canvas2, offset)
    DSr.screen2(canvas2, 'red')
    
    answer_canvas.delete('all')

    start_button.config(state = 'normal', fg = 'black', bg = 'lime')
    pause_button.config(text = 'Pause', state = 'disable', bg = 'yellow')
    reset_button.config(state = 'disable')

    #gap_slider.config(state = 'normal')
    screen_offset_slider.config(state = 'normal')
    width_slider.config(state = 'normal')
    Calculation2.empty(answer_canvas)

    
def offset_value(x):

    global offset, gap
    
    width_calculation_value()
    gap = 20
    offset_calculation_value()
    offset = ((offset * 100) - 100) * 2
    animation_base()

def gap_value(x):
    global gap, reset, status, offset
    width_calculation_value()
    gap = 20
    offset_calculation_value()
    offset = ((offset * 100) - 100) * 2
    if reset == True and status == True:
        start_animation()
        
    else:    
        animation_base()
        
def width_value(x):
    global gap, offset, width
    
    width_calculation_value()
    gap = 20
    offset_calculation_value()
    offset = ((offset * 100) - 100) * 2
    width = width_slider.get() * 200
    animation_base()
    

def width_calculation_value():
    global gap, calculation_width, width
    gap = 20
    width = width_slider.get() * 200
    calculation_width = width_slider.get()
    return width


def offset_calculation_value():
    global offset, calculation_offset, width
    calculation_offset = screen_offset_slider.get()
    offset = screen_offset_slider.get()
    width = width_slider.get() * 200
    
    return offset, calculation_offset, width
    
def get_result():
    global calculation_width, calculation_offset, wavelength
    
    v_value()
    width_calculation_value()
    offset_calculation_value()
    
    Calculation2.double_calculation(calculation_width, calculation_offset, wavelength, answer_canvas)
    
    
def get_back():
    global root
    reset_animation()
    root.destroy()
    execfile ('theory2.py',globals())
    
def get_home():
    global root
    reset_animation()
    root.destroy()
    execfile ('MainPage.py', globals())
    
# Frames and canvas----------------------------------------------------------------------

# Frame that contain animation
upper_frame = Tkinter.Frame(root, width =1150, height = 550, bg = 'grey', highlightbackground = 'black')
upper_frame.place(x = 0, y = 0)

image = Image.open('animation_background4.jpg')
image = image.resize((1150, 550), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

photo2 = Tkinter.Label(upper_frame, image = photo)
photo2.place(x = 0, y = 0)

# Main animation canvas
canvas2 = Tkinter.Canvas(upper_frame, width = 650, height = 350, bg = 'light grey', 
                         highlightbackground = 'black')
canvas2.place(x = 25, y = 50)

# Option canvas
option_canvas = Tkinter.Canvas(upper_frame, width = 230, height = 380, bg = 'sky blue', 
                               highlightbackground = 'black')
option_canvas.place(x = 910, y = 30)

answer_canvas = Tkinter.Canvas(upper_frame, width = 350, height = 110, bg = 'sky blue')
answer_canvas.place(x = 415, y = 410)

tri_canvas = Tkinter.Canvas(upper_frame, width = 218, height = 348, 
                         bg = 'black', highlightbackground = 'grey')
tri_canvas.place (x = 682, y = 50)


canvas4 = Tkinter.Canvas(upper_frame, width = 210, height = 340, 
                         bg = 'black', highlightbackground = 'black')
canvas4.place (x = 687, y = 56)

graph_label = Tkinter.Label(canvas4, text = 'Colour Intensity \nGraph', bg = 'black', fg = 'white', font = ('Arial', 20))
graph_label.place(x = 10, y = 140)

bottom_canvas = Tkinter.Canvas(upper_frame, width = 1150, height = 20, bg = 'black',
                               highlightbackground = 'black')
bottom_canvas.place(x = 3, y = 525)

# ------------------------------------------------------------------------------------
# Colour selection radio button settings.

MODES = [
        ('Red', "Red\n (665nm)", 1, 665),
        ('Dark Orange', "Orange\n (630nm)", 2, 630),
        ('Yellow', "Yellow\n (600nm)", 3, 600),
        ('teal', "Green\n (550nm)", 4, 550),
        ('Blue', "Blue\n (470nm)", 5, 470),
        ('Indigo', "Indigo\n (425nm)", 6, 425),
        ('Violet', "Violet\n (400nm)", 7, 400)
    ]

v = Tkinter.IntVar()
v.set(0) # initialize

colour_choice = dict()

for colour, text, mode, wavelength in MODES:
     
     colour_choice[mode] = Tkinter.Radiobutton(upper_frame, text=text, variable=v, state = 'normal', 
                                         value=mode, fg = colour, bg = 'sky blue', activebackground = colour, 
                                         activeforeground = colour, selectcolor = 'light grey')
     if mode < 5:
         mode = mode - 1
         colour_choice[mode + 1].place(x = 940, y = 210 + (mode * 35))


     else:
         mode = mode - 5
         colour_choice[mode + 5].place(x = 1029, y = 228 + (mode * 35))
         

def v_value():
     global v
     global num, wavelength
     a = MODES[v.get() - 1]

     wavelength = a[3]
     num = a[2]
     

# adjusted so that when slider moves, animation changes
def animation_base():
    global offset, gap
    canvas2.delete('all')
    
    DSr.barrier(canvas2, gap, width)
    DSr.screen(canvas2, offset)
    DSr.screen2(canvas2, 'red')
    Calculation2.empty(answer_canvas)
     
# Buttons -------------------------------------------------------------------------------------

   
# Start button
start_button = Tkinter.Button(upper_frame, text = 'Start', command = start_animation, 
                              state = 'normal', pady = 2, padx = 5, bd = 3, bg = 'lime')
start_button.place(x = 930, y = 370)

# Pause button
pause_button = Tkinter.Button(upper_frame, text = 'Pause', command = pause_animation, 
                              state = 'disable', pady = 2, padx = 5, bd = 3, bg = 'yellow')
pause_button.place(x = 990, y = 370)

# Reset button
reset_button = Tkinter.Button(upper_frame, text = 'Reset', command = reset_animation, 
                              state = 'disable', pady = 2, padx = 5, bd = 3, bg = 'red', fg = 'white')
reset_button.place(x = 1060, y = 370)

# To go to graph page
home_button = Tkinter.Button(upper_frame, text = 'Home', command = get_home, 
                              state = 'normal', pady = 1, padx = 5, bd = 3, bg = '#FFFFE0', fg = 'black')
home_button.place(x = 1080, y = 520)

back_button = Tkinter.Button(upper_frame, text = 'Back', command = get_back,
                             state = 'normal', pady = 1, padx = 7, bd = 3, bg = '#FFFFE0', fg = 'black')
back_button.place(x = 10, y = 520)


# Gap size slider and label
#gap_label = Tkinter.Label(upper_frame, text = 'Gap size (mm)', bg = 'sky blue')
#gap_label.place(x = 970, y = 30)
#gap_slider = Tkinter.Scale(upper_frame, from_ = 0.10, to = 0.50, resolution = 0.01, 
#                           bg = 'sky blue', command = gap_value, state = 'normal', 
#                           orient = 'horizontal', length = 150)
#gap_slider.place(x = 950, y = 50)

width_label = Tkinter.Label(upper_frame, text = 'Slit seperation (mm)', bg = 'sky blue')
width_label.place(x = 970, y = 40)
width_slider = Tkinter.Scale(upper_frame, from_ = 0.10, to = 0.40, resolution = 0.01, 
                           bg = 'sky blue', command = width_value, state = 'normal', 
                           orient = 'horizontal', length = 150)
width_slider.place(x = 950, y = 60)

# screen distance slider and label
offset_label = Tkinter.Label(upper_frame, text = 'Distance from barrier\n to screen (m)',
                             bg = 'sky blue')
offset_label.place(x = 970, y = 120)
screen_offset_slider = Tkinter.Scale(upper_frame, from_ = 1.00, to = 1.20, 
                                     resolution = 0.01, bg = 'sky blue', 
                                     command = offset_value, state = 'normal', 
                                     orient = 'horizontal', length = 150)
screen_offset_slider.place(x = 950, y = 160)

# -------------------------------------------------------------------------

# main display for animation (won't be empty initially)
DSr.barrier(canvas2, 20, width_slider.get() * 200)
DSr.screen(canvas2, ((screen_offset_slider.get() * 100)- 100) * 2)
DSr.screen2(canvas2, 'red')
Calculation2.empty(answer_canvas)

root.mainloop()

