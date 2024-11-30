import turtle


mandala = turtle.Turtle()

window = turtle.Screen()


turtle.title("Mandala na matiku")
turtle.bgcolor("#2c3e50")
mandala.speed(10000)
turtle.speed(100000)
n = 100

def drawMandala(n):

  for i in range(n):

      turtle.penup()
      turtle.forward(100)
      turtle.left(90)
      turtle.penup()
      turtle.forward (30)
      turtle.left (90)
      turtle.pendown()
      turtle.pencolor ("#27ae60")
      turtle.forward (60)
      turtle.pencolor("#d35400")
      turtle.right (70)
      turtle.forward (70)
      turtle.right (40)
      turtle.forward (50)
      turtle.pencolor ("#c0392b")
      turtle.left (90)
      turtle.pensize(5)
      turtle.forward (100)
      turtle.pencolor("#2980b9")
      turtle.left(90)
      turtle.forward (100)
      turtle.right (50)
      turtle.forward (70)
      turtle.pensize(10)
      turtle.left (60)
      turtle.pensize(6)
      turtle.forward (65)
      turtle.left (45)
      turtle.forward (120)


drawMandala(n)
window.exitonclick()