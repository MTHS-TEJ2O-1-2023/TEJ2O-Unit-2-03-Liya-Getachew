"""
Created by: Liya Getachew
Created on: Sep 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *


display.clear()
sleep(1)

display.scroll("A rectangle has dimensions 5cm & 3cm.'")
display.scroll("The perimeter equals " + str(2 * (5 + 3)) + "cm^2")
display.scroll("The area equals " + str(5 * 3) + "cm^2")
