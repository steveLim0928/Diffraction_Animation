#Single slit red 

def colour_1 (canvas):
    global r1, g1, b1, r2, g2, b2, steps, rdelta, bdelta, gdelta, r6, r7, rdelta4
    r1 = 135
    g1 = 0
    b1 = 0
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    r6 = 200#i2&i7&i1&i8
    r7 = 0
    rdelta4 = (r6 - r7)/ float(steps/10)#new
    
    for i in range(int(steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r6), int(g1), int(b1))

        r6 -= rdelta4#new
        g1 -= gdelta#new
        b1 -= bdelta#new
    
        ia = steps/12 -i
        canvas.create_rectangle(0 , ia , 100 , ia + 6, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0 , i0 , 100 , i0 + 6, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0 , i1 , 100 , i1 + 6, fill = color4, outline = "")
    
        i2  = (steps/4)+ i
        canvas.create_rectangle(0 , i2 , 100 , i2 + 6, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0 ,i7 , 100 , i7 + 6, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0 ,i8 , 100 , i8 + 6, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0 , i9  ,100 , i9 + 6, fill = color, outline = "")
    
        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0 ,ilast ,100 ,ilast + 6, fill = color, outline = "")
        
        
    r3 = 175#new
    r4 = 250#new
    rdelta2 = (r3 - r4)/ float(steps/10)#new
    r5 = 175
    r6 = 0
    rdelta3 = (r5 - r6)/ float(steps/10)#new
    for a in range((steps/12) + 1):#new
        
        color2 = '#%02x%02x%02x' % (int(r3), int(g1), int(b1))#new
        r3 -= rdelta2#new
        g1 -= gdelta#new
        b1 -= bdelta#new
    
        i3  = (float(steps/2.4))+ a
        canvas.create_rectangle(0  ,i3  ,100  ,i3 + 6,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a
        canvas.create_rectangle(0 , i6  ,100  , i6 + 6, fill = color2, outline = "")
    
        color3 = '#%02x%02x%02x' % (int(r5), int(g1), int(b1))#new
        r5 -= rdelta3#new
        g1 -= gdelta#new
        b1 -= bdelta#new
    
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0 ,i4 + 5, 100 , i4 + 6, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0 , i5 + 5, 100  ,i5 +6 , fill = color3, outline = "")




#single slit orange

def colour_2 (canvas):
    global r1,g1,b1,r2,g2,b2,steps,rdelta,bdelta,gdelta,g6,g7,gdelta4
    r1 = 255
    g1 = 90
    b1 = 0
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    g6 = 110#i2&i7&i1&i8
    g7 = 0
    gdelta4 = (g6 - g7)/ float(steps/10)#new
    for i in range((steps/12) + 1):
    
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
 
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
    
        color4 = '#%02x%02x%02x' % (int(r1), int(g6), int(b1))

        g6 -= gdelta4
   

        ia = steps/12 -i
        canvas.create_rectangle(0, ia, 336, ia + 1, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0, i0, 336, i0 + 1, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0, i1, 336, i1 + 1, fill = color4, outline = "")

        i2  = (steps/4)+ i 
        canvas.create_rectangle(0, i2, 336, i2 + 1, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0,i7, 336, i7 + 1, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0,i8, 336, i8 + 1, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0, i9 ,336, i9 + 1, fill = color, outline = "")

        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0,ilast,336,ilast + 1, fill = color, outline = "")


    r1 = 255
    r2 = 0

    b1 = 0
    b2 = 0

    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)


    g3 = 140
    g4 = 140
    gdelta2 = (g3 - g4)/ float(steps/10)


    g5 = 140
    g6 =  0
    gdelta3 = (g5 - g6)/ float(steps/10)


    color2 = '#%02x%02x%02x' % (int(r1), int(g3), int(b1))
    r1 -= rdelta
    g3 -= gdelta2
        
    for a in range((steps/12) + 1):

        i3  = (float(steps/2.4))+ a #middle orange
        canvas.create_rectangle(0, i3 ,336 ,i3 + 1,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a #middle orange
        canvas.create_rectangle(0, i6 ,336 , i6 + 1, fill = color2, outline = "")

        color3 = '#%02x%02x%02x' % (int(r1), int(g5), int(b1))
        r1 -= rdelta
        g5 -= gdelta3
        b1 -= bdelta
        
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0,i4, 336, i4 + 1, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0, i5 , 336 ,i5 +1 , fill = color3, outline = "")




#single slit yellow

