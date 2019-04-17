import SS_Colour_gradient
import Tkinter

# functions for the animation items

# gap function
def barrier(canvas, gap_size):
    above_gap = 170 - gap_size
    below_gap = 170 + gap_size
    canvas.create_rectangle(250, 5, 260, above_gap, fill = 'sky blue', outline = 'black')
    canvas.create_rectangle(250, below_gap, 260, 345, fill = 'sky blue', outline = 'black')
#black screen
def screen(canvas, screen_offset):
    # Mac
#    canvas.create_rectangle(550 + screen_offset, 5, 600 + screen_offset, 345, fill = 'black', outline = 'black')
#    canvas.create_text((575 + screen_offset, 170), text = 'Screen', fill = 'white', angle = -90)
    
    # Window
    canvas.create_rectangle(550 + screen_offset, 5, 600 + screen_offset, 345, fill = 'black', outline = 'black')
    canvas.create_text((575 + screen_offset, 170), text = 'Screen', fill = 'white')

def colour_screen (canvas2):
    SS_Colour_gradient.colour_5(canvas2)

#screen where light is emitted
def screen2(canvas, colour):
    # Mac
#    canvas.create_rectangle(10, 5, 30, 345, fill = colour, outline = 'black')
#    canvas.create_text((20, 170), text = 'Light Generator', fill = 'black', angle = -90)
    
    # Window
    canvas.create_rectangle(30, 5, 50, 345, fill = colour, outline = 'black' )
    canvas.create_text((40, 170), text = 'L\nI\nG\nH\nT\n\nG\nE\nN\nE\nR\nA\nT\nO\nR', fill = 'white')

#initial value of the wave
global x
x = 50

def waves(canvas, colour, x):
    canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)

## ---------------------------------------------------------------------------

global wavelength
wavelength = 40

