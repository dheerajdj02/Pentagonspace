#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

import math
x, y = 0, 0
while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT and step number: ")
    if step == "":
        break
    else:
        step = step.split(" ")
        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])
dis = math.sqrt(x**2 + y**2)
print("Distance:", dis)
