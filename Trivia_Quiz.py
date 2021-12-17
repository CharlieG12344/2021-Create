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
score = 0
color_list = ["blue", "white", "black", "gray", "dark blue", "lavender", "purple"]
question_bio = 4
question_mus = 4
number_b = 0
number = 0

# Background Things
wn.bgcolor("light blue")
def make_background(painter):
    global font
    scorekeeper.hideturtle()
    writer.hideturtle()
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

def Questions (type):
    global question_bio, number_b, question_mus, number
    if (type == "a"):
     if number_b <= 0:
        painter.clear()
     while question_bio > 3:
        writer.clear()
        writer.penup()
        question = biology_list[number_b]
        number_b += 1
        writer.goto(-400, 200)
        writer.write(question, font=font_four)
        Bio_Questions()
        if question_bio == 4:
            question_bio -= 1
            wn.onkeypress(score_change, "a")
            wn.onkeypress(bio_score, "b")
            wn.onkeypress(bio_score, "c")
            wn.onkeypress(bio_score, "d")
        if question_bio == 5:
            question_bio -= 5
            wn.onkeypress(score_change, "c")
            wn.onkeypress(bio_score, "a")
            wn.onkeypress(bio_score, "b")
            wn.onkeypress(bio_score, "d")
        if question_bio == 6:
            question_bio -= 3
            wn.onkeypress(score_change, "b")
            wn.onkeypress(end, "c")
            wn.onkeypress(end, "a")
            wn.onkeypress(end, "d")
    elif (type == "b"):
        if number <= 0:
            painter.clear()
        while question_mus > 3:
            writer.clear()
            writer.penup()
            question = music_list[number]
            number += 1
            writer.goto(-400, 200)
            writer.write(question, font=font_four)
            Mus_Questions()
            if question_mus == 4:
                question_mus -= 1
                wn.onkeypress(score_change, "a")
                wn.onkeypress(mus_score, "b")
                wn.onkeypress(mus_score, "c")
                wn.onkeypress(mus_score, "d")
            if question_mus == 5:
                question_mus -= 5
                wn.onkeypress(score_change, "b")
                wn.onkeypress(mus_score, "a")
                wn.onkeypress(mus_score, "c")
                wn.onkeypress(mus_score, "d")
            if question_mus == 6:
                question_mus -= 3
                wn.onkeypress(score_change, "c")
                wn.onkeypress(end, "a")
                wn.onkeypress(end, "b")
                wn.onkeypress(end, "d")

def bio_score ():
    global question_bio, number_b
    if number_b == 1:
        question_bio += 2
        Questions(type)
    if number_b == 2:
        question_bio += 3
        Questions(type)
    else:
        end()

def mus_score ():
    global question_mus, number
    if number == 1:
        question_mus += 2
        Questions(type)
    if number == 2:
        question_mus += 3
        Questions(type)
    else:
        end()

def score_change():
    global score, color_list, question_bio, question_mus
    choice = rand.choice(color_list)
    if score <= 1:
        painter.pensize(5)
        painter.pencolor(choice)
        painter.goto(295,240)
        painter.pendown()
        painter.circle(50,360,10)
        painter.penup()
    scorekeeper.penup()
    scorekeeper.pencolor(choice)
    scorekeeper.goto(275,250)
    score += 1
    scorekeeper.clear()
    scorekeeper.write(score, font=font)
    if number_b == 1:
        question_bio += 2
        Questions(type)
    elif number == 1:
        question_mus += 2
        Questions(type)
    elif number_b == 2:
        question_bio += 3
        Questions(type)
    elif number == 2:
        question_mus += 3
        Questions(type)
    elif number_b == 3:
        end()
    elif number == 3:
        end()

def Mus_Questions():
    writer.goto(-375,100)
    writer.write("A. A short note", font=font_three)
    writer.goto(-375, 50)
    writer.write("B. Four beats", font=font_three)
    writer.goto(-375, 0)
    writer.write("C. C sharp", font=font_three)
    writer.goto(-375, -50)
    writer.write("D. Other", font=font_three)

def Bio_Questions():
    writer.goto(-375,100)
    writer.write("A. Organelles", font=font_three)
    writer.goto(-375, 50)
    writer.write("B. 206", font=font_three)
    writer.goto(-375, 0)
    writer.write("C. Hemoglobin", font=font_three)
    writer.goto(-375, -50)
    writer.write("D. Other", font=font_three)

def end():
    global score, font
    writer.clear()
    painter.clear()
    scorekeeper.clear()
    scorekeeper.penup()
    writer.penup()
    scorekeeper.goto(-120, 100)
    scorekeeper.write("Your Score: " + str(score) + " / 3", font=font_four)
    if score == 3:
        painter.goto(-300, 200)
        painter.write("Congrats! You got every question correct.", font=font_three)
    elif score >= 1:
        painter.goto(-325, 200)
        painter.write("Congrats! You got some of the questions correct.", font=font_three)
    else:
        painter.goto(-275, 200)
        painter.write("You got none of the questions rights!", font=font_three)

#Calling Methods

make_background(painter)
type = input("Choose a Category:")
Questions(type)
wn.listen()
wn.mainloop()