# when x is < 550, to create a list of waves
def blue_scene_1(canvas, wavelength, colour, x):
 
    
    if x <= (50 + wavelength):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)

        x += 1

    elif x <= (50 + (2 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        x += 1

    elif x <= (50 + (3 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((2 * wavelength ) - 1), 90, x - ((2 * wavelength ) - 2), 250, fill = colour, outline = colour)
        x += 1

    elif x <= (50 + (4 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((2 * wavelength ) - 1), 90, x - ((2 * wavelength ) - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((3 * wavelength ) - 1), 90, x - ((3 * wavelength ) - 2), 250, fill = colour, outline = colour)
        x += 1
        
    elif x <= (50 + (5 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((2 * wavelength ) - 1), 90, x - ((2 * wavelength ) - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((3 * wavelength ) - 1), 90, x - ((3 * wavelength ) - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((4 * wavelength ) - 1), 90, x - ((4 * wavelength ) - 2), 250, fill = colour, outline = colour)
        x += 1
        


## -----------------------------------------------------------------------------------



# All is to set the wave value when x > 550        
global x1
x1 = 50

global x2
x2 = (52 + wavelength)

global x3
x3 = (52 + (2 * wavelength))

global x4
x4 = (52 + (3 * wavelength))

global x5
x5 = (52 + (4 * wavelength))


## ------------------------------------------------------------------------------------------------


# The diffraction waves after the slit
def diffracted_waves(canvas, colour, z, gap_size, screen_offset):
    above_gap = 170 - gap_size
    below_gap = 170 + gap_size

    canvas.create_arc(252 + z, above_gap - (z - 4) , 257 + 2 * z, below_gap + (z - 4), style = Tkinter.ARC, start = -90, extent = 180, width = 2, fill = colour, outline = colour)
    screen(canvas, screen_offset)
    
## --------------------------------------------------------------------------------------


# The parameter to create moving diffracted waves
global z1
z1 = 0

global z2
z2 = 0

global z3
z3 = 0

global z4
z4 = 0

global z5
z5 = 0

global z6
z6 = 0

global z7
z7 = 0

global z8
z8 = 0

global z9
z9 = 0

global z10
z10 = 0

global z11
z11 = 0

global z12
z12 = 0






## ----------------------------------------------------------------------------------------------------

# keep repeating, after x > 550
def blue_scene_2(canvas, colour, gap_size, a, screen_offset):
    global x1
    global x2
    global x3
    global x4
    global x5





    global z1
    global z2
    global z3
    global z4
    global z5
    global z6
    global z7
    global z8
    global z9
    global z10
    global z11
    global z12
 


    if a == True:
        z1 = 0
        z2 = 0
        z3 = 0
        z4 = 0
        z5 = 0
        z6 = 0
        z7 = 0
        z8 = 0
        z9 = 0
        z10 = 0
        z11 = 0
        z12 = 0
        x1 = 50
        x2 = (52 + wavelength)
        x3 = (52 + (2 * wavelength))
        x4 = (52 + (3 * wavelength))
        x5 = (52 + (4 * wavelength))

    

    
    waves(canvas, colour, x1)
    waves(canvas, colour, x2)
    waves(canvas, colour, x3)
    waves(canvas, colour, x4)
    waves(canvas, colour, x5)
    





    if x1 == 51:
        # initial z1 to 1
        z1 = 1
    # if z1 is 1
    if z1 >= 1:
        # start creating the diffracted waves
        diffracted_waves(canvas, colour, z1, gap_size, screen_offset)
        z1 += 0.5
    # out of the screen


    if z1 >= 101.5 :
        # reset it back to 0 and wait to see if the wave have repeated
        z1 = 0
        z2 = 101.5 


    if z2 >= 101.5  and z2 < 202 - (50 - screen_offset):
        diffracted_waves(canvas, colour, z2, gap_size, screen_offset)
        z2 += 0.5
    if z2 >= 202 - (50 - screen_offset):
        z2 += 0.5
    if z2 >= 211.5 - (50 - screen_offset):

        z2 = 101.5 - (50 - screen_offset)


    # gap from screen to barrier divide 2 = value for diffracted waves
    
    ######
    if x2 > 249:
        z3 = 1
    if z3 >= 1:
        diffracted_waves(canvas, colour, z3, gap_size, screen_offset)
        z3 += 0.5
    if z3 >= 101.5 :
        z4 = 101.5 
        z3 = 0

    if z4 >= 101.5  and z4 < 202 - (50 - screen_offset):
        diffracted_waves(canvas, colour, z4, gap_size, screen_offset)
        z4 += 0.5
    if z4 >= 202 - (50 - screen_offset):
        z4 += 0.5
    if z4 >= 211.5 - (50 - screen_offset):
        z4 = 101.5 - (50 - screen_offset)



    ######
        
    if x3 > 249:
        z5 = 1
    if z5 >= 1:
        diffracted_waves(canvas, colour, z5, gap_size, screen_offset)
        z5 += 0.5
    if z5 >= 101.5 :
        z6 = 101.5 
        z5 = 0

    if z6 >= 101.5  and z6 < 202 - (50 - screen_offset):
        diffracted_waves(canvas, colour, z6, gap_size, screen_offset)
        z6 += 0.5
    if z6 >= 202 - (50 - screen_offset):
        z6 += 0.5
    if z6 >= 211.5 - (50 - screen_offset):
        z6 = 101.5 - (50 - screen_offset)


   
    if x4 > 249:
        z9 = 1
    if z9 >= 1:
        diffracted_waves(canvas, colour, z9, gap_size, screen_offset)
        z9 += 0.5
    if z9 >= 101.5 :
        z10 = 101.5 
        z9 = 0

    if z10 >= 101.5  and z10 < 202 - (50 - screen_offset):
        diffracted_waves(canvas, colour, z10, gap_size, screen_offset)
        z10 += 0.5
    if z10 >= 202  - (50 - screen_offset):
        z10 += 0.5
    if z10 >= 211.5 - (50 - screen_offset):
        z10 = 101.5  - (50 - screen_offset)
        
    #######
    if x5 > 249:
        z11 = 1
    if z11 >= 1:
        diffracted_waves(canvas, colour, z11, gap_size, screen_offset)
        z11 += 0.5
    if z11 >= 101.5 :
        z12 = 101.5 
        z11 = 0

    if z12 >= 101.5  and z12 < 202 - (50 - screen_offset):
        diffracted_waves(canvas, colour, z12, gap_size, screen_offset)
        z12 += 0.5
    if z12 >= 202  - (50 - screen_offset):
        z12 += 0.5
    if z12 >= 211.5 - (50 - screen_offset):
        z12 = 101.5  - (50 - screen_offset)
    ## --------------------------------------------------------------------------------------------
        
    x1 += 1
    x2 += 1
    x3 += 1
    x4 += 1
    x5 += 1
    





   
    if x1 > 250:
        x1 = 50
    if x2 > 250:
        x2 = 50
    if x3 > 250:
        x3 = 50
    if x4 > 250:
        x4 = 50
    if x5 > 250:
        x5 = 50    
    



        


