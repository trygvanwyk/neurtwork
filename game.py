import tkinter as tk


def construct_board(dimension, grid_size):
    d = float(dimension)
    gap = d / grid_size

    canvas = tk.Canvas(root, width=d, height=d, background='grey75')
    for i in range(1, grid_size):
        canvas.create_line(i * gap, 0, i * gap, d)
        canvas.create_line(0, i * gap, d, i * gap)
        canvas.pack()
    for r in range(0, grid_size):
        for c in range(0, grid_size):
            if r % 2 != 0 and c % 2 == 0:
                canvas.create_rectangle(r * gap, c * gap, (r + 1) * gap, (c + 1) * gap, fill='green4')
            if r % 2 == 0 and c % 2 != 0:
                canvas.create_rectangle(r * gap, c * gap, (r + 1) * gap, (c + 1) * gap, fill='green4')


# make the main window, name it, and give it dimensions
root = tk.Tk()
root.title("Chess")
root.geometry('500x500')

# construct the main parts of the board
construct_board('500', 8)

root.mainloop()
