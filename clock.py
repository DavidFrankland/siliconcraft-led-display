import time
import siliconcraft_display

#  ───a───
# │       │
# f       b
# │       │
#  ───g───
# │       │
# e       c
# │       │
#  ───d───  .

digits = [
    # fcgb.eda
    0b11010111,  # 0
    0b01010000,  # 1
    0b00110111,  # 2
    0b01110011,  # 3
    0b11110000,  # 4
    0b11100011,  # 5
    0b11100111,  # 6
    0b01010001,  # 7
    0b11110111,  # 8
    0b11110011,  # 9
]


class Display:
    """
    Displays the time on the LED display.
    """

    def __init__(self, siliconcraft_display: siliconcraft_display.Display):
        self.display = siliconcraft_display
        self.prev_display_bytes = [0] * 6
        self.display_bytes = [0] * 6

    def show_time(self, time_string: str):
        for i in range(0, 6):
            self.display_bytes[i] = digits[int(time_string[i])]

        # set the decimal points
        self.display_bytes[1] |= 0b00001000
        self.display_bytes[3] |= 0b00001000
        self.display.write_bytes(self.display_bytes)

        time.sleep(0.5)

        # clear the decimal points
        self.display_bytes[1] &= 0b11110111
        self.display_bytes[3] &= 0b11110111
        self.display.write_bytes(self.display_bytes)
