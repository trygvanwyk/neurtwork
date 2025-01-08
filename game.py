import tkinter as tk
from PIL import Image, ImageTk

def construct_board(dimension, grid_size):
    d = float(dimension)
    gap = d / grid_size

    canvas = tk.Canvas(root, width=d, height=d, background='grey75')
    for i in range(1, grid_size):
        canvas.create_line(i * gap, 0, i * gap, d)
        canvas.create_line(0, i * gap, d, i * gap)
        canvas.grid(row=0, column=0)
    for r in range(0, grid_size):
        for c in range(0, grid_size):
            if r % 2 != 0 and c % 2 == 0:
                canvas.create_rectangle(r * gap, c * gap, (r + 1) * gap, (c + 1) * gap, fill='green4')
            if r % 2 == 0 and c % 2 != 0:
                canvas.create_rectangle(r * gap, c * gap, (r + 1) * gap, (c + 1) * gap, fill='green4')

class Piece:
    def __init__(self, master, name, row, column):
        #define where piece will exist
        self.master = master

        #call image from name of piece
        self.name = name
        self.image = Image.open(f"pieceimages/{name}.png")
        self.photo = ImageTk.PhotoImage(self.image)

        #create a label to display the piece
        self.photolabel = tk.Button(root, image=self.photo)
        self.photolabel.grid(row=row, column=column)

# make the main window, name it, and give it dimensions
root = tk.Tk()
root.title("Chess")
root.geometry('1000x1000')

# execute function in the Piece class to create new piece and store it as variable
bk = Piece(root, "bk", 1, 0)
bq = Piece(root, "bq", 1, 1)
br = Piece(root, "br", 1, 2)
bb = Piece(root, "bb", 1, 3)
bkn = Piece(root, "bkn", 1, 4)
bp = Piece(root, "bp", 1, 5)

wk = Piece(root, "wk", 0, 0)
wq = Piece(root, "wq", 0, 1)
wr = Piece(root, "wr", 0, 2)
wb = Piece(root, "wb", 0, 3)
wkn = Piece(root, "wkn", 0, 4)
wp = Piece(root, "wp", 0, 5)

# construct the main parts of the board
construct_board('500', 8)

root.mainloop()
