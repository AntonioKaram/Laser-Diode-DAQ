# plot.py
import matplotlib.pyplot as plt
import pandas as pd
from modules import globals
import matplotlib.ticker as ticker
from matplotlib.figure import Figure 
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 



def animate(i, fig):
    data = pd.read_csv('data/data.csv')
    x = data[data.columns[0]]
    
    if globals.power_factors and not data.empty:
        for i, pf in enumerate(globals.power_factors):
            
            # new value = value * pf/most recent voltage
            scalar = (pf/data[data.columns[i+1]].tail(1).values[0])
            data.iloc[:, i] = data.iloc[:, i].astype('float64') * (0.0 if float(scalar) == 0 else float(scalar))
            
    fig.clear()
    ax = fig.subplots()
    plotted = False
    colors = ['r', 'g', 'blue', 'gray', 'orange', 'purple', 'black', 'olivedrab', 'pink', 'sienna']
    for i in range(1, 11):
        if globals.channel_vars[i-1].get():
            ax.plot(x, data[data.columns[i]], label=f'Laser {i}', color=colors[i-1])
            ax.set_ylabel('Laser Power (Watts)')
            plotted = True

    if globals.therm_curr[1].get():
        ax.plot(x, data[data.columns[11]], label=f'Set Mon', color='navy')
        ax.set_ylabel('Set Monitor (Volts)')
        plotted = True

    if globals.therm_curr[0].get():
        ax.plot(x, data[data.columns[12]], label=f'Temperature', color='teal')
        ax.set_ylabel('Temperature (Fahrenheit)')
        plotted = True
        
    # Format the x-axis to properly display dates
    ax.set_xlabel('Time (hours)')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(int(len(x)/8) if int(len(x)/8) > 0 else 1 ))


    if plotted:
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18),
          ncol=3, fancybox=True, shadow=True)

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