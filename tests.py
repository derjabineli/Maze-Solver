import unittest
from graphics import Window
from maze import Maze

class Tests(unittest.TestCase):
    
    # def test_maze_create_cells(self):
    #     screen_x = 800
    #     screen_y = 600
    #     win = Window(screen_x, screen_y)
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_rows,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_cols,
    #     )
    
    # def test_maze_create_cells1(self):
    #     screen_x = 600
    #     screen_y = 600
    #     win = Window(screen_x, screen_y)
    #     num_cols = 10
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_rows,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_cols,
    #     )
    
    # def test_maze_entrance(self):
    #     screen_x = 800
    #     screen_y = 600
    #     win = Window(screen_x, screen_y)
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
    #     self.assertEqual(
    #         m1._cells[0][0].has_left_wall,
    #         False,
    #     )

    # def test_maze_exit(self):
    #     screen_x = 800
    #     screen_y = 600
    #     win = Window(screen_x, screen_y)
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
    #     self.assertEqual(
    #         m1._cells[9][11].has_bottom_wall,
    #         False,
    #     )
    def test_visited_reset(self):
        screen_x = 800
        screen_y = 600
        win = Window(screen_x, screen_y)
        num_cols = 4
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(m1._cells[i][j].visited, False)
    
    def test_visited_reset2(self):
        screen_x = 800
        screen_y = 600
        win = Window(screen_x, screen_y)
        num_cols = 10
        num_rows = 14
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(m1._cells[i][j].visited, False)

if __name__ == "__main__":
    unittest.main()