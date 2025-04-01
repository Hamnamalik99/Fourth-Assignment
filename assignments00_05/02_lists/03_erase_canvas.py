# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser 
# rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk  # Tkinter library ko import kiya gaya hai jo GUI banane ke liye use hoti hai.

# Canvas settings
CANVAS_WIDTH = 400  # Canvas ki width ko 400 pixels set kiya gaya hai.
CANVAS_HEIGHT = 400  # Canvas ki height ko 400 pixels set kiya gaya hai.
CELL_SIZE = 40  # Har cell ka size 40x40 pixels set kiya gaya hai.
ERASER_SIZE = 20  # Eraser ka size 20x20 pixels set kiya gaya hai.

class EraserApp:
    def __init__(self, root):
        self.root = root  # Root window ka reference store kiya gaya hai.
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")  # Canvas banaya gaya hai jisme 400x400 ka area hai, aur background white hai.
        self.canvas.pack()  # Canvas ko window mein pack kiya gaya hai.

        self.cells = {}  # Cells ke references ko store karne ke liye dictionary banayi gayi hai.
        self.create_grid()  # Grid ko create karne ke liye method call kiya gaya hai.

        # Eraser banaya gaya hai (pink color ka rectangle)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")  # Eraser ko initial position (0,0) par set kiya gaya hai.

        # Mouse binding
        self.canvas.bind("<B1-Motion>", self.move_eraser)  # Jab mouse ko left-click ke saath drag kiya jaye, move_eraser function ko call karte hain.

    def create_grid(self):
        """Create a grid of blue cells"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):  # Row ko canvas ki height ke hisaab se loop kiya gaya hai, step size = CELL_SIZE.
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):  # Column ko canvas ki width ke hisaab se loop kiya gaya hai, step size = CELL_SIZE.
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")  # Har cell ko rectangle ke form mein draw kiya gaya hai, blue color ka.
                self.cells[(col, row)] = cell  # Har cell ko dictionary mein store kiya gaya hai jisme (col, row) coordinates keys hain.

    def move_eraser(self, event):
        """Move the eraser and erase cells"""
        x, y = event.x, event.y  # Mouse ke current position ke x aur y coordinates ko store kiya gaya hai.
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Eraser ko mouse ke new position pe move kar diya gaya hai.
        self.erase_cells(x, y)  # Eraser ke new position ke hisaab se cells ko erase karne ka function call kiya gaya hai.

    def erase_cells(self, x, y):
        """Erase cells in contact with the eraser"""
        for (col, row), cell in self.cells.items():  # Har ek cell ko loop karke check kiya gaya hai.
            if col < x + ERASER_SIZE and col + CELL_SIZE > x and row < y + ERASER_SIZE and row + CELL_SIZE > y:  # Agar cell ka position eraser ke area mein hai toh:
                self.canvas.itemconfig(cell, fill="white")  # Cell ka color white mein change kar diya gaya hai, jisse wo erase ho jata hai.

def main():
    root = tk.Tk()  # Tkinter ka root window create kiya gaya hai.
    root.title("Eraser Canvas")  # Window ka title set kiya gaya hai.
    app = EraserApp(root)  # EraserApp class ka ek instance banaya gaya hai aur root window ko pass kiya gaya hai.
    root.mainloop()  # Tkinter main loop ko run kiya gaya hai jo GUI ko interactable banata hai.

if __name__ == "__main__":  # Yeh check karta hai ke script ko direct run kiya gaya hai ya import kiya gaya hai.
    main()  # Agar script direct run ho rahi hai toh main() function ko call kiya gaya hai.
