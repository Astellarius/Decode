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

color_sensor = ColorSensor(port.S4)
while True:
    
    robot.drive(100, 10)

    if color_sensor.color() == Color.BLACK:
        robot.stop()
        robot.drive(-100, 0, 3000)
        robot.drive(100, 180, 3000)
        
