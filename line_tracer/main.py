#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 160)

color_sensor = ColorSensor(Port.S1)

while True:
    
    if color_sensor.color() == Color.BLACK:
        while color_sensor.color() == Color.BLACK:
            robot.drive(25, 90)

    else:
        while color_sensor.color() != Color.BLACK:
            robot.drive(25, -90)
