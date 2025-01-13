import time
from typing import List

import siliconcraft_display
import port_definitions as pd

display = siliconcraft_display.Display(pd.serial_port, pd.baud_rate, pd.display_id)


def write_with_delay(bytes: List[int]):
    display.write_bytes(bytes)
    time.sleep(0.1)


#  ───a───
# │       │
# f       b
# │       │
#  ───g───
# │       │
# e       c
# │       │
#  ───d───  .
#     fcgb.eda
a = 0b10000100
b = 0b11010100

try:
    while True:
        write_with_delay([a, 0, 0, 0, 0, 0])
        write_with_delay([b, 0, 0, 0, 0, 0])
        write_with_delay([b, a, 0, 0, 0, 0])
        write_with_delay([b, b, 0, 0, 0, 0])
        write_with_delay([b, b, a, 0, 0, 0])
        write_with_delay([b, b, b, 0, 0, 0])
        write_with_delay([b, b, b, a, 0, 0])
        write_with_delay([b, b, b, b, 0, 0])
        write_with_delay([b, b, b, b, a, 0])
        write_with_delay([b, b, b, b, b, 0])
        write_with_delay([b, b, b, b, b, a])
        write_with_delay([b, b, b, b, b, b])
except KeyboardInterrupt:
    display.clear()
