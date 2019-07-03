#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
import random


#################################################
#               sensores                        #
#################################################

#som
sound = Sound()
#mover 
tank = MoveTank(OUTPUT_A,OUTPUT_D)
#garra
garra = MediumMotor(OUTPUT_C)
#sensor de cor
sensorLuz = ColorSensor(INPUT_2)
sensorLuz.mode='COL-COLOR'
#sensor de toque
sensorToque = TouchSensor(INPUT_1)
#sensor utra som
sensorSom = UltrasonicSensor(INPUT_3)
#leds cerebro
leds = Leds()
#giro
gs = GyroSensor(INPUT_4)


################################################
#                   variaveis                  #
################################################


#constantes
peca_final = 2 #n de pecas total 
peca_media = 1 #apanhou 1 peca


angulo_30 = 30
angulo_45 = 44
angulo_60 = 60
angulo_90 = 89
angulo_150 = 150
angulo_180 = 179
angulo_240 = 240
angulo_270 = 269
angulo_330 = 330
angulo_360 = 358

rotacoes_andar_Reconhecimento = 0.97
rotacoes_andar_cheiro = 3.8
rotacoes_andar_1_casa = 2.7
rotacoes_andar_2_casa = 5.2
rotacoes_dar_navalhada = 6.012

potencia_andar_Frente = -40
potencia_andar_navalhada= -90
potencia_andar_Tras = 40
potencia_garra_apanhar = 50
potencia_garra_largar = -50
potencia_esquerda_rodar_1 = -30
potencia_esquerda_rodar_2 = -12
potencia_direita_rodar_1 = 30
potencia_direita_rodar_2 = 12
distancia_detetar_zombie = 24

import time

#########################
#         Testes        #
#########################
while True:
    sensorLuz.mode='COL-COLOR'
    if sensorToque.value() ==1:

        garra.on_for_rotations(SpeedPercent(potencia_garra_apanhar),rotacoes_dar_navalhada)
        time.sleep(3)
        garra.on_for_rotations(SpeedPercent(potencia_garra_largar),rotacoes_dar_navalhada)

        #print(sensorLuz.color)
        sensorSom.mode = sensorSom.modes[0]
        print(sensorSom.distance_centimeters)
    #print(sensorSom.distance_centimeters)


            
