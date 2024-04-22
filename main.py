import sys
from modules import data, plot, gui, globals, functions 

def main():
    globals.window, globals.frame = gui.create_window()
    
    # Create an input box for sample rate 
    sampling_period = gui.IntInput()
    gui.TextBox(globals.frame, sampling_period, text= "Sample Period (s)", row=0, col=0)
    gui.Button(globals.frame, "Save", 0, 2, command=lambda: functions.save(sampling_period))


    # Create an input box for test criteria
    channels = []
    for i in range(1, 11):
        channels.append(gui.IntInput())
        gui.TextBox(globals.frame, channels[i-1], text=f"Channel {i}", row=i, col=0)


    # Create buttons for start, stop, pause
    gui.Button(globals.frame, "Start", 1, 2, command=functions.start)
    gui.Button(globals.frame, "Stop", 2, 2, command=functions.stop)
    gui.Button(globals.frame, "Export", 3, 2, command=functions.export)
    gui.Button(globals.frame, "Quit", 4, 2, command=functions.quit)
    
    # Run GUI
    globals.window.mainloop() 
    
if __name__ == "__main__":
    main()