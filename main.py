import sys
from modules import data, plot, gui, globals, functions    

def main():
    #dt = data.load_data()
    global window,frame
    window, frame = gui.create_window()
    
    # Create an input box for sample rate 
    sampling_period = gui.IntInput()
    gui.TextBox(frame, sampling_period, text= "Sample Period (s)", row=0, col=0)
    gui.Button(frame, "Save", 0, 2, command=functions.save)


    # Create an input box for test criteria
    channels = []
    for i in range(1, 11):
        channels.append(gui.IntInput())
        gui.TextBox(frame, channels[i-1], text=f"Channel {i}", row=i, col=0)


    # Create buttons for start, stop, pause
    gui.Button(frame, "Start", 1, 2, command=functions.start)
    gui.Button(frame, "Stop", 2, 2, command=functions.stop)
    gui.Button(frame, "Pause", 3, 2, command=functions.pause)
    gui.Button(frame, "Export", 4, 2, command=functions.export)
    gui.Button(frame, "Quit", 5, 2, command=functions.quit)
    
    # Run GUI
    window.mainloop() 
    
if __name__ == "__main__":
    main()