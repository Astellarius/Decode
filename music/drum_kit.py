#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

bass_button = TouchSensor(Port.S1)
hat_button = TouchSensor(Port.S2)

while True:

    if bass_button.pressed():
        brick.sound.file(SoundFile.HORN_1)

    if hat_button.pressed():
        brick.sound.file(SoundFile.CLICK)

