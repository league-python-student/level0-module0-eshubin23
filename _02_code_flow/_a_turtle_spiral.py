import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    hello=turtle.Turtle()
    # This code sets our shape to a turtle
    hello.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    hello.speed(10)
    # Set your turtle's color using .color('green')
    hello.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        # Set the turtle color to a random color
        hello.color(get_random_color())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        hello.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        hello.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
