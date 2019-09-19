#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import music

megalovania = music.Music()
        # sixteenth 125
        # eight 250 
        # half 1000
#measure 1
megalovania.play(megalovania.d4_note,125)
megalovania.play(megalovania.d4_note,125)
megalovania.play(megalovania.d5_note,250)
megalovania.play(megalovania.a4_note,375)
megalovania.play(megalovania.gs4_note,125)
wait(125)
megalovania.play(megalovania.g4_note,250)
megalovania.play(megalovania.f4_note,250)
megalovania.play(megalovania.d4_note,125)
megalovania.play(megalovania.f4_note,125)
megalovania.play(megalovania.g4_note,125)
#m2
megalovania.play(megalovania.c4_note,125)
megalovania.play(megalovania.c4_note,125)
megalovania.play(megalovania.d5_note,250)
megalovania.play(megalovania.a4_note,375)
megalovania.play(megalovania.gs4_note,125)
wait(125)
megalovania.play(megalovania.g4_note,250)
megalovania.play(megalovania.f4_note,250)
megalovania.play(megalovania.d4_note,125)
megalovania.play(megalovania.f4_note,125)
megalovania.play(megalovania.g4_note,125)
#m3 un def b3
megalovania.play(megalovania.b4_note,125)
megalovania.play(megalovania.b4_note,125)
megalovania.play(megalovania.d5_note,250)
megalovania.play(megalovania.a4_note,375)
megalovania.play(megalovania.gs4_note,125)
wait(125)
megalovania.play(megalovania.g4_note,250)
megalovania.play(megalovania.f4_note,250)
megalovania.play(megalovania.d4_note,125)
megalovania.play(megalovania.f4_note,125)
megalovania.play(megalovania.g4_note,125)
#m4 undef as3
megalovania.play(megalovania.as4_note,125)
megalovania.play(megalovania.as4_note,125)
megalovania.play(megalovania.d5_note,250)
megalovania.play(megalovania.a4_note,375)
megalovania.play(megalovania.gs4_note,125)
wait(125)
megalovania.play(megalovania.g4_note,250)
megalovania.play(megalovania.f4_note,250)
megalovania.play(megalovania.d4_note,125)
megalovania.play(megalovania.f4_note,125)
megalovania.play(megalovania.g4_note,125)


