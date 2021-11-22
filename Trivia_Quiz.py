'''
Allow player to choose a category
Answer questions
Keep track of score
Create leaderboard
'''
import turtle as trtl
wn = trtl.Screen()

# Variables
painter = trtl.Turtle()
font = ("Arial", 50, "bold")
font_two = ("Arial", 50, "normal")


# Background Things
wn.bgcolor("light blue")
def make_background(painter):
    global font
    painter.speed(0)
    painter.hideturtle()
    painter.penup()
    painter.goto(-450,200)
    painter.write("Choose a category:", font=font)
    painter.goto(-350,125)
    painter.write("Press a to choose: Biology", font=font_two)
    painter.goto(-350, 50)
    painter.write("Press b to choose: Music", font=font_two)

# Methods
def category_A(painter):
    painter.clear()


def category_B(painter):
    painter.clear()


make_background(painter)
wn.onkeypress(category_A, "a")
wn.onkeypress(category_B, "b")



wn.listen()
wn.mainloop()