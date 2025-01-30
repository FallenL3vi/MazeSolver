import random
import time
from line import Line
from point import Point
from cell import Cell



class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win = None,
                 seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_up_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].has_down_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols-1,self.num_rows-1)
    
    def _break_walls_r(self, column, row):
        while True:
            to_visit = []
            self._cells[column][row].visited = True
            if column >= 0 and column <= self.num_cols-1 and row >= 0 and row <= self.num_rows-1:
                left = row - 1
                right = row + 1
                down = column + 1
                up = column - 1

                print(f"Visiting : {column} : {row}")

                if left >= 0:
                    if self._cells[column][left].visited == False:
                        to_visit.append((column,left))
                if right <= self.num_rows - 1:
                    if self._cells[column][right].visited == False:
                        to_visit.append((column,right))
                if up >= 0:
                    if self._cells[up][row].visited == False:
                        to_visit.append((up,row))
                if down <= self.num_cols - 1:
                    if self._cells[down][row].visited == False:
                        to_visit.append((down,row))
                
                if len(to_visit) == 0:
                    #Comment this line to elimnate backtracking
                    #self._draw_cell(column, row)
                    if column == 0 and row == 0:
                        break
                    return
                print(f"Neighbours: {to_visit}")
                
                new_target = to_visit[random.randint(0, len(to_visit)-1)]
                if new_target[0] < column:
                    self._cells[new_target[0]][new_target[1]].has_down_wall = False
                    self._cells[column][row].has_up_wall = False
                elif new_target[0] > column:
                    self._cells[new_target[0]][new_target[1]].has_up_wall = False
                    self._cells[column][row].has_down_wall = False
                    
                if new_target[1] < row:
                    self._cells[new_target[0]][new_target[1]].has_right_wall = False
                    self._cells[column][row].has_left_wall = False
                elif new_target[1] > row:
                    self._cells[new_target[0]][new_target[1]].has_left_wall = False
                    self._cells[column][row].has_right_wall = False


                    #self._draw_cell(new_target[0],new_target[1])
                #Uncomment this line to show path
                self._draw_cell(column, row)


                self._break_walls_r(new_target[0],new_target[1])
                #self._draw_cell(column, row)
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, column, row):
        self._animate()
        #print(f"Current {column} : {row}")
        self._cells[column][row].visited = True
        
        if self._cells[column][row] == self._cells[self.num_cols-1][self.num_rows-1]:
            return True

        found = False
        if column - 1 >= 0:
            target_cell = self._cells[column-1][row]
            if target_cell.visited == False and target_cell.has_down_wall == False:
                self._cells[column][row].draw_move(target_cell)
                found = self._solve_r(column-1, row)
                if found == False:
                    self._cells[column][row].draw_move(target_cell, True)
                else:
                    return True
        if column + 1 <= self.num_cols - 1:
            target_cell = self._cells[column+1][row]
            if target_cell.visited == False and target_cell.has_up_wall == False:
                self._cells[column][row].draw_move(target_cell)
                found = self._solve_r(column+1, row)
                if found == False:
                    self._cells[column][row].draw_move(target_cell, True)
                else:
                    return True
        if row + 1 <= self.num_rows - 1:
            target_cell = self._cells[column][row+1]
            if target_cell.visited == False and target_cell.has_left_wall == False:
                self._cells[column][row].draw_move(target_cell)
                found = self._solve_r(column, row+1)
                if found == False:
                    self._cells[column][row].draw_move(target_cell, True)
                else:
                    return True
        if row - 1 >= 0:
            target_cell = self._cells[column][row-1]
            if target_cell.visited == False and target_cell.has_right_wall == False:
                self._cells[column][row].draw_move(target_cell)
                found = self._solve_r(column, row-1)
                if found == False:
                    self._cells[column][row].draw_move(target_cell, True)
                else:
                    return True
        return found


    
    def _reset_cells_visited(self):
        for col in self._cells:
            for row in col:
                row.visited = False
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.001)