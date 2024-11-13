import time
import random
from cell import Cell

class Maze():
    def __init__(
       self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for x in range(self._num_cols)] for y in range(self._num_rows)]
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        x1 = self.x1 + (j * self._cell_size_x)
        y1 = self.y1 + (i * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Left Cell
            if j > 0 and self._cells[i][j - 1].visited == False:
                to_visit.append([i, j-1])
            # Right Cell
            if j < self._num_cols - 1 and self._cells[i][j + 1].visited == False:
                to_visit.append([i, j + 1])
            # Top Cell
            if i > 0 and self._cells[i - 1][j].visited == False:
                to_visit.append([i - 1, j])
            # Bottom Cell
            if i < self._num_rows - 1 and self._cells[i + 1][j].visited == False:
                to_visit.append([i + 1, j])
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = random.choice(to_visit)
            # I J is above direction
            if direction[0] > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            # I J is below direction
            if direction[0] < i:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            # I J is to the left of direction
            if direction[1] > j:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            # I J is to the right of direction
            if direction[1] < j:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            self._break_walls_r(direction[0], direction[1])
            
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[self._num_rows - 1][self._num_cols - 1]:
            return True
        if j > 0 and self._cells[i][j - 1].visited == False and current_cell.has_left_wall == False:
            current_cell.draw_move(self._cells[i][j - 1])
            solved = self._solve_r(i, j-1)
            if solved:
                return True
            current_cell.draw_move(self._cells[i][j - 1], True)
        if j < self._num_cols - 1 and self._cells[i][j + 1].visited == False and current_cell.has_right_wall == False:
            current_cell.draw_move(self._cells[i][j + 1])
            solved = self._solve_r(i, j + 1)
            if solved:
                return True
            current_cell.draw_move(self._cells[i][j + 1], True)
        # Top Cell
        if i > 0 and self._cells[i - 1][j].visited == False and current_cell.has_top_wall == False:
            current_cell.draw_move(self._cells[i - 1][j])
            solved = self._solve_r(i - 1, j)
            if solved:
                return True
            current_cell.draw_move(self._cells[i - 1][j], True)
        if i < self._num_rows - 1 and self._cells[i + 1][j].visited == False and current_cell.has_bottom_wall == False:
            current_cell.draw_move(self._cells[i + 1][j])
            solved = self._solve_r(i + 1, j)
            if solved:
                return True
            current_cell.draw_move(self._cells[i + 1][j], True)
        return False
    def solve(self):
        return self._solve_r(0, 0)

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)