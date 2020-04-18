#!/usr/bin/env python

"""
Example for seven segment displays.
"""

import sys
import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import sevensegment


def main():
    # create seven segment device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)

    # Displaying numbers
    # Display position of each digit
    seg.text = "01234567"
    time.sleep(1.0)
    # Clear display
    seg.text = "        "
    time.sleep(1.0)
    # Display each digit position one by one
    positions = [0,1,2,3,4,5,6,7]
    for digit in positions:
        seg.text = "        "
        seg.text[digit] = str(digit)
        time.sleep(1.0)
    

if __name__ == '__main__':
    main()
