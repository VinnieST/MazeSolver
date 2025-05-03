from window import Line, Point

class Cell:
    def __init__(self, win=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return 
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        radius = abs(self._x2 - self._x1) // 2
        x_centre = radius + self._x1
        y_centre = radius + self._y1

        radius2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_centre2 = radius2 + to_cell._x1
        y_centre2 = radius2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "grey"

        line = Line(Point(x_centre, y_centre), Point(x_centre2, y_centre2))
        self._win.draw_line(line, fill_color)