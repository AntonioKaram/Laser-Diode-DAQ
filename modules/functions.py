# functions.py
import sys
from modules import globals, plot

# This describes useful button functions
def save():
    print("Save")
    
def quit():
    sys.exit(0)

def save():
    print("Saved")

def stop_animation():
    globals.anim.event_source.stop()

def start():
    print("Started Data Collection:")
    plot.plot(globals.window)

def stop():
    print("Stop")
    stop_animation()

def pause():
    print("Pause")
    
def export():
    print("Exported")

