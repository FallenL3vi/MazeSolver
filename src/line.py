from point import Point
from tkinter import Canvas

class Line():
    def __init__(self, point_start = Point(), point_end = Point()):
        self.point_start = point_start
        self.point_end = point_end
    
    def draw(self, canvas, fill_color = "white"):
        canvas.create_line(self.point_start.x, self.point_start.y, self.point_end.x, self.point_end.y, fill=fill_color,
                           width = 2)