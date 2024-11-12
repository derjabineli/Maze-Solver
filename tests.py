import unittest
from graphics import Window
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        screen_x = 800
        screen_y = 600
        win = Window(screen_x, screen_y)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_maze_create_cells1(self):
        screen_x = 600
        screen_y = 600
        win = Window(screen_x, screen_y)
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()