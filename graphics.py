from tkinter import Tk, BOTH, Canvas

class Window ():
    def __init__(self, width=0, height=0):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window Closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.__canvas, fill_color)

class Point ():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line ():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)