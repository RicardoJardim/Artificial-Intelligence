#!/usr/bin/env python3
from peca import *
from movimento import *
from bala import *
from zombie import * 
#CONTEM TODOS OS FICHEIROS PY 


##################################
#             MAIN               #
##################################
sound.speak('Hello motherfuckers')

while True:

    if sensorToque.value() == 1: 
        sensorLuz.mode='COL-COLOR'
        iniciaJogada()
        leds.set_color("RIGHT","GREEN")
        leds.set_color("LEFT", "GREEN")
            
    else:
        leds.set_color("RIGHT", "RED")
        leds.set_color("LEFT", "RED")
    
    alarme = getAlarme()

    if alarme == True:
       sound.tone(2000,2000)
    else:
        pass