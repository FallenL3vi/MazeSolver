from line import Line
from point import Point

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_down_wall = True
        self.has_up_wall = True
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._window = window
        self.visited = False
    
    def draw(self,top_left , bot_right):
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bot_right.x
        self._y2 = bot_right.y

        if self._window == None:
            return

        if self.has_left_wall:
            new_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._window.draw_line(new_line, "red")
        else:
            new_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._window.draw_line(new_line, "white")
        if self.has_right_wall:
            new_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._window.draw_line(new_line, "red")
        else:
            new_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._window.draw_line(new_line, "white")
        if self.has_down_wall:
            new_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._window.draw_line(new_line, "red")
        else:
            new_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._window.draw_line(new_line, "white")
        if self.has_up_wall:
            new_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._window.draw_line(new_line, "red")
        else:
            new_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._window.draw_line(new_line, "white")
    
    def draw_move(self, to_cell, undo = False):
        color = "red"
        if undo:
            color = "grey"
        start_point = Point((self._x1 + self.__2)/2, (self._y1 + self._y2)/2)
        end_point = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        new_line = Line(start_point, end_point)
        self._window.draw_line(new_line, color)