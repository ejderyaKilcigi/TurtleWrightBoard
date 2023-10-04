import turtle

writeBoard = turtle.Screen()
writeBoard.title("Interactive Write Board")
writeBoard.bgcolor("pink")

lion = turtle.Turtle()

writeBoard.listen()

def goForrestGooo():
    lion.forward(50)

def toTheLeft():
    lion.left(30)

def toTheRight():
    lion.right(30)

def boardClear():
    lion.clear()

def returnHome():
    lion.penup()
    lion.home()
    lion.pendown()



writeBoard.onkey(goForrestGooo, "Up")
writeBoard.onkey(toTheLeft, "Left")
writeBoard.onkey(toTheRight, "Right")
writeBoard.onkey(boardClear, "space")
writeBoard.onkey(returnHome, "h")



turtle.done()

