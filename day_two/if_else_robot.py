#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)

button = TouchSensor(Port.S1)

# If Else Beeping 
# Build basic car, use two unattached buttons to control turning. 

while True:

    if button.pressed():
        brick.sound.beep(200)     
    else: 
        brick.sound.beep(500)
