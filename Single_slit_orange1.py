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
    SS_Colour_gradient.colour_2(canvas2)

#screen where light is emitted
def screen2(canvas, colour):
    # Mac
#    canvas.create_rectangle(10, 5, 30, 345, fill = colour, outline = 'black')
#    canvas.create_text((20, 170), text = 'Light Generator', fill = 'black', angle = -90)
    
    # Window
    canvas.create_rectangle(10, 5, 30, 345, fill = colour, outline = 'black' )
    canvas.create_text((20, 170), text = 'L\nI\nG\nH\nT\n\nG\nE\nN\nE\nR\nA\nT\nO\nR', fill = 'black')

#initial value of the wave
global x
x = 30

def waves(canvas, colour, x):
    canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)

## ---------------------------------------------------------------------------

global wavelength
wavelength = 55

# when x is < 550, to create a list of waves
def orange_scene_1(canvas, wavelength, colour, x):
 
    
    if x <= (30 + wavelength):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        x += 1

    elif x <= (30 + (2 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        x += 1

    elif x <= (30 + (3 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((2 * wavelength ) - 1), 90, x - ((2 * wavelength ) - 2), 250, fill = colour, outline = colour)
        x += 1

    elif x <= (30 + (4 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((2 * wavelength ) - 1), 90, x - ((2 * wavelength ) - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((3 * wavelength ) - 1), 90, x - ((3 * wavelength ) - 2), 250, fill = colour, outline = colour)
        
        x += 1


## -----------------------------------------------------------------------------------



# All is to set the wave value when x > 550        
global x1
x1 = 30

global x2
x2 = (31 + wavelength)

global x3
x3 = (31 + (2 * wavelength))

global x4
x4 = (31 + (3 * wavelength))


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










## ----------------------------------------------------------------------------------------------------

# keep repeating, after x > 550
def orange_scene_2(canvas, colour, gap_size, a, screen_offset):
    global x1
    global x2
    global x3
    global x4






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
        x1 = 30
        x2 = (31 + wavelength)
        x3 = (31 + (2 * wavelength))
        x4 = (31 + (3 * wavelength))

    

    
    waves(canvas, colour, x1)
    waves(canvas, colour, x2)
    waves(canvas, colour, x3)
    waves(canvas, colour, x4)
    





    if x1 == 31:
        # initial z1 to 1
        z1 = 1
    # if z1 is 1
    if z1 >= 1:
        # start creating the diffracted waves
        diffracted_waves(canvas, colour, z1, gap_size, screen_offset)
        z1 += 0.5
    # out of the screen


    if z1 >= 111.5 :
        # reset it back to 0 and wait to see if the wave have repeated
        z1 = 0
        z2 = 111.5 

    
    if z2 >= 111.5  and z2 < 180 - (30 - screen_offset):
        diffracted_waves(canvas, colour, z2, gap_size, screen_offset)
        z2 += 0.5
    if z2 >= 180 - (30 - screen_offset):
        z2 += 0.5
    if z2 >= 221.5 + screen_offset:

        z2 = 111.5 + screen_offset


    # gap from screen to barrier divide 2 = value for diffracted waves
    
    ######
    if x2 > 249:
        z3 = 1
    if z3 >= 1:
        diffracted_waves(canvas, colour, z3, gap_size, screen_offset)
        z3 += 0.5
    if z3 >= 111.5 :
        z4 = 111.5 
        z3 = 0

    if z4 >= 111.5  and z4 < 180 - (30 - screen_offset):
        diffracted_waves(canvas, colour, z4, gap_size, screen_offset)
        z4 += 0.5
    if z4 >= 180 - (30 - screen_offset):
        z4 += 0.5
    if z4 >= 221.5 + screen_offset:
        z4 = 111.5 + screen_offset



    ######
        
    if x3 > 249:
        z5 = 1
    if z5 >= 1:
        diffracted_waves(canvas, colour, z5, gap_size, screen_offset)
        z5 += 0.5
    if z5 >= 111.5 :
        z6 = 111.5 
        z5 = 0

    if z6 >= 111.5  and z6 < 180 - (30 - screen_offset):
        diffracted_waves(canvas, colour, z6, gap_size, screen_offset)
        z6 += 0.5
    if z6 >= 180 - (30 - screen_offset):
        z6 += 0.5
    if z6 >= 221.5 + screen_offset:
        z6 = 111.5 + screen_offset


    ######

    

    if x4 > 249:
        z9 = 1
    if z9 >= 1:
        diffracted_waves(canvas, colour, z9, gap_size, screen_offset)
        z9 += 0.5
    if z9 >= 111.5 :
        z10 = 111.5 
        z9 = 0

    if z10 >= 111.5  and z10 < 180 - (30 - screen_offset):
        diffracted_waves(canvas, colour, z10, gap_size, screen_offset)
        z10 += 0.5
    if z10 >= 180  - (30 - screen_offset):
        z10 += 0.5
    if z10 >= 221.5 + screen_offset:
        z10 = 111.5  + screen_offset
    ## --------------------------------------------------------------------------------------------
        
    x1 += 1
    x2 += 1
    x3 += 1
    x4 += 1
    





   
    if x1 > 250:
        x1 = 30
    if x2 > 250:
        x2 = 30
    if x3 > 250:
        x3 = 30
    if x4 > 250:
        x4 = 30



        
