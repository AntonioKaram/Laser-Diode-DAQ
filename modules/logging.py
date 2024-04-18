# Import necessary libraries
import time
import datetime
import pyfirmata
import os

# Specify how fast to collect samples
SAMPRATE = 4

# specify the number of channels and which pins to use
NUMCHANNELS = 14
ADCPins = ['A13', 'A12', 'A11', 'A10', 'A9', 'A8', 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1', 'A0']

# Initialize the board
board = pyfirmata.Arduino('/dev/ttyACM0')  # replace '/dev/ttyACM0' with the port where your board is connected

# Create an iterator to read ADC values
it = pyfirmata.util.Iterator(board)
it.start()

# Start ADC for all pins
for pin in ADCPins:
    board.analog[pin[-1]].enable_reporting()

# Function to read ADC values
def read_adc():
    adc_values = []
    for pin in ADCPins:
        adc_values.append(board.analog[pin[-1]].read())
    return adc_values

# Function to write ADC values to a file
def write_to_file(filename, adc_values):
    with open(filename, 'a') as f:
        f.write(str(datetime.datetime.now()) + ', ' + ', '.join(map(str, adc_values)) + '\\n')

# Function to create a new file name based on time and date
def new_file_name():
    return 'ADC5CH_' + datetime.datetime.now().strftime('%m%d%H%M') + '.dat'

# Main loop
def main():
    filename = new_file_name()
    while True:
        adc_values = read_adc()
        write_to_file(filename, adc_values)
        time.sleep(1.0 / SAMPRATE)

if __name__ == '__main__':
    main()