def colour_3 (canvas):
    global r1,g1,b1,r2,g2,b2,steps,rdelta,bdelta,gdelta,g6,g7,gdelta4
    r1 = 255
    g1 = 200
    b1 = 0
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    g6 = 220#i2&i7&i1&i8
    g7 = 0
    gdelta4 = (g6 - g7)/ float(steps/10)#new
    for i in range((steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
     
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r1), int(g6), int(b1))

        g6 -= gdelta4
       

        ia = steps/12 -i
        canvas.create_rectangle(0, ia, 336, ia + 1, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0, i0, 336, i0 + 1, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0, i1, 336, i1 + 1, fill = color4, outline = "")

        i2  = (steps/4)+ i 
        canvas.create_rectangle(0, i2, 336, i2 + 1, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0,i7, 336, i7 + 1, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0,i8, 336, i8 + 1, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0, i9 ,336, i9 + 1, fill = color, outline = "")

        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0,ilast,336,ilast + 1, fill = color, outline = "")


    r1 = 255
    r2 = 0

    b1 = 0
    b2 = 0

    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)

    g5 = 240
    g6 =  0
    gdelta3 = (g5 - g6)/ float(steps/10)

    g3 = 240 #color of middle yellow
    g4 = 255 #color of middle yellow
    gdelta2 = (g3 - g4)/ float(steps/10)#color of middle yellow

    color2 = '#%02x%02x%02x' % (int(r1), int(g3), int(b1))#outside the function
    r1 -= rdelta
    g3 -= gdelta2
        
    for a in range((steps/12) + 1):
        i3  = (float(steps/2.4))+ a #middle yellow
        canvas.create_rectangle(0, i3 ,336 ,i3 + 1,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a #middle yellow
        canvas.create_rectangle(0, i6 ,336 , i6 + 1, fill = color2, outline = "")

        color3 = '#%02x%02x%02x' % (int(r1), int(g5), int(b1))
        r1 -= rdelta
        g5 -= gdelta3
        b1 -= bdelta
        
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0,i4, 336, i4 + 1, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0, i5 , 336 ,i5 +1 , fill = color3, outline = "")



#single slit green


def colour_4 (canvas):
    global r1,g1,b1,r2,g2,b2,steps,rdelta,bdelta,gdelta,g6,g7,gdelta4
    r1 = 0
    g1 = 109
    b1 = 91
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    g6 = 140#i2&i7&i1&i8
    g7 = 0
    gdelta4 = (g6 - g7)/ float(steps/10)#new
    for i in range((steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
     
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r1), int(g6), int(b1))

        g6 -= gdelta4
       

        ia = steps/12 -i
        canvas.create_rectangle(0, ia, 336, ia + 1, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0, i0, 336, i0 + 1, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0, i1, 336, i1 + 1, fill = color4, outline = "")

        i2  = (steps/4)+ i 
        canvas.create_rectangle(0, i2, 336, i2 + 1, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0,i7, 336, i7 + 1, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0,i8, 336, i8 + 1, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0, i9 ,336, i9 + 1, fill = color, outline = "")

        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0,ilast,336,ilast + 1, fill = color, outline = "")

    r1 = 0
    r2 = 0

    b1 = 91
    b2 = 0

    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)

    g5 =  170
    g6 =  0
    gdelta3 = (g5 - g6)/ float(steps/10)

    g3 = 170 #color of middle green
    g4 = 220 #color of middle green
    gdelta2 = (g3 - g4)/ float(steps/10)#color of middle green

    color2 = '#%02x%02x%02x' % (int(r1), int(g3), int(b1))#outside the function
    r1 -= rdelta
    g3 -= gdelta2
        
    for a in range((steps/12) + 1):
        i3  = (float(steps/2.4))+ a #middle green
        canvas.create_rectangle(0, i3 ,336 ,i3 + 1,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a #middle green
        canvas.create_rectangle(0, i6 ,336 , i6 + 1, fill = color2, outline = "")

        color3 = '#%02x%02x%02x' % (int(r1), int(g5), int(b1))
        r1 -= rdelta
        g5 -= gdelta3
        b1 -= bdelta
        
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0,i4, 336, i4 + 1, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0, i5 , 336 ,i5 +1 , fill = color3, outline = "")





#single slit blue


def colour_5 (canvas):
    global r1,g1,b1,r2,g2,b2,steps,rdelta,bdelta,gdelta,b6,b7,bdelta4
    r1 = 0
    g1 = 0
    b1 = 135
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    b6 = 150#i2&i7&i1&i8
    b7 = 0
    bdelta4 = (b6 - b7)/ float(steps/10)#new
    for i in range((steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
     
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r1), int(g1), int(b6))

        b6 -= bdelta4
       

        ia = steps/12 -i
        canvas.create_rectangle(0, ia, 336, ia + 1, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0, i0, 336, i0 + 1, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0, i1, 336, i1 + 1, fill = color4, outline = "")

        i2  = (steps/4)+ i 
        canvas.create_rectangle(0, i2, 336, i2 + 1, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0,i7, 336, i7 + 1, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0,i8, 336, i8 + 1, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0, i9 ,336, i9 + 1, fill = color, outline = "")

        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0,ilast,336,ilast + 1, fill = color, outline = "")

    r1 = 0
    r2 = 0

    g1 = 0
    g2 = 0

    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)

    b5 =  205
    b6 =  0
    bdelta3 = (b5 - b6)/ float(steps/10)

    b3 = 205 #color of middle blue
    b4 = 255 #color of middle blue
    bdelta2 = (b3 - b4)/ float(steps/10)#color of middle blue

    color2 = '#%02x%02x%02x' % (int(r1), int(g1), int(b3))#outside the function
    r1 -= rdelta
    b3 -= bdelta2
        
    for a in range((steps/12) + 1):
        i3  = (float(steps/2.4))+ a #middle blue
        canvas.create_rectangle(0, i3 ,336 ,i3 + 1,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a #middle blue
        canvas.create_rectangle(0, i6 ,336 , i6 + 1, fill = color2, outline = "")

        color3 = '#%02x%02x%02x' % (int(r1), int(g1), int(b5))
        r1 -= rdelta
        g1 -= gdelta
        b5 -= bdelta3
        
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0,i4, 336, i4 + 1, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0, i5 , 336 ,i5 +1 , fill = color3, outline = "")



