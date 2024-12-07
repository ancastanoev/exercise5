import turtle

# Define the points
points = [(-2, 7), (1, 10), (3, 8), (4, 10), (5, 7), (6, 7), (7, 11)]


# Function to calculate cross product to determine the turn direction
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


# Andrew's variant of Graham's scan for the lower hull
def lower_hull(points):
    # Sort points by x-coordinate (then by y-coordinate)
    points = sorted(points)

    # Initialize the lower hull
    lower = []

    for p in points:
        # Remove points that do not make a counter-clockwise turn
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    return lower


# Visualization function using turtle
def visualize(points, lower_hull):
    # Set up the turtle window
    screen = turtle.Screen()
    screen.setworldcoordinates(-3, -1, 8, 12)  # Adjust for better view

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()

    # Draw points and display their coordinates
    for x, y in points:
        pen.goto(x, y)
        pen.dot(10, "red")
        pen.goto(x, y + 0.2)
        pen.write(f"({x},{y})", align="center", font=("Arial", 8, "normal"))

    # Draw the evolving lower hull
    pen.goto(lower_hull[0][0], lower_hull[0][1])
    pen.pendown()
    pen.pensize(2)
    pen.color("blue")

    for point in lower_hull[1:]:
        pen.goto(point[0], point[1])


    pen.penup()
    pen.goto(0, -2)
    pen.write("Lower Hull", align="center", font=("Arial", 16, "normal"))

    turtle.done()


# Find the lower hull using Andrew's algorithm
lower_hull_points = lower_hull(points)

# Print the lower hull
print("Lower Hull:", lower_hull_points)

# Visualize using turtle
visualize(points, lower_hull_points)
