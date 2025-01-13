import time
import random
from typing import List

import siliconcraft_display
import port_definitions as pd

display = siliconcraft_display.Display(pd.serial_port, pd.baud_rate, pd.display_id)

#  ───a───
# │       │
# f       b
# │       │
#  ───g───
# │       │
# e       c
# │       │
#  ───d───  .
# fcgb.eda
try:
    while True:
        bytes = random.randbytes(6)
        # clear the decimal point
        bytes = [x & 0b11110111 for x in bytes]
        display.write_bytes(bytes)
        time.sleep(0.25)
except KeyboardInterrupt:
    display.clear()
