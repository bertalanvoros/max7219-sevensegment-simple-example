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

    # setting with manually, there is only one 7 segment digit
    # digit one is actually Dig 7 on the Max7219
    seg.device.width = 2

    # Displaying numbers
    seg.text = " " * seg.device.width
    time.sleep(1.0)
    
    seg.text = "." * seg.device.width
    time.sleep(1.0)


    while True:

        now = datetime.now()
        todisplay = now.strftime("%S")
        seg.text = str(todisplay)
        time.sleep(1)


if __name__ == '__main__':
    main()