#single slit indigo

def colour_6 (canvas):
    global r1,g1,b1,r2,g2,b2,steps,rdelta,bdelta,gdelta,b6,b7,bdelta4
    r1 = 75
    g1 = 0
    b1 = 180
     
    r2 = 0
    g2 = 0
    b2 = 0

    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)

    b6 = 150#i2&i7&i1&i8
    b7 = 0
    bdelta4 = (b6 - b7)/ float(steps/10)#new
    for i in range((steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
     
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r1), int(g1), int(b6))

        b6 -= bdelta4
       

        ia = steps/12 -i
        canvas.create_rectangle(0, ia, 336, ia + 1, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0, i0, 336, i0 + 1, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0, i1, 336, i1 + 1, fill = color4, outline = "")

        i2  = (steps/4)+ i 
        canvas.create_rectangle(0, i2, 336, i2 + 1, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0,i7, 336, i7 + 1, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0,i8, 336, i8 + 1, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0, i9 ,336, i9 + 1, fill = color, outline = "")

        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0,ilast,336,ilast + 1, fill = color, outline = "")


    r1 = 75
    r2 = 0

    g1 = 0
    g2 = 0

    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)

    b5 = 130
    b6 =  0
    bdelta3 = (b5 - b6)/ float(steps/10)

    b3 = 130 #color of middle indigo
    b4 = 130 #color of middle indigo
    bdelta2 = (b3 - b4)/ float(steps/10)#color of middle indigo

    color2 = '#%02x%02x%02x' % (int(r1), int(g1), int(b3))#outside the function
    r1 -= rdelta
    b3 -= bdelta2
        
    for a in range((steps/12) + 1):
        i3  = (float(steps/2.4))+ a #middle indigo
        canvas.create_rectangle(0, i3 ,336 ,i3 + 1,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a #middle indigo
        canvas.create_rectangle(0, i6 ,336 , i6 + 1, fill = color2, outline = "")

        color3 = '#%02x%02x%02x' % (int(r1), int(g1), int(b5))
        r1 -= rdelta
        g1 -= gdelta
        b5 -= bdelta3
        
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0,i4, 336, i4 + 1, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0, i5 , 336 ,i5 +1 , fill = color3, outline = "")




#single slit violet


def colour_7 (canvas):
    global r1,g1,b1,r2,g2,b2,steps,rdelta,bdelta,gdelta,g6,g7,gdelta4
    r1 = 238
    g1 = 40
    b1 = 238
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    g6 = 80#i2&i7&i1&i8
    g7 = 0
    gdelta4 = (g6 - g7)/ float(steps/10)#new
    for i in range((steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
     
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r1), int(g6), int(b1))

        g6 -= gdelta4
       

        ia = steps/12 -i
        canvas.create_rectangle(0, ia, 336, ia + 1, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0, i0, 336, i0 + 1, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0, i1, 336, i1 + 1, fill = color4, outline = "")

        i2  = (steps/4)+ i 
        canvas.create_rectangle(0, i2, 336, i2 + 1, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0,i7, 336, i7 + 1, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0,i8, 336, i8 + 1, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0, i9 ,336, i9 + 1, fill = color, outline = "")

        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0,ilast,336,ilast + 1, fill = color, outline = "")


    r1 = 238
    r2 = 0

    b1 = 238
    b2 = 0

    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)

    g5 = 130
    g6 =  0
    gdelta3 = (g5 - g6)/ float(steps/10)

    g3 = 130 #color of middle violet
    g4 = 130 #color of middle violet
    gdelta2 = (g3 - g4)/ float(steps/10)#color of middle violet

    color2 = '#%02x%02x%02x' % (int(r1), int(g3), int(b1))#outside the function
    r1 -= rdelta
    g3 -= gdelta2
        
    for a in range((steps/12) + 1):
        i3  = (float(steps/2.4))+ a #middle violet
        canvas.create_rectangle(0, i3 ,336 ,i3 + 1,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a #middle violet
        canvas.create_rectangle(0, i6 ,336 , i6 + 1, fill = color2, outline = "")

        color3 = '#%02x%02x%02x' % (int(r1), int(g5), int(b1))
        r1 -= rdelta
        g5 -= gdelta3
        b1 -= bdelta
        
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0,i4, 336, i4 + 1, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0, i5 , 336 ,i5 +1 , fill = color3, outline = "")

























        



