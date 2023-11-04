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
    width = 120
    height = 27

    for func in functions:
        y_list = []
        for x in range(width):
            try:
                y = eval(func.replace("_x", f"({x1 + x * (x2 - x1) / width})").replace("_t", str(time.time() - t)))
                y_list.append(y)
            except ArithmeticError:
                y_list.append("nope")
        y_list_list.append(y_list)

    frame = ""
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

            if x == width - 1:
                draw = draw + "\n"
            frame = frame + draw
    print(frame)


pi = math.pi  # just to use the import somewhere
t = time.time()

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Time:", round(time.time() - t, 2))
    main()
    time.sleep(0.04)

# TODO:
#  numbers on axes on edges of screen
