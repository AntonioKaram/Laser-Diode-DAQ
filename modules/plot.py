# plot.py
import matplotlib.pyplot as plt
from modules import data as dt, globals
from matplotlib.figure import Figure 
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

def animate(i, fig):
    data = dt.load_data()
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    fig.clear()
    ax = fig.subplots()
    ax.plot(x, y1, label='Channel 1')
    ax.plot(x, y2, label='Channel 2')

    ax.legend(loc='upper left')
    plt.tight_layout()
    
def plot(window): 
    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), dpi = 100) 

    # creating the Tkinter canvas containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = window)   
    canvas.draw() 

    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 

    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 

    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

    # Assign the animation to the global variable anim
    global anim
    anim = FuncAnimation(fig, animate, fargs=(fig,), interval=1000, save_count=1000)
    plt.tight_layout()