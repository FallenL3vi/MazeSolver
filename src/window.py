from tkinter import Tk, BOTH, Canvas, ttk
from line import Line

class Window():
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__canvas_widget = Canvas(self.__root_widget, bg="White", height=height, width=width)
        self.__canvas_widget.pack(fill=BOTH, expand=1)
        self.__is_running =  False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def draw_line(self, line, fill_color):
        if line:
            line.draw(self.__canvas_widget, fill_color)
            return
        raise Exception("No line passed to draw_line")

    def close(self):
        self.__is_running = False