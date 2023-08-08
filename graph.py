import json
import math


def main():
    file = json.loads(str(open("graphs.json", "r")))
    functions = file["functions"]
    x1 = file["x_min"]
    x2 = file["x_max"]
    y1 = file["y_min"]
    y2 = file["y_max"]

    y_list_list = []
    width = 100
    height = 20

    for func in functions:
        y_list = []
        for x in range(width):
            y = eval(func.replace("x", f"({str(x1 + x * (x2 - x1) / width)})"))
            y_list.append(y)
        y_list_list.append(y_list)

    for y in range(height):
        for x in range(width):
            x_zero = int(-x1 / (x2 - x1) * width)
            y_zero = int(-y1 / (y2 - y1) * height)
            draw = " "
            isline = False
            for y_list in y_list_list:
                if height - y == int((y_list[x] - y1) / (y2 - y1) * height):
                    isline = True
            if isline:
                draw = "#"
            elif x == x_zero and height - y == y_zero:
                draw = "+"
            elif x == x_zero:
                draw = "|"
            elif height - y == y_zero:
                draw = "-"

            print(draw, end="" if x < width - 1 else "\n")


while True:

    main()
