# functions.py
import sys
import time
import numpy as np
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
    
def rescale(powers):
        
    if not globals.power_factors:
        for p in powers:
            globals.power_factors.append(p.get())

    else:
        for i, p in enumerate(powers):
            if p.get() != 0:
                globals.power_factors[i] = p.get()
    
    np.savetxt('./data/array.txt', globals.power_factors)

def stop_animation():
    globals.anim.event_source.stop()
    
    print("Stopping")
    if inter:
        inter.stop_recording()
        inter.serialThread.stop()
        time.sleep(1)
        
    print("Stopped")

def start():
    global port, inter
    print("Connecting to Teensy...")
    port = interface.get_port()
    inter = interface.CLI(port, globals.filename)
    time.sleep(2)
    
    print("Started Data Collection...")
    inter.start_recording()
    time.sleep(globals.sampling_rate)

    print("Launching Plot...")
    if globals.anim:
        globals.anim.event_source.start()
    else:
        plot.plot(globals.window)

def stop():
    global inter
    print("Stopping Data Collection...")
    inter.stop_recording()
    inter.serialThread.stop()
    stop_animation()


def gettemp(therm):
    R1 = 10000
    c1 = 1.009249522e-03
    c2 = 2.378405444e-04
    c3 = 2.019202697e-07

    R2 = R1 * ()

def laser_check():

    for button in globals.channel_vars:
        if button.get():
            for b in globals.therm_curr:
                b.set(0)
    
def therm_check():
    for button in globals.therm_curr:
        if button.get():
            for b in globals.channel_vars:
                b.set(0) 

    globals.therm_curr[1].set(0)

def curr_check():
    for button in globals.therm_curr:
        if button.get():
            for b in globals.channel_vars:
                b.set(0) 

    globals.therm_curr[0].set(0)