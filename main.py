from graphics import Window
from maze import Maze


def main():
    try:
        num_rows = int(input("How many rows would you like your maze to be? "))
    except ValueError:
        print("Row size must be an integer")
    try:
        num_cols = int(input("How many columns would you like your maze to be? "))
    except ValueError:
        print("Column size must be an integer")
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()


main()
