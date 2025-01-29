from window import Window
from line import Line
from point import Point
from cell import Cell
import time

class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win = None):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for column in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                new_cell = Cell(self._win)
                self._cells[column].append(new_cell)
                self._draw_cell(column, row)
    
    def _draw_cell(self, column, row):
        cell_position = Point((row * self.cell_size_x) + self.__x1, (column * self.cell_size_y) + self.__y1)
        bot_right = Point(cell_position.x + self.cell_size_x, cell_position.y + self.cell_size_y)

        self._cells[column][row].draw(cell_position, bot_right)

        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
    
def  main():
    win = Window(800, 600)

    #maze = Maze(0,0,20,20,30,30,win)

    win.wait_for_close()

main()