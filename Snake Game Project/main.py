import traceback

def run():
    from turtle import Turtle, Screen
    import random
    import time

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    # create snake
    segment = []
    positions = [(0, 0), (-20, 0), (-40, 0)]

    for position in positions:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segment.append(new_segment)

    # snake movement directions
    def go_up():
        if segment[0].heading() != 270:
            segment[0].setheading(90)

    def go_down():
        if segment[0].heading() != 90:
            segment[0].setheading(270)

    def go_left():
        if segment[0].heading() != 0:
            segment[0].setheading(180)

    def go_right():
        if segment[0].heading() != 180:
            segment[0].setheading(0)

    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")

    # create food at a random position
    food = Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.shapesize(0.5, 0.5)
    food.speed("fastest")
    food.goto(random.randint(-280, 280), random.randint(-280, 280))

    # score display
    score = 0
    scoreboard = Turtle()
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, 260)
    scoreboard.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.2)

        # move snake body
        for seg in range(len(segment) - 1, 0, -1):
            new_x = segment[seg - 1].xcor()
            new_y = segment[seg - 1].ycor()
            segment[seg].goto(new_x, new_y)

        segment[0].forward(20)

        # detect food collision
        if segment[0].distance(food) < 15:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            # add new segment at the tail
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(segment[-1].position())
            segment.append(new_segment)

            # update score
            score += 1
            scoreboard.clear()
            scoreboard.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

        # detect wall collision
        if (
            segment[0].xcor() > 290
            or segment[0].xcor() < -290
            or segment[0].ycor() > 290
            or segment[0].ycor() < -290
        ):
            game_is_on = False

        # detect self collision
        for seg in segment[1:]:
            if segment[0].distance(seg) < 10:
                game_is_on = False

    # game over screen — stays open for 3 seconds then closes
    scoreboard.goto(0, 0)
    scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    scoreboard.goto(0, -40)
    scoreboard.write(f"Final Score: {score}", align="center", font=("Arial", 18, "normal"))
    screen.update()
    screen.update()
    screen.exitonclick() 
try:
    run()
except Exception as e:
    if "bye" not in str(e).lower() and "destroy" not in str(e).lower():
        input("ERROR:\n\n" + traceback.format_exc() + "\n\nPress Enter to close...")