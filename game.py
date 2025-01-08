import tkinter as tk
from PIL import Image, ImageTk

# make the main window, name it, and give it dimensions
root = tk.Tk()
root.title("Chess")
root.geometry('820x820')

game_board = tk.Frame(root, borderwidth=5, relief="solid")
game_board.grid(padx=5, pady=5)
game_board.config(width=800, height=800)

class BoardSquare:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color

        self.frame = tk.Frame(game_board, background=f"{color}")
        self.frame.grid(row=row, column=column)
        self.frame.config(height=100, width=100)

# create board where each square is a frame (frames can contain more widgets)
def construct_board1():
    # create gray squares
    for x in range(0, 8, 2):
        for i in range(0, 8, 2):
            BoardSquare(x, i, "grey75")
    for x in range(1, 8, 2):
        for i in range(1, 8, 2):
            BoardSquare(x, i, "grey75")
    # create green squares
    for x in range(0, 8, 2):
        for i in range(1, 8, 2):
            BoardSquare(x, i, "green4")
    for x in range(1, 8, 2):
        for i in range(0, 8, 2):
            BoardSquare(x, i, "green4")

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
        self.photolabel = tk.Button(master, image=self.photo)
        self.photolabel.grid(row=row, column=column)

construct_board1()

# execute function in the Piece class to create new piece and store it as variable
bk = Piece(game_board, "bk", 0, 4)
bq = Piece(game_board, "bq", 0, 3)
br = Piece(game_board, "br", 0, 0)
bb = Piece(game_board, "bb", 0, 2)
bkn = Piece(game_board, "bkn", 0, 1)
bp = Piece(game_board, "bp", 1, 0)

wk = Piece(game_board, "wk", 7, 4)
wq = Piece(game_board, "wq", 7, 3)
wr = Piece(game_board, "wr", 7, 0)
wb = Piece(game_board, "wb", 7, 2)
wkn = Piece(game_board, "wkn", 7, 1)
wp = Piece(game_board, "wp", 6, 0)

# construct the main parts of the board
#construct_board('500', 8)

root.mainloop()
