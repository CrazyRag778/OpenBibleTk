from tkinter import ttk, Canvas, Scrollbar, messagebox
from tkinter import *
import pythonbible as bible
from data.books import bible_books_list
import webbrowser
from data.definations import *


root = Tk()

# Theme/Style
sty = ttk.Style()
sty.theme_use(themename='clam')

## APP
root.title("OpenBibleTk")
root.geometry("900x900")
root.minsize()
root.maxsize()
###

# MenuBar Configuration
menubar = Menu(root)

Open = Menu(menubar, tearoff=False) 
about = Menu(menubar, tearoff=False) 
pref = Menu(menubar, tearoff=False)



Open.add_command(label="New") 
Open.add_command(label="Rules") 
Open.add_command(label="Exit", command=root.quit) 

about.add_command(label="Developer", command=show_about) 
about.add_command(label="PythonBible", command=open_pytbib_githbpg) 
about.add_command(label="Github", command=open_projct_githbpg) 

pref.add_command(label="Settings")

menubar.add_cascade(label="Open", menu=Open) 
menubar.add_cascade(label="About", menu=about) 
menubar.add_cascade(label="Preference", menu=pref)
###

## User Interface



# Create vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(root, orient="vertical")
vertical_scrollbar.pack(side="right", fill="y")

# Create horizontal scrollbar
horizontal_scrollbar = ttk.Scrollbar(root, orient="horizontal")
horizontal_scrollbar.pack(side="bottom", fill="x")

# Create canvas
canvas = Canvas(root, yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Configure vertical scrollbar
vertical_scrollbar.config(command=canvas.yview)

# Configure horizontal scrollbar
horizontal_scrollbar.config(command=canvas.xview)

# Create a frame inside the canvas to hold the contents
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Add some content to the scrollable frame



book = "43"
ch = "001"
n_ch = int(ch)
vrs = "001"
code = book+ch+vrs
code = int(code)

ttk.Label(scrollable_frame, text=(str(n_ch)), font=('FreeMono', 50)).pack()
ttk.Label(scrollable_frame, text=(f"\n{bible_books_list[int(book)-1]}"), font=('FreeMono', 25)).pack()

for i in range(0, 50):
    ttk.Label(scrollable_frame, text=((f"{i+1} "+(bible.get_verse_text((code+i), version=bible.Version.KING_JAMES)))), font=('FreeMono')).pack(anchor='nw')




# Update the scroll region
scrollable_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))





###

root.config(menu=menubar) 
root.mainloop()
