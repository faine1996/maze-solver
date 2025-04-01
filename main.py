from graphics import Window
from shapes import Line,Point

def main():
    win = Window(800, 600)
     # Create a few points and lines
    p1 = Point(100, 100)
    p2 = Point(300, 100)
    p3 = Point(300, 300)
    p4 = Point(100, 300)

    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    # Draw lines on the window
    win.draw_line(line1, "red")
    win.draw_line(line2, "green")
    win.draw_line(line3, "blue")
    win.draw_line(line4, "purple")

    win.wait_for_close()

if __name__ == "__main__":
    main()