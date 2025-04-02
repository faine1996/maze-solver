from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        center_x_of_self = (self._x1 + self._x2) / 2
        center_y_of_self = (self._y1 + self._y2) / 2
        center_x_of_to_cell = (to_cell._x1 + to_cell._x2) / 2
        center_y_of_to_cell = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(center_x_of_self,center_y_of_self),Point(center_x_of_to_cell,center_y_of_to_cell))
        if not undo:
            self._win.draw_line(line,"red")
        else:
            self._win.draw_line(line,"grey")
