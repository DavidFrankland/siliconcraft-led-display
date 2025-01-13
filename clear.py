import siliconcraft_display
import port_definitions as pd

# clear the LED display
display = siliconcraft_display.Display(pd.serial_port, pd.baud_rate, pd.display_id)
display.clear()
