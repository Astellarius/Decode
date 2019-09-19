#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import music

birthday = music.Music()

birthday.play(birthday.c4_note)
birthday.play(birthday.c4_note, 200)
birthday.play(birthday.d4_note)
birthday.play(birthday.c4_note)
birthday.play(birthday.f4_note)
birthday.play(birthday.e4_note, 600)

wait(200)

birthday.play(birthday.c4_note)
birthday.play(birthday.c4_note, 200)
birthday.play(birthday.d4_note)
birthday.play(birthday.c4_note)
birthday.play(birthday.g4_note)
birthday.play(birthday.f4_note, 600)

wait(200)

birthday.play(birthday.c4_note)
birthday.play(birthday.c4_note, 200)
birthday.play(birthday.c5_note)
birthday.play(birthday.a4_note)
birthday.play(birthday.f4_note)
birthday.play(birthday.e4_note)
birthday.play(birthday.d4_note, 600)

wait(200)

birthday.play(birthday.as4_note)
birthday.play(birthday.as4_note, 200)
birthday.play(birthday.a4_note)
birthday.play(birthday.f4_note)
birthday.play(birthday.g4_note)
birthday.play(birthday.f4_note, 800)