from window import Window
from line import Line
from point import Point
from cell import Cell

def  main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(Point(100, 100), Point(150, 150))
    win.wait_for_close()

main()