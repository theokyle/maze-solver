from cell import Cell
import time
import random

class Maze ():
    def __init__ (
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(.05)
    
    def __break_entrance_and_exit(self):
        if len(self.__cells) == 0:
            return
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            queue = []
            if i > 0:
                if self.__cells[i-1][j].visited == False:
                    queue.append([i-1, j])
            if j > 0:
                if self.__cells[i][j-1].visited == False:
                    queue.append([i, j-1])
            if i + 1 < self.__num_cols:
                if self.__cells[i+1][j].visited == False:
                        queue.append([i + 1, j])
            if j + 1 < self.__num_rows:
                if self.__cells[i][j+1].visited == False:
                        queue.append([i, j+1])
            if len(queue) == 0:
                self.__draw_cell(i, j)
                return
            direction = random.randrange(len(queue))
            next_index = queue[direction]

            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False
            if next_index[1] == j+1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False
            if next_index[1] == j-1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False

            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited (self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False
    
    def _solve_r (self, i, j):
        self.__animate()
        current_cell = self.__cells[i][j]
        current_cell.visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows-1:
            return True
        if i < self.__num_cols - 1 and not current_cell.has_right_wall and not self.__cells[i+1][j].visited :
            next_cell = self.__cells[i+1][j]
            current_cell.draw_move(next_cell)
            if self._solve_r(i + 1, j):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        if j < self.__num_cols - 1 and not current_cell.has_bottom_wall and not self.__cells[i][j+1].visited :
            next_cell = self.__cells[i][j+1]
            current_cell.draw_move(next_cell)
            if self._solve_r(i, j+1):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        if i > 0 and not current_cell.has_left_wall and not self.__cells[i-1][j].visited:
            next_cell = self.__cells[i-1][j]
            current_cell.draw_move(next_cell)
            if self._solve_r(i-1, j):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        if j > 0 and not current_cell.has_top_wall and not self.__cells[i][j-1].visited:
            next_cell = self.__cells[i][j-1]
            current_cell.draw_move(next_cell)
            if self._solve_r(i, j-1):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        return False

    def solve(self):
        return self._solve_r(0,0)
                
        
                

