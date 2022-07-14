def circle_print(num_grid):
    result = []
    row = len(num_grid)
    column = len(num_grid[0])
    size = row * column
    x_max = row - 1
    y_max = column - 1
    x_min = 0
    y_min = 0
    x = x_min
    y = y_min
    while len(result) != size:
        if x == x_min and y == y_min:
            for y in range(y, y_max + 1):
                result.append(num_grid[x][y])
            x_min += 1
            x += 1
        elif x == x_min and y == y_max:
            for x in range(x, x_max + 1):
                result.append(num_grid[x][y])
            y_max -= 1
            y -= 1
        elif x == x_max and y == y_max:
            for y in range(y, y_min - 1, -1):
                result.append(num_grid[x][y])
            x_max -= 1
            x -= 1
        elif x == x_max and y == y_min:
            for x in range(x, x_min - 1, -1):
                result.append(num_grid[x][y])
            y_min += 1
            y += 1
    return result


def main():
    num_grid = [
        [1, 6, 11, 16],
        [2, 7, 12, 17],
        [3, 8, 13, 18],
        [4, 9, 14, 19],
    ]
    circle_list = circle_print(num_grid)
    print(circle_list)


if __name__ == "__main__":
    main()
