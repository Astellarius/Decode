#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)

while True:
    robot.drive_time(500, 0, 10000)    
    robot.drive_time(500, 90, 5000)    
    robot.drive_time(500, 90, 4000)    
    robot.drive_time(500, 90, 5000)
    robot.drive_time(500, -90, 5000)    