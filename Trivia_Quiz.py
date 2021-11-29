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
font_three = ("Arial", 25, "normal")
biology_list = ["What are the parts of a cell called?", "What gives blood it's red color?", "How many bones are in the body?"]
music_list = ["What does a staccato mean?", "How many beats does a whole note have?", "What is the sharp version of D flat?"]
bio_length = len(biology_list)
bio_index = rand.randint(0,bio_length)
mus_length = len(music_list)
mus_index = rand.randint(0,mus_length)


# Background Things
wn.bgcolor("light blue")
def make_background(painter):
    global font
    painter.speed(0)
    painter.hideturtle()
    painter.penup()
    painter.goto(-300,200)
    painter.write("Choose a category:", font=font)
    painter.goto(-375,50)
    painter.write("Press a to choose: Biology", font=font_two)
    painter.goto(-375,-150)
    painter.write("Press b to choose: Music", font=font_two)

# Methods

def category_Bio():
    painter.clear()
    x = 0
    while x < 3:
        writer.penup()
        question = biology_list.pop(bio_index)
        writer.goto(-375, 200)
        writer.write(question, font=font)
        Bio_Questions()

        writer.clear()
        x += 1





def category_Mus():
    painter.clear()
    x = 0
    while x < 3:
        writer.penup()
        question_two = music_list.pop(mus_index)
        writer.goto(-375,200)
        writer.write(question_two, font=font)
        Mus_Questions()
        if a
        writer.clear()
        x += 1

def Mus_Questions():
    writer.goto(-375,50)
    writer.write("A. A short note", font=font_two)
    writer.goto(-375, 25)
    writer.write("B. Four beats", font=font_two)
    writer.goto(-375, 0)
    writer.write("C. C sharp", font=font_two)

def Bio_Questions():
    writer.goto(-375,50)
    writer.write("A. Organelles", font=font_two)
    writer.goto(-375, 25)
    writer.write("B. Hemoglobin", font=font_two)
    writer.goto(-375, 0)
    writer.write("C. 206", font=font_two)

writer.hideturtle()
make_background(painter)
wn.onkeypress(category_Bio, "a")
wn.onkeypress(category_Mus, "b")



wn.listen()
wn.mainloop()