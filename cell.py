from graphics import Window, Line, Point

class Cell ():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x1, self.__y2)
        p3 = Point(self.__x2, self.__y2)
        p4 = Point(self.__x2, self.__y1)
        if self.has_left_wall:
            line = Line(p1, p2)
            self.__win.draw_line(line)
        else:
            line = Line(p1, p2)
            self.__win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(p1, p4)
            self.__win.draw_line(line)
        else:
            line = Line(p1, p4)
            self.__win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(p4, p3)
            self.__win.draw_line(line)
        else:
            line = Line(p4, p3)
            self.__win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(p2, p3)
            self.__win.draw_line(line)
        else:
            line = Line(p2, p3)
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        
        p1 = Point(((self.__x1 + self.__x2) / 2), ((self.__y1 + self.__y2) / 2))
        p2 = Point(((to_cell.__x1 + to_cell.__x2) / 2), ((to_cell.__y1 + to_cell.__y2) / 2))
        line = Line(p1, p2)
        self.__win.draw_line(line)

