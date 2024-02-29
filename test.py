import json
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

def browse_file():
    file_path = fd.askopenfilename()
    if file_path:
        # Do something with the selected file path, for example:
        print("Selected file:", file_path)

win = Tk()
win.geometry("500x500")

# main
main_frame = Frame(win)
main_frame.pack(fill=BOTH, expand=1)

# canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# vertical scrollbar
v_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
v_scrollbar.pack(side=RIGHT, fill=Y)

# horizontal scrollbar
h_scrollbar = tk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
h_scrollbar.pack(side=BOTTOM, fill=X)

# configure the canvas
my_canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)

second_frame = Frame(my_canvas, width=1000, height=100)
btn1 = tk.Label(second_frame,
                  text="BrowsdfghffghfgfhfdhfjhhggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggSSSe...",
                  )

btn1.place(x=600, y=0)

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
win.mainloop()
