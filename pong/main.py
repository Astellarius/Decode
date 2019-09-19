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

# Board Methods 
# display.clear()
# display.text("text", (x,y))
# Dimensions x = 177 y = 127

# Classes 
    # Board 
    class Board:
        def __init__(self):
            self.ball = []
            self.p1_paddle = []
            self.p2_paddle = []
            self.p1_score = 0
            self.p2_score = 0
        # Ball Update
        # Motor Updates
        # Display Board 
        def display_board(self, p1_motor, p2_motor):
            
        # Motor Contols 
        def motor(self, motor):
            if motor.angle() > 0:
                # Hi 
            elif motor.angle() < 0:
                # Bye 
                


