from graphics import Window
from shapes import Line,Point
from cell import Cell

def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "black")


    win.wait_for_close()

if __name__ == "__main__":
    main()