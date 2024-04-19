import sys
from modules import data, interface, plot, gui, globals, functions 

def main():
    
    port = interface.get_port()
    inter = interface.CLI(port, globals.filename)
    
    
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
    gui.Button(frame, "Start", 1, 2, command=inter.start_recording)
    gui.Button(frame, "Stop", 2, 2, command=inter.stop_recording)
    gui.Button(frame, "Export", 3, 2, command=functions.export)
    gui.Button(frame, "Quit", 4, 2, command=functions.quit)
    
    # Run GUI
    window.mainloop() 
    
if __name__ == "__main__":
    main()