# plot.py
import matplotlib.pyplot as plt
import pandas as pd
from modules import data as dt, globals
from matplotlib.figure import Figure 
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def animate(i, fig):
    data = pd.read_csv('data/data.csv')
    data[data.columns[0]] = pd.to_datetime(data[data.columns[0]], format='%m/%d/%y:%H:%M')  # Convert to datetime object
    x = data[data.columns[0]]
    y1 = data[data.columns[1]]
    y2 = data[data.columns[2]]

    fig.clear()
    ax = fig.subplots()
    ax.plot(x, y1, label='Channel 1')
    ax.plot(x, y2, label='Channel 2')

    # Format the x-axis to properly display dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y:%H:%M'))
    ax.xaxis.set_major_locator(mdates.DayLocator())

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
    globals.anim = FuncAnimation(fig, animate, fargs=(fig,), interval=1000, save_count=1000)
    plt.tight_layout()