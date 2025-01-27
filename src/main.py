from window import Window
from line import Line
from point import Point

def  main():
    win = Window(800, 600)

    line_1 = Line(Point(0, 30), Point(100, 100))
    line_2 = Line(Point(100, 100), Point(200, 0))
    win.draw_line(line_1, "red")
    win.draw_line(line_2, "red")
    win.wait_for_close()

main()