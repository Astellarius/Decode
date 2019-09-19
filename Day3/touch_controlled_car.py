#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)

left_button = TouchSensor(Port.S1)
right_button = TouchSensor(Port.S2)

while not left_button.pressed() and right_button.pressed():

    robot.drive(100, 0)

    if left_button.pressed():
        while left_button.pressed():
            robot.drive(50, 90)

    if right_button.pressed():
        while right_button.pressed():
            robot.drive(50, -90)

    

