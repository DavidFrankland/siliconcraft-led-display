import siliconcraft_display
import port_definitions as pd

# toggle the display brightness
display = siliconcraft_display.Display(pd.serial_port, pd.baud_rate, pd.display_id)
display.set_brightness()
