from line import Line
from point import Point

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_down_wall = True
        self.has_up_wall = True
        self.__x1 = 0
        self.__x2 = 0
        self.__y1 = 0
        self.__y2 = 0
        self.__window = window
    
    def draw(self,top_left , bot_right):
        self.__x1 = top_left.x
        self.__y1 = top_left.y
        self.__x2 = bot_right.x
        self.__y2 = bot_right.y

        if self.has_left_wall:
            new_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__window.draw_line(new_line, "red")
        if self.has_right_wall:
            new_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__window.draw_line(new_line, "red")
        if self.has_down_wall:
            new_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__window.draw_line(new_line, "red")
        if self.has_up_wall:
            new_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__window.draw_line(new_line, "red")