#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# # Write your program here
# brick.sound.beep()

# # Write your program here
# tuning_motor = Motor(Port.B)
# play_button = TouchSensor(Port.S1)
# end_button = TouchSensor(Port.S2)


# def angle_converter(angle):
#     if angle <= 0:
#         return [ 261.63, 'C4' ]        
#     elif 0 < angle <= 30:
#         return [ 277.18, 'C#4' ]        
#     elif 30 < angle <= 60:    
#         return [ 293.66, 'D4' ] 
#     elif 60 < angle <= 90:    
#         return [ 329.63, 'D#4' ]
#     elif 90 < angle <= 120:    
#         return [ 349.23, 'E4' ] 
#     elif 120 < angle <= 150:    
#         return [ 369.99, 'F4' ] 
#     elif 150 < angle <= 180:    
#         return [ 392, 'F#4' ]   
#     elif 180 < angle <= 210:    
#         return [ 415.30, 'G4' ] 
#     elif 210 < angle <= 240:    
#         return [ 440, 'A4' ]    
#     elif 240 < angle <= 270:    
#         return [ 466.16, 'A#4' ]
#     elif 270 < angle <= 300:    
#         return [ 493.88, 'B4' ] 
#     elif 300 < angle <= 330:    
#         return [ 523.25, 'C5' ] 
#     elif 330 < angle <= 360:    
#         return [ 554.37, 'C#5' ]
#     elif 360 < angle <= 390:    
#         return [ 587.33, 'D5' ] 
#     elif 390 < angle <= 420:    
#         return [ 622.25, 'D#5' ]
#     elif 420 < angle <= 450:    
#         return [ 659.25, 'E5' ] 
#     elif 450 < angle <= 480:    
#         return [ 698.46, 'F5' ] 
#     elif 480 < angle <= 510:    
#         return [ 739.99, 'F#5' ]
#     elif 510 < angle <= 540:    
#         return [ 783.99, 'G5' ] 
#     elif 540 < angle <= 570:    
#         return [ 830.61, 'G#5' ]
#     elif 570 < angle <= 600:    
#         return [ 880, 'A5' ]    
#     elif 600 < angle <= 630:    
#         return [ 932.33, 'A#5' ]
#     elif 630 < angle <= 660:    
#         return [ 987.77, 'B5' ] 
#     elif angle > 660:    
#         return [ 1046.5, 'C6' ] 


# while not end_button.pressed():
#     brick.display.clear()
#     frequency, note = angle_converter(tuning_motor.angle())
#     brick.display.text(note, (60, 50))
#     wait(100)
#     if play_button.pressed():
#         while play_button.pressed():
#             brick.sound.beep(frequency)

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


