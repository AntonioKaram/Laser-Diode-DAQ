# functions.py
import sys
import time
from modules import globals, plot, interface

port = None
inter = None

# This describes useful button functions
def quit():
    global inter

    print("Shutting Down Teensy...")
    if inter:
        inter.stop_recording()
        inter.serialThread.stop()
        time.sleep(1)

    print("Exitting...") 
    sys.exit(0)

def save(val):
    globals.sampling_rate = val.get()
    print(f"Saved {globals.sampling_rate}")
    time.sleep(1)

def stop_animation():
    globals.anim.event_source.stop()

def start():
    global port, inter
    print("Connecting to Teensy...")
    port = interface.get_port()
    inter = interface.CLI(port, globals.filename)
    time.sleep(globals.sampling_rate)
    
    print("Started Data Collection...")
    inter.start_recording()
    time.sleep(globals.sampling_rate)

    print("Launching Plot...")
    plot.plot(globals.window)

def stop():
    global inter
    print("Stopping Data Collection...")
    inter.stop_recording()
    inter.serialThread.stop()
    stop_animation()

    
def export():
    print("Exported")

