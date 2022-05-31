from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1
        
    # Initializing the movement of ball diagonally
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x,new_y)

    # To make the ball bounce from top and down walls of y-axis we need to reverse the value of y
    def bounce_y(self):
        self.y_move *= -1

    # TO make the ball bounce from both paddles i.e x-axis we need to reverse the value of x
    def bounce_x(self):
        self.x_move *= -1
        self.movement_speed *= 0.9

    # Reset the ball to the center of the screen after any player misses it and serve it in opposite direction of losing side
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.movement_speed = 0.1

