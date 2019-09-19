#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

left_thigh = Motor(Port.B)
right_thigh = Motor(Port.C)

# thighs = DriveBase(left_thigh, right_thigh, 30, 110)

left_lower = Motor(Port.A)
right_lower = Motor(Port.D)

# lowers = DriveBase(left_lower, right_lower, 30, 110)

# left_thigh.run_target(500, -90)
# right_thigh.run_target(500, -90)

# left_lower.run_target(500, 90)
# right_lower.run_target(500, 90)

while True:

    brick.display.clear()
    brick.display.text(left_lower.angle(), (50, 40))
    brick.display.text(right_lower.angle())
    brick.display.text("Lower"
    brick.display.text(left_thigh.angle())
    brick.display.text(right_thigh.angle())

    brick.sound.beep(440, 250)

    if left_lower.stalled():
        brick.sound.beep(400, 250)
        brick.sound.beep(500, 250)
        break
    elif left_lower.angle() > -90:
        left_lower.run(-50)
    elif left_lower.angle() < -90:
        left_lower.run(50)

    if right_lower.stalled():
        brick.sound.beep(400, 250)
        brick.sound.beep(500, 250)
        break
    elif right_lower.angle() > -90:
        right_lower.run(-50)
    elif right_lower.angle() < -90:
        right_lower.run(50)

    if left_thigh.stalled():
        brick.sound.beep(400, 250)
        brick.sound.beep(500, 250)
        break
    elif left_thigh.angle() > -90:
        left_thigh.run(-50)
    elif left_thigh.angle() < -90:
        left_thigh.run(50)

    if right_thigh.stalled():
        brick.sound.beep(400, 250)
        brick.sound.beep(500, 250)
        break
    elif right_thigh.angle() > -90:
        right_thigh.run(-50)
    elif right_thigh.angle() < -90:
        right_thigh.run(50)


brick.sound.beep(440, 250)
