global n
n = 1

import math

def empty(canvas):
    canvas.create_text(60, 15, text = 'Calculation', fill = 'maroon', font =('Bahnschrift SemiBold',20,'bold', 'underline'))
    
    
def double_calculation(gap, offset, wavelength, canvas):

    
    global n, A, D, LAMBDA
    A = float(gap/1000)
    D = float(offset)
    LAMBDA = float(wavelength)/1000000000
    
    
    
    theta_value = (((math.asin(float((((n*LAMBDA)/A)))))))
    bright_value = (n * LAMBDA * D) / A
    dark_value = bright_value / 2
    
    bright_value = bright_value * 1000
    dark_value = dark_value * 1000
    
    theta_value = str(round(theta_value, 4))
    bright_value = str(round(bright_value, 2))  
    dark_value = str(round(dark_value, 2))
    
    n1 = str(n)
    
    canvas.create_text(60, 15, text = 'Calculation', fill = 'maroon', font =('Bahnschrift SemiBold',20,'bold', 'underline'))
    
    canvas.create_text(50, 40, text = ('Value of n = ' + n1), fill = 'red')
    
    canvas.create_text(68, 60, text = ('Theta = ' + theta_value + ' rad'), fill = 'black')
    
    canvas.create_text(175, 80, text = ('Distance from centre to 1st bright fringe = ' + bright_value + ' mm'), fill = 'black')
    
    canvas.create_text(170, 100, text = ('Distance from centre to 1st dark fringe = ' + dark_value + ' mm'), fill = 'black')
    

####################################################################################################################
    
def single_calculation(gap, offset, wavelength, canvas):

    
    global n, A, D, LAMBDA
    A = float(gap/1000)
    D = float(offset)
    LAMBDA = float(wavelength)/1000000000
    

    
    theta_value = (((math.asin(float((((n*LAMBDA)/A)))))))
    dark_value1 = (D*(math.tan(theta_value)))
    bright_value1 = dark_value1 * 3 / 2
    
    
    bright_value1 = bright_value1 * 1000
    dark_value1 = dark_value1 * 1000
    
    theta_value = str(round(theta_value, 4))
    bright_value1 = str(round(bright_value1, 2))  
    dark_value1 = str(round(dark_value1, 2))
    
    n1 = str(n)
    
    canvas.create_text(60, 15, text = 'Calculation', fill = 'maroon', font =('Bahnschrift SemiBold',20,'bold', 'underline'))
    
    canvas.create_text(50, 40, text = ('Value of n = ' + n1), fill = 'red')
    
    canvas.create_text(68, 60, text = ('Theta = ' + theta_value + ' rad'), fill = 'black')
    
    canvas.create_text(175, 80, text = ('Distance from centre to 1st bright fringe = ' + bright_value1 + ' mm'), fill = 'black')
    
    canvas.create_text(170, 100, text = ('Distance from centre to 1st dark fringe = ' + dark_value1 + ' mm'), fill = 'black')
    


