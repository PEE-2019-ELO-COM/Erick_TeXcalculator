import matplotlib
matplotlib.rcParams['text.usetex'] = True
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

from tkinter import *
from tkinter.ttk import *
import calculator as calc



def graph(text):
    tmptext = entry.get()
    if calc.preview(tmptext)[1]==1:
        tmptext = calc.preview(tmptext)[0]
        tmptext = '$\displaystyle '+tmptext+"$"
    else:
        tmptext = calc.operator(tmptext)
        tmptext = calc.latifa(tmptext)
        tmptext = '$\displaystyle '+tmptext+"$"
        
    ax.clear()
    ax.text(0.2, 0.4, tmptext, fontsize = 24)  
    canvas.draw()
   
root = Tk()
root.title('TeXcalculator')
mainframe = Frame(root)
mainframe.pack()

text = StringVar()
entry = Entry(mainframe, width=70, textvariable=text)
entry.pack()

label = Label(mainframe)
label.pack()

fig = matplotlib.figure.Figure(figsize=(6, 2), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

root.bind('<Return>', graph)
root.mainloop()
