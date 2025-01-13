import datetime
import time

import siliconcraft_display
import clock
import port_definitions as pd

display = siliconcraft_display.Display(pd.serial_port, pd.baud_rate, pd.display_id)
# display.set_brightness()
# display.set_protocol(38400, display_id)

my_clock = clock.Display(display)
old_time_string = ''
time_string = ''

try:
    while True:
        while time_string == old_time_string:
            time.sleep(0.001)
            time_string = datetime.datetime.now().strftime('%H%M%S')
        old_time_string = time_string
        my_clock.show_time(time_string)
except KeyboardInterrupt:
    display.clear()
