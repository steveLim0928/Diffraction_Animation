
def colour_1 (canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 200
    g2 = 0
    b2 = 0
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10) 
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    
    
    #color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
    
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
##        i11 = float(steps/1.166666666667)- i
##        canvas.create_rectangle( 0, i11 ,340,i11+1, fill = color, outline = "")
##        i12 = float(steps/1.166666666667)+ i
##        canvas.create_rectangle( 0, i12 ,340,i12+1, fill = color1, outline = "")
##        i13 = steps - i
##        canvas.create_rectangle( 0, i13 ,340,i13+1, fill = color1, outline = "")
    
def colour_2(canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 255
    g2 = 140
    b2 = 0
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10)
        
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
##    color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
       
##        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color1, outline = "")
##        i1  = ((steps/7)- i)
##        canvas.create_rectangle(0,i1, 340, (i1+ 1)  , fill = color1, outline = "")
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
##        i12 = (float(steps/1.166666666667)+ i)
##        canvas.create_rectangle( 0, i12 ,340, (i12+1) , fill = color1, outline = "")
##        i13 = (steps - i)
##        canvas.create_rectangle( 0, i13 ,340,i13+1, fill = color1, outline = "")
##
def colour_3(canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 255
    g2 = 255
    b2 = 0
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10)
        
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    #color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
       
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
def colour_4(canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 0
    g2 = 109
    b2 = 91
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10)
        
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    #color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
       
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
def colour_5(canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 0
    g2 = 0
    b2 = 255
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10)
        
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    
    
    #color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
       
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
def colour_6(canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 75
    g2 = 0
    b2 = 130
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10)
        
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    #color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
       
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
        
def colour_7(canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 238
    g2 = 130
    b2 = 238
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10)
        
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    #color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/10) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
       
        canvas.create_rectangle(0, i, 340, (i + 1) , fill = color, outline = "")
        i1  = ((steps/5)- i)
        canvas.create_rectangle(0,i1, 340, (i1 + 1) , fill = color, outline = "")
        i2  = (float((steps/5))+ i )
        canvas.create_rectangle(0, i2, 340, (i2 + 1)  ,fill = color, outline = "")
        i3 = (float((steps/2.5))- i)
        canvas.create_rectangle(0, i3 , 340, (i3 + 1), fill = color, outline = "")
        i4 = (float((steps/2.5))+ i)
        canvas.create_rectangle(0, i4 , 340, (i4 + 1) , fill = color, outline = "")
        i5 = (float((steps/1.666666666667))- i) 
        canvas.create_rectangle(0, i5 , 340, (i5 +1), fill = color, outline = "")
        i6 = (float((steps/1.666666666667))+ i) 
        canvas.create_rectangle(0, i6 , 340, (i6+1),fill = color, outline = "")
        i7 = (float((steps/1.25))- i)
        canvas.create_rectangle( 0, i7 , 340, (i7+1) , fill = color, outline = "")
        i8 = (float((steps/1.25))+ i) 
        canvas.create_rectangle( 0, i8 , 340, (i8+1), fill = color, outline = "")
        i9 = steps - i
        canvas.create_rectangle( 0, i9 , 340, (i9+1), fill = color, outline = "")
