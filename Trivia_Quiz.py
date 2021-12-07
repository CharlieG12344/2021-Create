'''
Ensure all requirements are complete
Create leaderboard (Maybe)
Decorate
'''
import turtle as trtl
import random as rand
wn = trtl.Screen()

# Variables
painter = trtl.Turtle()
writer = trtl.Turtle()
scorekeeper = trtl.Turtle()
font = ("Arial", 50, "bold")
font_two = ("Arial", 50, "normal")
font_three = ("Arial", 25, "normal")
font_four = ("Arial", 25, "bold")
biology_list = ["What are the parts of a cell called?", "What gives blood it's red color?", "How many bones are in the body?"]
music_list = ["What does a staccato mean?", "How many beats does a whole note have?", "What is the sharp version of D flat?"]
mus_length = len(music_list)
bio_length = len(biology_list)
index = mus_length - 1
index_B = bio_length - 1
score = 0
color_list = ["blue", "White", "black", "Gray", "dark blue", "lavender"]
question_number = 0
question_number_mus = 0

# Background Things
wn.bgcolor("light blue")
def make_background(painter):
    global font
    painter.speed(0)
    painter.hideturtle()
    painter.penup()
    painter.goto(-300,200)
    painter.pencolor("dark blue")
    painter.write("Choose a category:", font=font)
    painter.goto(-375,50)
    painter.write("Press a to choose: Biology", font=font_two)
    painter.goto(-375,-150)
    painter.write("Press b to choose: Music", font=font_two)

# Methods

def category_Bio():
    global question_number
    painter.clear()
    writer.penup()
    question = biology_list.pop(index_B)
    writer.goto(-400, 200)
    writer.write(question, font=font_four)
    Bio_Questions()
    question_number += 1
    wn.onkeypress(score_change, "b")
    wn.onkeypress(bio_two, "c")
    wn.onkeypress(bio_two, "a")

def category_Mus():
    global question_number_mus
    mus_length = len(music_list)
    index = mus_length - 1
    painter.clear()
    writer.penup()
    question_two = music_list.pop(index)
    writer.goto(-400,200)
    writer.write(question_two, font=font_four)
    Mus_Questions()
    question_number_mus += 1
    wn.onkeypress(score_change, "c")
    wn.onkeypress(mus_two, "b")
    wn.onkeypress(mus_two, "a")

def bio_two():
    global question_number
    bio_length = len(biology_list)
    index_B = bio_length - 1
    writer.clear()
    question = biology_list.pop(index_B)
    writer.goto(-400, 200)
    writer.write(question, font=font_four)
    Bio_Questions()
    question_number += 1
    wn.onkeypress(score_change, "c")
    wn.onkeypress(bio_three, "b")
    wn.onkeypress(bio_three, "a")


def mus_two():
    global question_number_mus
    mus_length = len(music_list)
    index_A = mus_length - 1
    writer.clear()
    question_two = music_list.pop(index_A)
    writer.goto(-400, 200)
    writer.write(question_two, font=font_four)
    Mus_Questions()
    question_number_mus += 1
    wn.onkeypress(score_change, "b")
    wn.onkeypress(mus_three, "c")
    wn.onkeypress(mus_three, "a")

def mus_three():
    global question_number_mus, mus_length
    writer.clear()
    writer.goto(-400, 200)
    writer.write("What does a staccato mean?", font=font_four)
    Mus_Questions()
    question_number_mus += 1
    wn.onkeypress(score_change, "a")
    wn.onkeypress(end, "c")
    wn.onkeypress(end, "b")

def bio_three():
    global question_number
    writer.clear()
    writer.goto(-400, 200)
    writer.write("What are the parts of a cell called?", font=font_four)
    Bio_Questions()
    question_number += 1
    wn.onkeypress(score_change, "a")
    wn.onkeypress(end, "c")
    wn.onkeypress(end, "b")

def score_change():
    global score, color_list
    choice = rand.choice(color_list)
    if score <= 1:
        painter.pensize(5)
        painter.pencolor(choice)
        painter.goto(270,240)
        painter.pendown()
        painter.circle(50,360,10)
        painter.penup()
    scorekeeper.penup()
    scorekeeper.pencolor(choice)
    scorekeeper.goto(250,250)
    score += 1
    scorekeeper.clear()
    scorekeeper.write(score, font=font)
    if question_number == 1:
        bio_two()
    elif question_number_mus == 1:
        mus_two()
    elif question_number == 2:
        bio_three()
    elif question_number_mus == 2:
        mus_three()
    elif question_number == 3:
        end()
    elif question_number_mus == 3:
        end()


def Mus_Questions():
    writer.goto(-375,100)
    writer.write("A. A short note", font=font_three)
    writer.goto(-375, 50)
    writer.write("B. Four beats", font=font_three)
    writer.goto(-375, 0)
    writer.write("C. C sharp", font=font_three)

def Bio_Questions():
    writer.goto(-375,100)
    writer.write("A. Organelles", font=font_three)
    writer.goto(-375, 50)
    writer.write("B. 206", font=font_three)
    writer.goto(-375, 0)
    writer.write("C. Hemoglobin", font=font_three)

def end():
    global score, font
    writer.clear()
    painter.clear()
    scorekeeper.clear()
    scorekeeper.penup()
    writer.penup()
    scorekeeper.goto(-110, 100)
    scorekeeper.write("Your Score: " + str(score), font=font_four)
    if score == 3:
        painter.goto(-300, 200)
        painter.write("Congrats! You got every question correct.", font=font_three)
    elif score >= 1:
        painter.goto(-325, 200)
        painter.write("Congrats! You got some of the questions correct.", font=font_three)
    else:
        painter.goto(-275, 200)
        painter.write("You got none of the questions rights!", font=font_three)


scorekeeper.hideturtle()
writer.hideturtle()
make_background(painter)
wn.onkeypress(category_Bio, "a")
wn.onkeypress(category_Mus, "b")


wn.listen()
wn.mainloop()