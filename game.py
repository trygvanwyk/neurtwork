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

pawns = ["wp", "wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7",
         "bp", "bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7"]
rooks = ["wr", "wr1", "br", "br1"]
knights = ["wkn", "wkn1", "bkn", "bkn2"]
queens = ["wq", "bq"]
kings = ["wk", "bk"]
bishops = ["wb", "wb1", "bb", "bb1"]

#placeholder functions when piece is pressed
def get_valid_rook_moves():
    print("Rook")
def get_valid_queen_moves():
    print("Queen")
def get_valid_king_moves():
    print("King")
def get_valid_bishop_moves():
    print("Bishop")
def get_valid_knight_moves():
    print("Knight")
def get_valid_pawn_moves():
    print("Pawn")

class Piece:
    #call image from name of piece, create button for piece
    def __init__(self, master, name, row, col):
        self.name = name
        self.image = Image.open(f"pieceimages/{name}.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.master = master
        self.photolabel = tk.Button(master, image=self.photo, command=lambda: self.get_valid_moves(name))
        self.row = row
        self.col = col
        self.photolabel.grid(row=row, column=col)

    #when piece is clicked, refer it to function with custom moves
    def get_valid_moves(self, name):
        self.name = name
        if name in queens:
            get_valid_queen_moves()
        elif name in rooks:
            get_valid_rook_moves()
        elif name in kings:
            get_valid_king_moves()
        elif name in bishops:
            get_valid_bishop_moves()
        elif name in knights:
            get_valid_knight_moves()
        elif name in pawns:
            get_valid_pawn_moves()

construct_board1()

# execute function in the Piece class to create new piece and store it as variable
bk = Piece(game_board, "bk", 0, 4)
bq = Piece(game_board, "bq", 0, 3)
br = Piece(game_board, "br", 0, 0)
br1 = Piece(game_board, "br", 0, 7)
bb = Piece(game_board, "bb", 0, 2)
bb1 = Piece(game_board, "bb", 0, 5)
bkn = Piece(game_board, "bkn", 0, 1)
bkn1 = Piece(game_board, "bkn", 0, 6)
bp = Piece(game_board, "bp", 1, 0)
bp1 = Piece(game_board, "bp", 1, 1)
bp2 = Piece(game_board, "bp", 1, 2)
bp3 = Piece(game_board, "bp", 1, 3)
bp4 = Piece(game_board, "bp", 1, 4)
bp5 = Piece(game_board, "bp", 1, 5)
bp6 = Piece(game_board, "bp", 1, 6)
bp7 = Piece(game_board, "bp", 1, 7)

wk = Piece(game_board, "wk", 7, 4)
wq = Piece(game_board, "wq", 7, 3)
wr = Piece(game_board, "wr", 7, 0)
wr1 = Piece(game_board, "wr", 7, 7)
wb = Piece(game_board, "wb", 7, 2)
wb1 = Piece(game_board, "wb", 7, 5)
wkn = Piece(game_board, "wkn", 7, 1)
wkn1 = Piece(game_board, "wkn", 7, 6)
wp = Piece(game_board, "wp", 6, 0)
wp1 = Piece(game_board, "wp", 6, 1)
wp2 = Piece(game_board, "wp", 6, 2)
wp3 = Piece(game_board, "wp", 6, 3)
wp4 = Piece(game_board, "wp", 6, 4)
wp5 = Piece(game_board, "wp", 6, 5)
wp6 = Piece(game_board, "wp", 6, 6)
wp7 = Piece(game_board, "wp", 6, 7)

# construct the main parts of the board
#construct_board('500', 8)

root.mainloop()