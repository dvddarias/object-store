import os
import sys
import signal
from eve import Eve

def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

app = Eve()

if __name__ == '__main__':
    app.run(host='0.0.0.0')



