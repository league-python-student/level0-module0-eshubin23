import turtle
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def set_background(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)


class Eye:
    def __init__(self, eye=None, x=0, y=0, radius=30):
        self.eye = eye
        self.x = x
        self.y = y
        self.radius = radius
        
        self.eye.penup()
        
    def draw(self):
        self.eye.begin_fill()
        self.eye.goto(self.x, self.y)
        self.eye.circle(radius=self.radius, steps=20)
        self.eye.end_fill()

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def key_pressed():
    print('You pressed the space key')
    
    # LASER BEAM.  This code will make your ellipse move down and to the right
    # when you press the space bar. Run the program to test it.

    # 10. Increment the x and y variables of the 2 eye variables by 5:
    left_eye.x += 5
    right_eye.x += 5
    # 11. Call the .draw() method for both eye variables.
    right_eye.draw()

if __name__ == '__main__':
    window = turtle.Screen()
    
    # 1. Find an image of a cat with BIG eyes OR use one of the 2 images provided
    #    a. Find an image using google to search. The image must be a .gif file
    #    b. Right click on the image and select 'Save image As'
    #    c. Rename the image something short (e.g. cat.gif)
    #    d. Save the image to your computer's desktop
    #    e. Drag and drop the image into this python package
    bg_image = 'bigEyedCat2.gif'
    # 2. Call the set_background() function with your variable inside of the parenthesis
    #    for example, set_background(https://github.com/league-python-student/level0-module0-eshubin23.gitbg_image)
    set_background(bg_image)
    # 3. Make a new turtle
    hi=turtle.Turtle()
    # 4. Set the turtle color and pen color to red (or any color you want)
    #    using .color('red', 'red')
    hi.color('red', 'red')
    # 5. Set the turtle width to 0 so no outlines are drawn
    hi.width(0)
    # 6. Set the turtle speed to 0 (fastest)
    hi.speed(0)
    # 7. Run the program and click on one of the cat's eyes. 
    #    The x,y position of the eye will be printed at the bottom of your
    #    processing window.
    #    Variables for x and y have been created at the top of your sketch, 
    #    now you can set them equal to the values you just found. Watch for
    #    negative signs!
    x= -53.0
    y=65.0

    x2=7.0
    y2=58.8

    # 8. After you've found the x and y for the eyes create 2 eye variables
    #    and initialize them:
    left_eye  = Eye(eye=hi, x=x, y=y, radius=30)
    right_eye = Eye(eye=hi, x=x2, y=y2, radius=30)

    # 9. Call the .draw() method on BOTH eye variables
    left_eye.draw()

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    window.onkeypress(key_pressed, 'space')
    window.listen()
    turtle.done()
