
import numpy as np


def main(file):
    sodoku_array = [[0]*9 for i in range(9)]
    file_txt = open(file)
    row = 0
    column = 0
    not_digit = True
    for line in file_txt:
        string = line.split()
        for i in string:
            if i == ".":
                sodoku_array[column][row] = 0
                row += 1
                not_digit = False
            elif not i.isdigit():
                not_digit = True
                continue
            else:
                sodoku_array[column][row] = int(i)
                row += 1
                not_digit = False
        if not_digit:
            row = 0
            continue
        else:
            column += 1
            row = 0

    for x in sodoku_array:
        print(x)


if __name__ == "__main__":
    file = "sodoku.txt"
    main(file)
