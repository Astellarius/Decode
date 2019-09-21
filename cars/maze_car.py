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

while True:
    robot.drive( 100, 0, 3000 ) # go_forward
    robot.drive( 100, 90, 3000 ) # turn_right
    robot.drive( 100, -90, 3000 ) # turn_left
    robot.drive( 100, 180, 3000 ) # turn_around
    break