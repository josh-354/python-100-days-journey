import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout Clone")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off screen updates for manual control

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Ball speed in x direction
ball.dy = -2  # Ball speed in y direction

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-5, 6):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x * 50, 250 - y * 20)
        bricks.append(brick)

# Score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddle
def paddle_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 250:
        x += 20
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
    
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    # Ball falls below paddle (game over)
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        score = 0
        score_display.clear()
        score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        time.sleep(1)  # Pause briefly
    
    # Paddle and ball collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-230)
        ball.dy *= -1
    
    # Ball and brick collision
    for brick in bricks:
        if brick.isvisible():
            if (ball.xcor() > brick.xcor() - 40 and ball.xcor() < brick.xcor() + 40) and (ball.ycor() > brick.ycor() - 10 and ball.ycor() < brick.ycor() + 10):
                brick.hideturtle()
                ball.dy *= -1
                score += 10
                score_display.clear()
                score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    
    # Check if all bricks are broken
    if all(not brick.isvisible() for brick in bricks):
        score_display.clear()
        score_display.write("You Win!", align="center", font=("Courier", 24, "normal"))
        break
    
    time.sleep(0.01)  # Control game speed

wn.mainloop()
