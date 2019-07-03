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

rotacoes_andar_Reconhecimento = 0.7
rotacoes_andar_1_casa = 2.7
rotacoes_andar_2_casa = 5.2
rotacoes_andar_navalhada = 1.5
rotacoes_dar_navalhada = 6.012

potencia_andar_Frente = -25
potencia_andar_navalhada= -90
potencia_andar_Tras = 25
potencia_garra_apanhar = 50
potencia_garra_largar = -50
potencia_esquerda_rodar_1 = -40
potencia_esquerda_rodar_2 = -15
potencia_direita_rodar_1 = 40
potencia_direita_rodar_2 = 15
distancia_detetar_zombie = 24


angulo_60 = 60
angulo_90 = 88
angulo_150 = 150
angulo_180 = 178
angulo_240 =240
angulo_270 = 268
angulo_330 = 330
angulo_360 = 358

##############################

def ataque_zombie(zombie):
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'

    posicao_ocupada = 0

    if zombie == 1: #atacar para a frente

        garra.on_for_rotations(SpeedPercent(potencia_garra_apanhar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        garra.on_for_rotations(SpeedPercent(potencia_garra_largar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        
        posicao_ocupada = 1
    
    

    elif zombie == 2: #atacar para a direita

        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_60:
            pass #90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_90:
            pass#90º direita
        tank.off()
        garra.on_for_rotations(SpeedPercent(potencia_garra_apanhar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        garra.on_for_rotations(SpeedPercent(potencia_garra_largar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        tank.on(SpeedPercent(potencia_esquerda_rodar_1),SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass
        tank.on(SpeedPercent(potencia_esquerda_rodar_2),SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass
        tank.off()

        posicao_ocupada = 2

    elif zombie == 3: #atacar para a esquerda

        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_150:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_180:
            pass#90º direita
        tank.off()
        garra.on_for_rotations(SpeedPercent(potencia_garra_apanhar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        garra.on_for_rotations(SpeedPercent(potencia_garra_largar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        tank.on(SpeedPercent(potencia_esquerda_rodar_1),SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass
        tank.on(SpeedPercent(potencia_esquerda_rodar_2),SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass
        tank.off()

        posicao_ocupada = 3

    elif zombie == 4: #atacar para tras

        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_240:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_270:
            pass#90º direita
        tank.off()
        garra.on_for_rotations(SpeedPercent(potencia_garra_apanhar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        garra.on_for_rotations(SpeedPercent(potencia_garra_largar), rotacoes_dar_navalhada)
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        tank.on(SpeedPercent(potencia_esquerda_rodar_1),SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass
        tank.on(SpeedPercent(potencia_esquerda_rodar_2),SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass
        tank.off()

        posicao_ocupada = 4

    return posicao_ocupada 

def ataque_zombie_com_peca(zombie):
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    posicao_ocupada = 0

    if zombie == 1: #atacar para a frente

        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        
        posicao_ocupada = 1
    
    

    elif zombie == 2: #atacar para a direita

        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_60:
            pass #90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_90:
            pass#90º direita
        tank.off()
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        tank.on(SpeedPercent(potencia_esquerda_rodar_1),SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass
        tank.on(SpeedPercent(potencia_esquerda_rodar_2),SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass
        tank.off()

        posicao_ocupada = 2

    elif zombie == 3: #atacar para a esquerda

        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_150:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_180:
            pass#90º direita
        tank.off()
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        tank.on(SpeedPercent(potencia_esquerda_rodar_1),SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass
        tank.on(SpeedPercent(potencia_esquerda_rodar_2),SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass
        tank.off()
        posicao_ocupada = 3

    elif zombie == 4: #atacar para tras

        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_240:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_270:
            pass#90º direita
        tank.off()
        tank.on_for_rotations(SpeedPercent(potencia_andar_navalhada),SpeedPercent(potencia_andar_navalhada), rotacoes_andar_navalhada) #frente
        tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_navalhada) #tras
        tank.on(SpeedPercent(potencia_esquerda_rodar_1),SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass
        tank.on(SpeedPercent(potencia_esquerda_rodar_2),SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass
        tank.off()

        posicao_ocupada = 4

    return posicao_ocupada 

def ataque_zombie_com_bala(zombie):
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    if zombie == 1: #atacar para a frente
        sound.tone(2600, 1400)
        sound.tone(3400, 1400)
        sound.tone(1350, 1400)



    elif zombie == 2:
        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_60:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_90:
            pass#90º direita
        tank.off()
        sound.tone(2600, 1400)
        sound.tone(3400, 1400)
        sound.tone(1350, 1400)        
        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass#90º direita
        tank.off()

    elif zombie == 3:
        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_150:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_180:
            pass#90º direita
        tank.off()
        sound.tone(2600, 1400)
        sound.tone(3400, 1400)
        sound.tone(1350, 1400)        
        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass#90º direita
        tank.off()

    elif zombie == 4:
        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_240:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_270:
            pass#90º direita
        tank.off()
        sound.tone(2600, 1400)
        sound.tone(3400, 1400)
        sound.tone(1350, 1400)        
        tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
        while gs.angle < angulo_330:
            pass#90º direita
        tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
        while gs.angle < angulo_360:
            pass#90º direita
        tank.off()
