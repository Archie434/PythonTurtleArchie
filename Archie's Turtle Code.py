import turtle # runs turtle

# makes the canvas 400x400, the 422x422 is because the window top and
# sidebar take up window space that needs to be accounted for along with
# the turtle's size
turtle.setup(422,422)

turtle.shape("classic") # makes the turtle an easier to work with arrow shape
turtle.speed(10) # makes the turtle faster
turtle.width(2) # makes the turtle draw in thicker width

# a function that I use to test if my measurements are correct by moving
# the turtle out if the way. This won't be in the final code
def test():
    turtle.penup()
    turtle.forward(36)
    turtle.pendown()

# a function that teleports the turtle without it drawing
def tp(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

# a function that lets me make squares and rectangles with one line of code
def square(a,b,c,d):
    tp(a,b)
    turtle.begin_fill()
    turtle.goto(a,c)
    turtle.goto(d,c)
    turtle.goto(d,b)
    turtle.goto(a,b)
    turtle.end_fill()

# similar to the 'square' function, lets me make circles with one line of code
def circle(x,a,b,c,d,e,f):
    turtle.right(x)
    turtle.fillcolor(a) # sets the fill colour
    turtle.begin_fill() # starts filling
    tp(b,c)
    turtle.circle(d,e)
    turtle.goto(f)
    turtle.end_fill() # stops filling

# 2 objects in the image have 2 curved sides and 2 straight sides, meaning I can use a function
# to make the code more effecient
def doublecurve(a,b,c,d,e,f,x,y,g,h,z,k,i):
    tp(a,b)
    turtle.begin_fill()
    turtle.goto(a,c)
    turtle.seth(d)
    while turtle.xcor() < e:
        turtle.circle(f,x,y)
    turtle.seth(g)
    while turtle.ycor() < b:
        turtle.circle(h,z,k)
    turtle.goto(a,i)
    turtle.end_fill()

# a function that lets me input 3 values and draws a horizontal line
def hline(x,y,z):
    tp(x,z)
    turtle.goto(y,z)

# a function that lets me input 3 values and draws a vertical line
def vline(x,y,z):
    tp(z,x)
    turtle.goto(z,y)

turtle.left(90) # puts the turtle in the correct starting position

# the 'fill color' command changes the colour that the turtle is filling in. Although the colour
# was directly eye droped from the image, every single colour in my image is slightly less saturated.
# I have tried to overcorrect for this, but it seems its a quirk of turtle that cannot be fixed
turtle.fillcolor('#2E4F8F')

square(141,200,-200,-141) # creates the border of the image

circle(90,'#EFB34F',0,-119,125,360,(-0.00,-119.00)) # creates the center circle
circle(180,'#FFFFFF',141,148,141,180,(141,148)) # creates the right circle
circle(0,'#FFFFFF',-141,149,-141,180,(-141,149)) # creates the left circle

turtle.fillcolor("#C82B1E") # sets the fill colour to red.

# each block of code under here is a new
# red shape until a fill colour change. By drawing shapes of the same
# colour one after the other I save a few lines due to not having to
# switch fill colours as much
square(51,38,-2,141)

tp(14,67)
turtle.seth(244.82)
turtle.begin_fill()
while turtle.ycor() > -54:
    turtle.circle(141,1,1)
turtle.goto(14,67)
turtle.end_fill()

square(-100,38,-42,-23)

doublecurve(-90,-80,-80,313.28,-57.5,125,1,1,37.17,141,1,1,-79) # use of the doublecure function

turtle.fillcolor("#2A27D4") # sets the fill colour to blue (a more vibrant blue than the background)

# each block of code under here is a new blue shape until a fill colour change
tp(93,39)
turtle.begin_fill()
turtle.goto(93,88.5)
tp(93,89)
turtle.seth(131.93)
while turtle.xcor() > 55:
    turtle.circle(125,0.5,1)
turtle.seth(217.58)
while turtle.xcor() > 14:
    turtle.circle(141,0.5,1)
turtle.goto(14,39)
turtle.end_fill()

# explanation of how the 'sector method' works
turtle.seth(270)
tp(-23,-2)
turtle.left(90)
turtle.begin_fill()
turtle.goto(0,-2)
turtle.left(87.15) # locks the turtle to the angle it needs to be in to start drawing the curved side
while turtle.xcor() > -22:  # -22 is the coordinate where the turtle stops drawing the curved side
    turtle.circle(141,1,1)  # draws 1 degree sectors over until it reaches -22
turtle.goto(-23,-2)
turtle.end_fill()

doublecurve(51,-82,-102,308.1,54,141,0.5,1,27.13,125,0.5,1,-82)

turtle.fillcolor('#EFB34F') # sets the fill colour to orange.

# each block of code under here is a new orange shape until a fill colour change.
tp(-100,38)
turtle.begin_fill()
turtle.goto(-120,38)
turtle.seth(254.22)
while turtle.xcor() < -100:
    turtle.circle(122,1,1)
turtle.goto(-100,-63)
turtle.goto(-100,38)
turtle.end_fill()

tp(-63,38)
turtle.begin_fill()
turtle.goto(-63,113)
turtle.seth(210.23)
while turtle.xcor() > -120.45:
    turtle.circle(125,1,1)
turtle.goto(-119,38)
turtle.goto(-63,38)
turtle.end_fill()

# creates the horizontal lines of the image. Each new 'hline' is a new horizontal line
hline(-119,-141,38)
hline(141,94,78)
hline(141,16,38)
hline(141,51,-82)
hline(-1,-23,-2)
hline(-141,-10,-42)
hline(-100,-33,-79)

# creates the vertical lines of the image. Each new 'vline' is a new vertical line
vline(80,84,-23)
vline(38,-126,-100)
vline(38,124,-63)
vline(38,-101,51)
vline(39,138,93)

# re-draws center circle on the top of the image
turtle.seth(270)
tp(0,-119)
turtle.left(90)
turtle.circle(125,360)
turtle.right(90)

turtle.hideturtle() # hides the turtle to make the image easier to see
turtle.done() # ends the program
