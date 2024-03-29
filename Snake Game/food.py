import random
import turtle

ALIGN, FONT = "center", ("Arial", 14, "bold")


class Food(turtle.Turtle):

    def __init__(self, color="green") -> None:
        super().__init__(shape="circle")
        self.shapesize(0.8, 0.8)
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        while True:
            x_random = random.uniform(-280.0, 280.0)
            y_random = random.uniform(-280.0, 250.0)
            food_pos = (x_random, y_random)
            if all(element.distance(food_pos) > 20 for element in turtle.turtles() if not isinstance(element, Food)):
                break

        self.goto(x_random, y_random)