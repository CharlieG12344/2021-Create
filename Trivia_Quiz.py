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
scorekeeper = trtl.Turtle()
font = ("Arial", 50, "bold")
font_two = ("Arial", 50, "normal")
font_three = ("Arial", 25, "normal")
biology_list = ["What are the parts of a cell called?", "What gives blood it's red color?", "How many bones are in the body?"]
music_list = ["What does a staccato mean?", "How many beats does a whole note have?", "What is the sharp version of D flat?"]
mus_length = len(music_list)
bio_length = len(biology_list)
index = mus_length - 1
index_B = bio_length - 1
score = 0
x = 0


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
    #while x < 3:
    writer.penup()
    question = biology_list.pop(index_B)
    writer.goto(-400, 200)
    writer.write(question, font=font_three)
    Bio_Questions()
    wn.onkeypress(score_change, "b")

def category_Mus():
    painter.clear()
    x = 0
    while x < 3:
        writer.penup()
        question_two = music_list.pop(index)
        writer.goto(-400,200)
        writer.write(question_two, font=font_three)
        Mus_Questions()
        wn.onkeypress(score_change, "c")

def score_change():
    global score, x
    scorekeeper.penup()
    scorekeeper.goto(225,250)
    score += 1
    scorekeeper.clear()
    scorekeeper.write(score, font=font)
    x += 1

def Mus_Questions():
    writer.goto(-375,50)
    writer.write("A. A short note", font=font_three)
    writer.goto(-375, -25)
    writer.write("B. Four beats", font=font_three)
    writer.goto(-375, -100)
    writer.write("C. C sharp", font=font_three)

def Bio_Questions():
    writer.goto(-375,50)
    writer.write("A. Organelles", font=font_three)
    writer.goto(-375, -25)
    writer.write("B. 206", font=font_three)
    writer.goto(-375, -100)
    writer.write("C. Hemoglobin", font=font_three)

def end():
    global score, font
    writer.clear()
    painter.goto(-300, 200)
    if score == 3:
        painter.write("Congrats! You got every question correct.", font=font)
    elif score >= 1:
        painter.write("Congrats! You got some of the questions correct", font=font)
    else:
        painter.write("You got none od the questions rights.", font=font)


scorekeeper.hideturtle()
writer.hideturtle()
make_background(painter)
wn.onkeypress(category_Bio, "a")
wn.onkeypress(category_Mus, "b")
end()



wn.listen()
wn.mainloop()