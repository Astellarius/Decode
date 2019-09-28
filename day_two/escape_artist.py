from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 56, 160)

button = TouchSensor(Port.S1)

# Create a walled circle around robot, with opening
# Attach touch button to front of robot
# Escape the Walls 

while True:
    
    robot.drive(100, 0)

    if button.pressed(): 
        robot.drive_time(-100, 0 , 2000)
        robot.drive_time(100, 180, 1000)