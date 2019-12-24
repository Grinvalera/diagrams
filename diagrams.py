from turtle import Turtle, Screen
from itertools import cycle


letter_frequencies = [('python', 50.0), ('assembler', 10.0), ('objective-c', 15.0), ('html', 2.0)]

COLORS = cycle(['green', 'orange', 'pink', 'purple'])

RADIUS = 175
LABEL_RADIUS = RADIUS * 1.33
FONTSIZE = 18
FONT = ("Ariel", FONTSIZE, "bold")


total = sum(fraction for _, fraction in letter_frequencies)

baker = Turtle()
baker.penup()
baker.sety(-RADIUS)
baker.pendown()

for _, fraction in letter_frequencies:
    baker.fillcolor(next(COLORS))
    baker.begin_fill()
    baker.circle(RADIUS, fraction * 360 / total)
    position = baker.position()
    baker.goto(0, 0)
    baker.end_fill()
    baker.setposition(position)


baker.penup()
baker.sety(-LABEL_RADIUS)

for label, fraction in letter_frequencies:
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    baker.write(label, align="center", font=FONT)
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)

baker.hideturtle()

screen = Screen()
screen.exitonclick()