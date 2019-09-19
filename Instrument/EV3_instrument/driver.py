#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 160)

left_button = TouchSensor(Port.S1)
right_button = TouchSensor(Port.S2)


while True:
    
    robot.drive(-500, 0)

    # if left_button.pressed() and right_button.pressed():
    #     while left_button.pressed() and right_button.pressed():
    #         robot.stop() 

    if left_button.pressed():
        while left_button.pressed(): 
            robot.drive(0, 500)

    if right_button.pressed():
        while right_button.pressed(): 
            robot.drive(0, -500)

