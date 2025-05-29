from graphics import Window, Line, Point

class Cell ():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2):
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
        if self.has_top_wall:
            line = Line(p2, p3)
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(p3, p4)
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(p4, p1)
            self.__win.draw_line(line)
