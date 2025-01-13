import serial
from typing import List


class Display:
    """
    Represents a Silicon Craft SC6Dlite LED display.
    """

    def __init__(self, port: str, baudrate: int,  id: int):
        self.ser = serial.Serial(port, baudrate)
        self.id = id

    def write_bytes(self, display_bytes: List[int]):
        """
        Send the individual digit segment data to the display.
        """
        self.ser.write(bytes([self.id]))
        self.ser.write(bytes('a', 'utf-8'))
        self.ser.write(bytes(display_bytes))

    def clear(self):
        """
        Blank the display.
        """
        self.write_bytes([0, 0, 0, 0, 0, 0])

    def set_brightness(self):
        """
        Switch between low/high brightness.
        The display powers on at full brightness.
        """
        self.ser.write(bytes([self.id]))
        self.ser.write(bytes('n', 'utf-8'))

    def set_protocol(self, new_baud_rate: int, new_id: int):
        """
        Set the display baud rate and ID.
        Settings are stored in the non volatile memory and remain unchanged until next setting.
        Display shows “ SEt” when programming is done.
        You need to reset the display by turning off then on for the changes to take effect.
        """
        b = 0
        if new_baud_rate == 9600:
            b = 36
        if new_baud_rate == 19200:
            b = 18
        if new_baud_rate == 38400:
            b = 9
        if b != 0:
            raw_bytes = [0x1e, 0x1e, b, new_id]
            self.ser.write(bytes(raw_bytes))
            exit()
