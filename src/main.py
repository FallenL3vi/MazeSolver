from window import Window
from maze import Maze

    
def  main():
    win = Window(1280, 720)

    maze = Maze(1,1,30,30,20,20,win)
    maze.solve()

    win.wait_for_close()

main()