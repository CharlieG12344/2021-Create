'''
Allow player to choose a category
Answer questions
Keep track of score
Create leaderboard
'''
import turtle as trtl
import random as rand
wn = trtl.Screen()

# Variables
painter = trtl.Turtle()
writer = trtl.Turtle()
font = ("Arial", 50, "bold")
font_two = ("Arial", 50, "normal")
biology_list = ["What are the parts of a cell called?", "What gives blood it's red color?", "How many bones are in the body?"]
music_list = ["What does a staccato do?", "How many beats does a whole note have?", "What is the sharp version of D flat?"]

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
def category_Bio(biology):
    painter.clear()
    writer.write(biology, font=font_two)


def category_Mus():
    painter.clear()


writer.hideturtle()
make_background(painter)
wn.onkeypress(category_Bio, "a")
wn.onkeypress(category_Mus, "b")



wn.listen()
wn.mainloop()