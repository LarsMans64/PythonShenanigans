import json
import math
import os
import time


def main():
    file = json.loads(open("graphs.json", "r").read())
    functions: list[str] = file["functions"]
    x1: float = file["x_min"]
    x2: float = file["x_max"]
    y1: float = file["y_min"]
    y2: float = file["y_max"]

    y_list_list = []
    width = 100
    height = 20

    for func in functions:
        y_list = []
        for x in range(width):
            try:
                y = eval(func.replace("x", f"({x1 + x * (x2 - x1) / width})"))
                y_list.append(y)
            except ArithmeticError:
                y_list.append("nope")
        y_list_list.append(y_list)

    for y in range(height):
        for x in range(width):
            x_zero = int(-x1 / (x2 - x1) * width)
            y_zero = int(-y1 / (y2 - y1) * height)
            draw = " "
            is_line = False
            for y_list in y_list_list:
                if not isinstance(y_list[x], float):
                    continue
                if height - y == int((y_list[x] - y1) / (y2 - y1) * height):
                    is_line = True
            if is_line:
                draw = "#"
            elif x == x_zero and height - y == y_zero:
                draw = "+"
            elif x == x_zero:
                draw = "|"
            elif height - y == y_zero:
                draw = "-"

            print(draw, end="" if x < width - 1 else "\n")


while True:
    os.system("cls")
    print()
    main()
    time.sleep(1)
