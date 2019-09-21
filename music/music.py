from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch

class Music:
    def __init__(self):
        self.c4_note = [ 261.63, 'C4' ]
        self.cs4_note = [ 277.18, 'C#4' ]        
        self.d4_note = [ 293.66, 'D4' ]        
        self.ds4_note = [ 311.13, 'D#4' ]        
        self.e4_note = [ 329.63, 'E4' ]        
        self.f4_note = [ 349.23, 'F4' ]        
        self.fs4_note = [ 369.99, 'F#4' ]        
        self.g4_note = [ 392, 'G4' ]
        self.gs4_note = [ 415.3, 'G#4' ]        
        self.a4_note = [ 440, 'A4' ]        
        self.as4_note = [ 466.16, 'A#4' ]        
        self.b4_note = [ 493.88, 'B4' ]        
        self.c5_note = [ 523.25, 'C5' ]        
        self.cs5_note = [ 554.37, 'C#5' ]        
        self.d5_note = [ 587.33, 'D5' ]        
        self.ds5_note = [ 622.25, 'D#5' ]        
        self.e5_note = [ 659.25, 'E5' ]        
        self.f5_note = [ 698.46, 'F5' ]         
        self.fs5_note = [ 739.99, 'F#5' ]        
        self.g5_note = [ 783.99, 'G5' ]        
        self.gs5_note = [ 830.61, 'G#5' ]        
        self.a5_note = [ 880, 'A5' ]        
        self.as5_note = [ 932.33, 'A#5' ]        
        self.b5_note = [ 987.77, 'B5' ]        
        self.c6_note = [ 1046.5, 'C6' ]   
    # Music constructor

    def play(self, note, duration = 500):
        # Sixteenth 125
        # Eight 250
        # Quarter 500 
        # Half 1000
        brick.display.text( note[1], ( 60, 50 ) )
        brick.sound.beep( note[0], duration )
        wait(100)
    # Music play