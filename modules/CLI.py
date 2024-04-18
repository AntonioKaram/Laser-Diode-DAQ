import sys
import glob
from serialUtils import *
from collections import deque

class CLI:
    def __init__(self, port, filename):
        self.data = deque(maxlen=20000)
        self.serialThread = SerialThread(port, self.data, 1152000)
        self.serialThread.start()
        self.filename = filename

    def start_recording(self):
        self.serialThread.start_recording(self.filename)

    def stop_recording(self):
        self.serialThread.stop_recording()

def get_port():
    ports = glob.glob("/dev/tty.*")[::-1]
    for i, port in enumerate(ports):
        print(f"{i+1}. {port}")
    choice = int(input("Select a port: ")) - 1
    return ports[choice]

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    port = get_port()
    filename = sys.argv[1]

    cli = CLI(port, filename)

    while True:
        command = input("Enter command (start, stop, exit): ")
        if command == "start":
            cli.start_recording()
        elif command == "stop":
            cli.stop_recording()
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()
