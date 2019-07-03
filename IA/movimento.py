
#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
import random
from zombie import *
from peca import *
from bala import *
import time


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



angulo_30 = 30
angulo_45 = 45
angulo_60 = 60
angulo_90 = 89
angulo_115 = 115
angulo_135 = 134
angulo_150 = 150
angulo_180 = 179
angulo_200 = 200
angulo_225 = 224
angulo_240 = 240
angulo_270 = 269
angulo_300 = 300
angulo_315 = 314
angulo_330 = 330
angulo_360 = 359


rotacoes_andar_Reconhecimento = 0.99 #0.97
rotacoes_andar_1_casa = 2.7
rotacoes_andar_2_casa = 5.2
rotacoes_dar_navalhada = 6.012 #6.3


potencia_andar_Frente = -35 #-40
potencia_andar_navalhada= -90
potencia_andar_Tras = 35 #40
potencia_garra_apanhar = 55
potencia_garra_largar = -55
potencia_esquerda_rodar_1 = -25 #-30
potencia_esquerda_rodar_2 = -12 #-12
potencia_direita_rodar_1 = 25 #30
potencia_direita_rodar_2 = 12 #12
distancia_detetar_zombie = 24

distancia_detetar_zombie_2_casas_min = 35
distancia_detetar_zombie_2_casas_max = 70
distancia_detetar_zombie_L_min = 10
distancia_detetar_zombie_L_max =50

global invert
invert = False
"""
global apagar_cheiro1_x
apagar_cheiro1_x = 0
global apagar_cheiro2_x
apagar_cheiro2_x = 0 
global apagar_cheiro3_x
apagar_cheiro3_x = 0
global apagar_cheiro4_x
apagar_cheiro4_x = 0
global apagar_cheiro5_x
apagar_cheiro5_x = 0
global apagar_cheiro6_x
apagar_cheiro6_x = 0
global apagar_cheiro7_x
apagar_cheiro7_x = 0
global apagar_cheiro8_x
apagar_cheiro8_x = 0

global apagar_cheiro1_y
apagar_cheiro1_y = 0
global apagar_cheiro2_y
apagar_cheiro2_y = 0 
global apagar_cheiro3_y
apagar_cheiro3_y = 0
global apagar_cheiro4_y
apagar_cheiro4_y = 0
global apagar_cheiro5_y
apagar_cheiro5_y = 0
global apagar_cheiro6_y
apagar_cheiro6_y = 0
global apagar_cheiro7_y
apagar_cheiro7_y = 0
global apagar_cheiro8_y
apagar_cheiro8_y = 0

"""
global conta_peca
conta_peca = 0 #n de peças

global existe_bala
existe_bala = False

global apanha
apanha = False
#tamanho do tabuleiro, cria uma linha com 6 valores, vez 6
w, h = 6, 6

global Matrix
#criação da matriz 6*6
Matrix = [[0 for x in range(w)] for y in range(h)] 
#se necessario é possivel meter 2 parametros em cada posicao da matriz


#robo
global x 
global y
x = 0
y = 0

#mudar de linha
global aux
aux = 0

global aux2
aux2 = 0

#alarme
global alarme
alarme = False


#posicoes da matrix

Matrix[y][x] = "robo"
Matrix[5][5] = "mota"



#limites da matrix

lim1 = 6
lim2 = -1

#print da matriz

def imprime(matriz):
    for col in matriz:
        print(col) 

#############################################
#            Funcoes para andar             #
#############################################

def andar_frente1():
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente), SpeedPercent(potencia_andar_Frente),rotacoes_andar_1_casa)

def andar_frente2():
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente),rotacoes_andar_2_casa)

def andar_tras1():
    tank.on_for_rotations(SpeedPercent(potencia_andar_Tras), SpeedPercent(potencia_andar_Tras),rotacoes_andar_1_casa)

def andar_tras2():
    tank.on_for_rotations(SpeedPercent(potencia_andar_Tras), SpeedPercent(potencia_andar_Tras),rotacoes_andar_2_casa)


def esquerda():
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_240:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_270:
        pass#90º direita
    tank.off()
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_1_casa)

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_330:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_360:
        pass#90º direita
    tank.off()

def esquerda2():
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_240:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_270:
        pass#90º direita
    tank.off()
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_2_casa)

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_330:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_360:
        pass#90º direita
    tank.off()

def direita():
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_60:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_90:
        pass#90º direita
    tank.off()
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_1_casa)

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_330:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_360:
        pass#90º direita
    tank.off()


def direita2():
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_60:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_90:
        pass#90º direita
    tank.off()
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_2_casa)
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_330:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_360:
        pass#90º direita
    tank.off()
         
#############################################


#############################################
#              Andar pela matrix            #
#             em procura de pecas           #
#############################################

# INVERT = FALSE

#############################
#                           #
#   #        ###########    #
#   #        #         #    #
#   #        #         #    #
#   #        #         #    #
#   #        #         #    #
#   #        #         #    #
#   #        #         #    #
#   ##########         #### #
#                           #
#############################       

#############################################
# INVERT = TRUE 

##############################
#   #####        ########### #
#       #        #         # #
#       #        #         # #
#       #        #         # #
#       #        #         # #
#       #        #         # #
#       #        #         # #
#       ##########         # #             
#                            #
##############################

def jogada(posicao):

    print("ANDAR PELO MAPA")

    global x
    global y
    global Matrix
    global invert
    global aux
    global aux2
    var = 0
    
    print("posicao jogada: ", posicao)
    #rota para andar
   
    if invert == False:
        aux2 = 0
        if aux < 5:
            if posicao != 1 and y+1 != lim1:
                if y+2 < lim1: 
                    if Matrix[y+2][x] == "zomb_cheiro":
                        Matrix[y+2][x] == 0
                        var = 1
                        andar_frente1()
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        

                    elif y+1 < lim1 and x+1 < lim1:
                    
                        if Matrix[y+1][x+1] == "zomb_cheiro":
                            Matrix[y+1][x+1] == 0
                            var = 4
                            andar_frente1()
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y + 1
                            Matrix[y][x] = "robo"
                            
                        else:
                            Matrix[y][x] = 0
                            andar_frente1()
                            y = y + 1
                            Matrix[y][x] = "robo"
                            aux = aux + 1
                    else:
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                                                                    
                elif y+1 < lim1 and x+1 < lim1:
                    
                    if Matrix[y+1][x+1] == "zomb_cheiro":
                        Matrix[y+1][x+1] == 0
                        var = 4
                        andar_frente1()
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        
                    else:
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                        
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1
                    Matrix[y][x] = "robo"
                    aux = aux + 1
                
            elif posicao == 1 and y+2 != lim1:

                Matrix[y][x] = 0
                andar_frente2()
                aux = aux + 2 
                y = y + 2
                Matrix[y][x] = "robo"

            elif posicao == 1 and y+2 == lim1 and x+1 != lim1:
                
                Matrix[y][x] = 0
                andar_frente1()
                esquerda()
                x = x + 1
                y = y + 1
                Matrix[y][x] = "robo"
                print("Y: ",y,"X: ",x)
                aux = aux + 1
    
            
            
        elif aux >= 5 and aux < 7:

            if posicao == 4 and x+2 != lim1:
                Matrix[y][x] = 0   
                esquerda2()
                aux = aux + 2 
                x = x + 2
                Matrix[y][x] = "robo"


            elif posicao != 4 and x+1 != lim1: 
                if x+2 < lim1:
                    if Matrix[y][x+2] == "zomb_cheiro":
                        Matrix[y][x+2] == 0
                        var = 4
                        esquerda()
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
                        

                    elif y-1 > lim2 and x+1 < lim1:
                        if Matrix[y-1][x+1] == "zomb_cheiro":
                            Matrix[y-1][x+1] == 0 
                            var = 3
                            esquerda()
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            x = x +1
                            Matrix[y][x] = "robo"  
                                   
                        else:
                            Matrix[y][x] = 0
                            esquerda()
                            x = x + 1
                            Matrix[y][x] = "robo"
                            aux = aux + 1
                    else:
                        Matrix[y][x] = 0
                        esquerda()
                        x = x + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                        
                                    
                elif y-1 > lim2 and x+1 < lim1:
                    if Matrix[y-1][x+1] == "zomb_cheiro":
                        var = 3
                        Matrix[y-1][x+1] == 0
                        esquerda()
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
                                       
                    else:
                        Matrix[y][x] = 0
                        esquerda()
                        x = x + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                        
                else:
                    Matrix[y][x] = 0
                    esquerda()
                    x = x + 1
                    Matrix[y][x] = "robo"
                    aux = aux + 1
                

        elif aux >= 7 and aux < 12:

            if posicao != 3 and y-1 != lim2: 
                if y-2 > lim2:
                    if Matrix[y-2][x] == "zomb_cheiro":
                            var = 3
                            andar_tras1()
                            Matrix[y-2][x] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y - 1
                            Matrix[y][x] = "robo"
                            
                    elif y-1 > lim2 and x+1 < lim1:

                        if Matrix[y-1][x+1] == "zomb_cheiro":
                                var = 4
                                andar_tras1()
                                Matrix[y-1][x+1] == 0
                                posicao = ataque_zombie(var)
                                aux = aux + 1
                                Matrix[y][x] = 0
                                y = y - 1
                                Matrix[y][x] = "robo"
                                
                        elif y-1 > lim2 and x-1 > lim2:
                            if Matrix[y-1][x-1] == "zomb_cheiro":
                                    var = 2
                                    andar_tras1()
                                    Matrix[y-1][x-1] == 0
                                    posicao = ataque_zombie(var)
                                    aux = aux + 1
                                    Matrix[y][x] = 0
                                    y = y - 1
                                    Matrix[y][x] = "robo"
                                    
                            else:
                                Matrix[y][x] = 0
                                andar_tras1()
                                y = y - 1 
                                Matrix[y][x] = "robo"
                                aux = aux + 1
                        else:
                            Matrix[y][x] = 0
                            andar_tras1()
                            y = y - 1 
                            Matrix[y][x] = "robo"
                            aux = aux + 1
                    else:
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1 
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                    
                    
                elif y-1 > lim2 and x+1 < lim1:

                    if Matrix[y-1][x+1] == "zomb_cheiro":
                            var = 4
                            andar_tras1()
                            Matrix[y-1][x+1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y - 1
                            Matrix[y][x] = "robo"
                            
                    elif y-1 > lim2 and x-1 > lim2:
                        if Matrix[y-1][x-1] == "zomb_cheiro":
                                var = 2
                                andar_tras1()
                                Matrix[y-1][x-1] == 0
                                posicao = ataque_zombie(var)
                                aux = aux + 1
                                Matrix[y][x] = 0
                                y = y - 1
                                Matrix[y][x] = "robo"  
                                         
                        else:
                            Matrix[y][x] = 0
                            andar_tras1()
                            y = y - 1 
                            Matrix[y][x] = "robo"
                            aux = aux + 1
                    else:
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1 
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                    
                elif y-1 > lim2 and x-1 > lim2:
                    if Matrix[y-1][x-1] == "zomb_cheiro":
                            var = 2
                            andar_tras1()
                            Matrix[y-1][x-1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y - 1
                            Matrix[y][x] = "robo"
                            
                    
                    else:
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1 
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                else:
                    Matrix[y][x] = 0
                    andar_tras1()
                    y = y - 1 
                    Matrix[y][x] = "robo"
                    aux = aux + 1

            elif posicao == 3 and y-2 != lim2:
                    
                Matrix[y][x] = 0
                andar_tras2()
                aux = aux + 2 
                y = y - 2 
                Matrix[y][x] = "robo"

            elif posicao == 3 and y-2 == lim2:

                Matrix[y][x] = 0
                andar_tras1()
                esquerda()
                y = y - 1
                x = x + 1 
                Matrix[y][x] = "robo"
                aux = aux + 1

        elif aux >= 12 and aux < 14:
           
            if posicao == 4 and x+2 != lim1:

                Matrix[y][x] = 0   
                esquerda2()
                x = x + 2
                Matrix[y][x] = "robo"
                aux = aux + 2 

            elif posicao != 4 and x+1 != lim1: 
                if y+1 < lim1 and x+1 < lim1:
                    if Matrix[y+1][x+1] == "zomb_cheiro":
                        var = 1
                        esquerda()
                        Matrix[y+1][x+1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
                        
                    elif x+2 < lim1:
                        if Matrix[y][x+2] == "zomb_cheiro":
                            var = 4
                            esquerda()
                            Matrix[y][x+2] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            x = x + 1
                            Matrix[y][x] = "robo"
                            
                        else:
                            Matrix[y][x] = 0
                            esquerda()
                            x = x + 1
                            Matrix[y][x] = "robo"
                            aux = aux + 1
                    else:
                        Matrix[y][x] = 0
                        esquerda()
                        x = x + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                    
                elif x+2 < lim1:
                    if Matrix[y][x+2] == "zomb_cheiro":
                        var = 4
                        esquerda()
                        Matrix[y][x+2] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
                        
                    else:
                        Matrix[y][x] = 0
                        esquerda()
                        x = x + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                
                else:
                    Matrix[y][x] = 0
                    esquerda()
                    x = x + 1
                    Matrix[y][x] = "robo"
                    aux = aux + 1
            
        
        elif aux >= 14 and aux <= 18:
            
            if posicao != 1 and y+1 != lim1:

                if y+2 < lim1:   
                    if Matrix[y+2][x] == "zomb_cheiro":
                        var = 1
                        andar_frente1()
                        Matrix[y+2][x] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        

                    elif y+1 < lim1 and x-1 > lim2:
                        if Matrix[y+1][x-1] == "zomb_cheiro":
                            var = 3
                            andar_frente1()
                            Matrix[y+1][x-1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y + 1
                            Matrix[y][x] = "robo"
                            
                        else:
                            Matrix[y][x] = 0
                            andar_frente1()
                            y = y + 1
                            Matrix[y][x] = "robo"
                            aux = aux + 1
                    else:
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                        
                    
                elif y+1 < lim1 and x-1 > lim2:
                    if Matrix[y+1][x-1] == "zomb_cheiro":
                        var = 3
                        andar_frente1()
                        Matrix[y+1][x-1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        
    
                    else:
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1
                        Matrix[y][x] = "robo"
                        aux = aux + 1
                
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1
                    Matrix[y][x] = "robo"
                    aux = aux + 1
            
                        
            elif posicao == 1 and y+2 != lim1:

                Matrix[y][x] = 0
                andar_frente2()
                y = y + 2
                Matrix[y][x] = "robo"
                aux = aux + 2 

            elif posicao == 1 and y+2 == lim1 and x+1 != lim1:
                
                Matrix[y][x] = 0
                andar_frente1()
                esquerda()
                x = x + 1
                y = y + 1
                Matrix[y][x] = "robo"
                aux = aux + 1
        
        if aux == 19:
            invert = True

        print("auxa: ",aux)         

    else:
        aux = 0 

        if aux2 < 5:

            if posicao != 3 and y-1 != lim2:
                if y-2 > lim2:

                    if Matrix[y-2][x] == "zomb_cheiro":
                        var = 3
                        andar_tras1()
                        Matrix[y-2][x] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                        
                    elif y-1 > lim2 and x-1 > lim2:
                        if Matrix[y-1][x-1] == "zomb_cheiro":
                            var = 4
                            andar_tras1()
                            Matrix[y-1][x-1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y - 1
                            Matrix[y][x] = "robo"
                            
                        else:
                            Matrix[y][x] = 0
                            andar_tras1()
                            y = y - 1
                            Matrix[y][x] = "robo"
                            aux2 = aux2 + 1
                    else:
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                    
                elif y-1 > lim2 and x-1 > lim2:
                    if Matrix[y-1][x-1] == "zomb_cheiro":
                        var = 4
                        andar_tras1()
                        Matrix[y-1][x-1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                        
                    else:
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                
                else:
                    Matrix[y][x] = 0
                    andar_tras1()
                    y = y - 1
                    Matrix[y][x] = "robo"
                    aux2 = aux2 + 1
                    
            elif posicao == 3 and y-2 != lim2:

                Matrix[y][x] = 0
                andar_tras2()
                y = y - 2
                Matrix[y][x] = "robo"
                aux2 = aux2 + 2

            elif posicao == 3 and y-2 == lim2 and x-1 != lim2:
                Matrix[y][x] = 0
                andar_tras1()
                direita()
                x = x - 1
                y = y - 1
                Matrix[y][x] = "robo"
                aux2 = aux2 + 1
            
        elif aux2 >= 5 and aux2 < 7:

            if posicao != 2 and x-1 != lim2:
                if x-2 > lim2:
                    if Matrix[y][x-2] == "zomb_cheiro":
                        var = 3
                        direita()
                        Matrix[y][x-2] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                        
                    elif y+1 < lim1 and x-2 > lim2 :
                        if Matrix[y+1][x-1] == "zomb_cheiro":
                            var = 1
                            direita()
                            Matrix[y+1][x-1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            x = x - 1
                            Matrix[y][x] = "robo"
                            
                        else:
                            Matrix[y][x] = 0
                            direita()
                            x = x - 1
                            Matrix[y][x] = "robo"
                            aux2 = aux2 + 1
                    else:
                        Matrix[y][x] = 0
                        direita()
                        x = x - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                    
                elif y+1 < lim1 and x-2 > lim2 :
                    if Matrix[y+1][x-1] == "zomb_cheiro":
                        var = 1
                        direita()
                        Matrix[y+1][x-1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                        
                    else:
                        Matrix[y][x] = 0
                        direita()
                        x = x - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                   
                else:
                    Matrix[y][x] = 0
                    direita()
                    x = x - 1
                    Matrix[y][x] = "robo"
                    aux2 = aux2 + 1
            

            elif posicao == 2 and x-2 != lim2:

                Matrix[y][x] = 0   
                direita2()
                x = x - 2
                Matrix[y][x] = "robo"
                aux2 = aux2 +2

        elif aux2 >= 7 and aux2 < 12:

            if posicao != 1 and y+1 != lim1:
                if y+2 < lim1 :
                    if Matrix[y+2][x] == "zomb_cheiro":
                        var = 1
                        andar_frente1()
                        Matrix[y+2][x] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        
                    elif y+1 < lim1 and x-1 > lim2:
                        if Matrix[y+1][x-1] == "zomb_cheiro":
                            var = 2
                            andar_frente1()
                            Matrix[y+1][x-1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y + 1
                            Matrix[y][x] = "robo"
                            
                        elif y+1 < lim1 and x+1 < lim1:
                            if Matrix[y+1][x+1] == "zombi_cheiro":
                                var = 4
                                andar_frente1()
                                Matrix[y+1][x+1] == 0
                                posicao = ataque_zombie(var)
                                aux = aux + 1
                                Matrix[y][x] = 0
                                y = y + 1
                                Matrix[y][x] = "robo"
                                
                            else:           
                                Matrix[y][x] = 0
                                andar_frente1()
                                y = y + 1 
                                Matrix[y][x] = "robo"
                                aux2 = aux2 + 1
                        else:           
                            Matrix[y][x] = 0
                            andar_frente1()
                            y = y + 1 
                            Matrix[y][x] = "robo"
                            aux2 = aux2 + 1
                    else:           
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1 
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                elif y+1 < lim1 and x-1 > lim2:
                    if Matrix[y+1][x-1] == "zomb_cheiro":
                        var = 2
                        andar_frente1()
                        Matrix[y+1][x-1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        
                    elif y+1 < lim1 and x+1 < lim1:
                        if Matrix[y+1][x+1] == "zombi_cheiro":
                            var = 4
                            andar_frente1()
                            Matrix[y+1][x+1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y + 1
                            Matrix[y][x] = "robo"
                            
                        else:           
                            Matrix[y][x] = 0
                            andar_frente1()
                            y = y + 1 
                            Matrix[y][x] = "robo"
                            aux2 = aux2 + 1
                    else:           
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1 
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                    
                elif y+1 < lim1 and x+1 < lim1:
                    if Matrix[y+1][x+1] == "zombi_cheiro":
                        var = 4
                        andar_frente1()
                        Matrix[y+1][x+1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                        
                    else:           
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1 
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1
                
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1 
                    Matrix[y][x] = "robo"
                    aux2 = aux2 + 1
                

            elif posicao == 1 and y+2 != lim1:
                    
                Matrix[y][x] = 0
                andar_frente2()
                y = y + 2 
                Matrix[y][x] = "robo"
                aux2 = aux2 + 2
            
            elif posicao == 1 and y+2 == lim1 and x-1 != lim2:
                
                Matrix[y][x] = 0
                andar_frente1()
                direita()
                x = x - 1
                y = y + 1
                Matrix[y][x] = "robo"
                aux2 = aux2 + 1

        elif aux2 >= 12 and aux2 < 14:
                        
            if posicao != 2 and x+1 != lim2: 
                if x+2 < lim1:
                    if Matrix[y][x+2] == "zomb_cheiro":
                        var = 2
                        direita()
                        Matrix[y][x+2] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                        
                    elif y-1 > lim2 and x-1 > lim2:
                        if Matrix[y-1][x-1] == "zomb_cheiro":
                            var = 3
                            direita()
                            Matrix[y-1][x-1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            x = x - 1
                            Matrix[y][x] = "robo"
                            
                        else: 
                            Matrix[y][x] = 0
                            direita()
                            x = x - 1
                            Matrix[y][x] = "robo"
                            aux2 = aux2 + 1 
                    else: 
                        Matrix[y][x] = 0
                        direita()
                        x = x - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1 
                    
                elif y-1 > lim2 and x-1 > lim2:
                    if Matrix[y-1][x-1] == "zomb_cheiro":
                        var = 3
                        direita()
                        Matrix[y-1][x-1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                        
                    else: 
                        Matrix[y][x] = 0
                        direita()
                        x = x - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1          
                       
                else:
                    Matrix[y][x] = 0
                    direita()
                    x = x - 1
                    Matrix[y][x] = "robo"
                    aux2 = aux2 + 1
                

            elif posicao == 2 and x+2 != lim2:

                Matrix[y][x] = 0   
                direita2()
                x = x - 2
                Matrix[y][x] = "robo"
                aux2 = aux2 + 2
        
        elif aux2 >= 14 and aux2 <= 18:
            
            if posicao != 3 and y-1 != lim2:
                if y-2 < lim1:
                    if Matrix[y-2][x] == "zomb_cheiro":
                        var = 3
                        andar_tras1()
                        Matrix[y-2][x] == 0 
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo" 
                                
                    elif y-1 > lim2 and x+1 < lim1:
                        if Matrix[y-1][x+1] == "zomb_cheiro":
                            var = 4
                            andar_tras1()
                            Matrix[y-1][x+1] == 0
                            posicao = ataque_zombie(var)
                            aux = aux + 1
                            Matrix[y][x] = 0
                            y = y - 1
                            Matrix[y][x] = "robo"
                            
                        else:  
                            Matrix[y][x] = 0
                            andar_tras1()
                            y = y - 1
                            Matrix[y][x] = "robo"
                            aux2 = aux2 + 1
                    else:  
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1    
                        
                elif y-1 > lim2 and x+1 < lim1:
                    if Matrix[y-1][x+1] == "zomb_cheiro":
                        var = 4
                        andar_tras1()
                        Matrix[y-1][x+1] == 0
                        posicao = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                        
                    else:  
                        Matrix[y][x] = 0
                        andar_tras1()
                        y = y - 1
                        Matrix[y][x] = "robo"
                        aux2 = aux2 + 1         
                        
                else:
                    Matrix[y][x] = 0
                    andar_tras1()
                    y = y - 1
                    Matrix[y][x] = "robo"
                    aux2 = aux2 + 1
                
                
            elif posicao == 3 and y-2 != lim2:

                Matrix[y][x] = 0
                andar_tras2()
                y = y - 2
                Matrix[y][x] = "robo"
                aux2 = aux2 + 2
            
            elif posicao == 3 and y-2 == lim2 and x+1 != lim1:
                
                Matrix[y][x] = 0
                andar_tras1()
                esquerda()
                x = x + 1 
                y = y - 1
                Matrix[y][x] = "robo"
                aux2 = aux2 + 1

        if aux2 == 19:
            invert = False
            
        print("auxa: ",aux)


#############################################

#############################################
#             Ir para a mota                #
#############################################
def jogada_meter_peca(posicao):
    print("JOGADA METER PECA")
    global x
    global y
    global Matrix
    global invert
    global alarme
    global apanha
    global aux2
    global aux
    print(posicao)
   
    
    if posicao != 1 and y+1 != lim1:
        if y+2 < lim1 :
            if Matrix[y+2][x] == "zomb_cheiro":
                var = 1
                andar_frente1()
                Matrix[y+2][x] == 0
                var2 = ataque_zombie(var)
                aux = aux + 1
                Matrix[y][x] = 0
                y = y + 1
                Matrix[y][x] = "robo"
                
            elif y+1 < lim1 and x+1 < lim1:
                if Matrix[y+1][x+1] == "zomb_cheiro":
                    var = 4
                    Matrix[y+1][x+1] == 0
                    andar_frente1()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"
                    
                elif y+1 < lim1 and x-1 > lim2:
                    if Matrix[y+1][x-1] == "zomb_cheiro":
                        var = 2
                        Matrix[y+1][x-1] == 0
                        andar_frente1()
                        var2 = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"  
                    else:
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1
                        Matrix[y][x] = "robo"
                
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1
                    Matrix[y][x] = "robo"
            else:
                Matrix[y][x] = 0
                andar_frente1()
                y = y + 1
                Matrix[y][x] = "robo"
                
        elif y+1 < lim1 and x+1 < lim1:
            if Matrix[y+1][x+1] == "zomb_cheiro":
                var = 4
                Matrix[y+1][x+1] == 0
                andar_frente1()
                var2 = ataque_zombie(var)
                aux = aux + 1
                Matrix[y][x] = 0
                y = y + 1
                Matrix[y][x] = "robo"
                
            elif y+1 < lim1 and x-1 > lim2:
                if Matrix[y+1][x-1] == "zomb_cheiro":
                    var = 2
                    Matrix[y+1][x-1] == 0
                    andar_frente1()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"     
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1
                    Matrix[y][x] = "robo"
            else:
                Matrix[y][x] = 0
                andar_frente1()
                y = y + 1
                Matrix[y][x] = "robo"
        
            
        elif y+1 < lim1 and x-1 > lim2:
            if Matrix[y+1][x-1] == "zomb_cheiro":
                var = 2
                Matrix[y+1][x-1] == 0
                andar_frente1()
                var2 = ataque_zombie(var)
                aux = aux + 1
                Matrix[y][x] = 0
                y = y + 1
                Matrix[y][x] = "robo"
                
            else:
                Matrix[y][x] = 0
                andar_frente1()
                y = y + 1
                Matrix[y][x] = "robo"
        
        else:
            Matrix[y][x] = 0
            andar_frente1()
            y = y + 1
            Matrix[y][x] = "robo"
        
    elif posicao == 1 and y+2 != lim1:

        Matrix[y][x] = 0
        y = y + 2
        andar_frente2()
        Matrix[y][x] = "robo"

    elif posicao == 1 and y+2 == lim1 and x+1 != lim1:
                
        Matrix[y][x] = 0
        andar_frente1()
        esquerda()
        x = x + 1
        y = y + 1
        Matrix[y][x] = "robo"

    else:   
        if posicao != 4 and x+1 != lim1 :
            if x+2 < lim1:
                if Matrix[y][x+2] == "zomb_cheiro":
                    Matrix[y][x+2] == 0
                    var = 4
                    esquerda()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo"
                    
                elif y-1 > lim2 and x-1 > lim2:

                    if Matrix[y-1][x-1] == "zomb_cheiro":
                        var = 3
                        Matrix[y-1][x-1] == 0
                        esquerda()
                        var2 = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
        
                    else:      
                        Matrix[y][x] = 0   
                        esquerda()
                        x = x + 1
                        Matrix[y][x] = "robo"
                else:      
                    Matrix[y][x] = 0   
                    esquerda()
                    x = x + 1
                    Matrix[y][x] = "robo"
                
                
            elif y-1 > lim2 and x-1 > lim2:

                if Matrix[y-1][x-1] == "zomb_cheiro":
                    var = 3
                    Matrix[y-1][x-1] == 0
                    esquerda()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo"
    
                else:      
                    Matrix[y][x] = 0   
                    esquerda()
                    x = x + 1
                    Matrix[y][x] = "robo"
            
            else:      
                Matrix[y][x] = 0   
                esquerda()
                x = x + 1
                Matrix[y][x] = "robo"
            
            

        elif posicao == 4 and x+2 != lim1:
            Matrix[y][x] = 0 
            esquerda2()  
            x = x + 2
            Matrix[y][x] = "robo"
        
            

    if y == 5 and x == 5 :
        largar_peca()
        alarme = False
        invert = True
        apanha = False
        
        print("alarme: ", alarme)
        print("inverte: ",invert)
        aux2 = 0
        
    
    print("COORDENADAS y , x")
    print(y,x)

    print("MATRIZ ATUALIZADA")
    imprime(Matrix)
    

#############################################

#############################################
#              Jogada final                 #
# Ir em direçao da mota para largar a ultima#
# peca e ganhar o jogo                      #
#############################################

# FALTA FAZER ESTA FUNCAO
def jogada_final(posicao):
    print("JOGADA FINAL")
    global x
    global y
    global Matrix
    global invert
    global alarme
    global apanha
    global aux2
    global aux
    print(posicao)
   
    
    if posicao != 1 and y+1 != lim1:
        if y+2 < lim1 :
            if Matrix[y+2][x] == "zomb_cheiro":
                var = 1
                andar_frente1()
                Matrix[y+2][x] == 0
                var2 = ataque_zombie(var)
                aux = aux + 1
                Matrix[y][x] = 0
                y = y + 1
                Matrix[y][x] = "robo"
                
            elif y+1 < lim1 and x+1 < lim1:
                if Matrix[y+1][x+1] == "zomb_cheiro":
                    var = 4
                    Matrix[y+1][x+1] == 0
                    andar_frente1()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"
                    
                elif y+1 < lim1 and x-1 > lim2:
                    if Matrix[y+1][x-1] == "zomb_cheiro":
                        var = 2
                        Matrix[y+1][x-1] == 0
                        andar_frente1()
                        var2 = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"  
                    else:
                        Matrix[y][x] = 0
                        andar_frente1()
                        y = y + 1
                        Matrix[y][x] = "robo"
                
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1
                    Matrix[y][x] = "robo"
            else:
                Matrix[y][x] = 0
                andar_frente1()
                y = y + 1
                Matrix[y][x] = "robo"
                
        elif y+1 < lim1 and x+1 < lim1:
            if Matrix[y+1][x+1] == "zomb_cheiro":
                var = 4
                Matrix[y+1][x+1] == 0
                andar_frente1()
                var2 = ataque_zombie(var)
                aux = aux + 1
                Matrix[y][x] = 0
                y = y + 1
                Matrix[y][x] = "robo"
                
            elif y+1 < lim1 and x-1 > lim2:
                if Matrix[y+1][x-1] == "zomb_cheiro":
                    var = 2
                    Matrix[y+1][x-1] == 0
                    andar_frente1()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"     
                else:
                    Matrix[y][x] = 0
                    andar_frente1()
                    y = y + 1
                    Matrix[y][x] = "robo"
            else:
                Matrix[y][x] = 0
                andar_frente1()
                y = y + 1
                Matrix[y][x] = "robo"
        
            
        elif y+1 < lim1 and x-1 > lim2:
            if Matrix[y+1][x-1] == "zomb_cheiro":
                var = 2
                Matrix[y+1][x-1] == 0
                andar_frente1()
                var2 = ataque_zombie(var)
                aux = aux + 1
                Matrix[y][x] = 0
                y = y + 1
                Matrix[y][x] = "robo"
                
            else:
                Matrix[y][x] = 0
                andar_frente1()
                y = y + 1
                Matrix[y][x] = "robo"
        
        else:
            Matrix[y][x] = 0
            andar_frente1()
            y = y + 1
            Matrix[y][x] = "robo"
        
    elif posicao == 1 and y+2 != lim1:

        Matrix[y][x] = 0
        y = y + 2
        andar_frente2()
        Matrix[y][x] = "robo"

    elif posicao == 1 and y+2 == lim1 and x+1 != lim1:
                
        Matrix[y][x] = 0
        andar_frente1()
        esquerda()
        x = x + 1
        y = y + 1
        Matrix[y][x] = "robo"

    else:   
        if posicao != 4 and x+1 != lim1 :
            if x+2 < lim1:
                if Matrix[y][x+2] == "zomb_cheiro":
                    Matrix[y][x+2] == 0
                    var = 4
                    esquerda()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo"
                    
                elif y-1 > lim2 and x-1 > lim2:

                    if Matrix[y-1][x-1] == "zomb_cheiro":
                        var = 3
                        Matrix[y-1][x-1] == 0
                        esquerda()
                        var2 = ataque_zombie(var)
                        aux = aux + 1
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
        
                    else:      
                        Matrix[y][x] = 0   
                        esquerda()
                        x = x + 1
                        Matrix[y][x] = "robo"
                else:      
                    Matrix[y][x] = 0   
                    esquerda()
                    x = x + 1
                    Matrix[y][x] = "robo"
                
                
            elif y-1 > lim2 and x-1 > lim2:

                if Matrix[y-1][x-1] == "zomb_cheiro":
                    var = 3
                    Matrix[y-1][x-1] == 0
                    esquerda()
                    var2 = ataque_zombie(var)
                    aux = aux + 1
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo"
    
                else:      
                    Matrix[y][x] = 0   
                    esquerda()
                    x = x + 1
                    Matrix[y][x] = "robo"
            
            else:      
                Matrix[y][x] = 0   
                esquerda()
                x = x + 1
                Matrix[y][x] = "robo"
            
            

        elif posicao == 4 and x+2 != lim1:
            Matrix[y][x] = 0 
            esquerda2()  
            x = x + 2
            Matrix[y][x] = "robo"
        
            

    if y == 5 and x == 5 :
        alarme = False
        largar_peca()
        sound.speak('i won Motherfuckers')
        
    print("COORDENADAS y , x")
    print(y,x)

    print("MATRIZ ATUALIZADA")
    imprime(Matrix)


##################################################   
# Funcao que retorna se tem de esperar ou        # 
# continuar a sua jogada normal, quando encontra #
# jogadas em que pode perde                      #
##################################################
def funcao():
    global x
    global y
    global Matrix
    global conta_peca
    global existe_bala
    global apanha
    global invert
    global alarme
    global aux
    global aux2

    var = False

    if invert == False:
        if aux < 5: 
            if y+2 < lim1 and x+1 < lim1 : 
                if Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x+1] == "zomb_cheiro":
                    var = True 

        elif aux >= 5 and aux < 7:
            if x+2 <lim1 and y-1 >lim2:
                if Matrix[y-1][x+1] == "zomb_cheiro" and Matrix[y][x+2] == "zomb_cheiro":
                    var = True

        elif aux >= 7 and aux < 12:
            if y -1 > lim2:
                if Matrix[y-1][x+1] == "zomb_cheiro" and Matrix[y-1][x-1] == "zomb_cheiro":
                    var = True
                elif y-2 > lim2:   
                    if Matrix[y-2][x] == "zomb_cheiro" and Matrix[y-1][x+1] == "zomb_cheiro":
                        var = True
                    elif Matrix[y-2][x] == "zomb_cheiro" and Matrix[y-1][x-1] == "zomb_cheiro":
                        var = True 
        elif aux >= 12 and aux < 14:
            if x+2 < lim1 and y+1 <lim1:
                if Matrix[y][x+2] == "zomb_chero" and Matrix[y+1][x+1] == "zomb_cheiro":
                    var= True 
            
        elif aux >= 14 and aux < 18:
            if y+2 < lim1 and x-1 > lim2 : 
                if Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x-1] == "zomb_cheiro":
                    var = True 
    else:
        if aux2 < 5: 
            if y-2 > lim2 and x-1 > lim2 : 
                if Matrix[y-2][x] == "zomb_cheiro" and Matrix[y-1][x-1] == "zomb_cheiro":
                    var = True 

        elif aux2 >= 5 and aux2 < 7:
            if x-2 > lim2 and y+1 <lim1:
                if Matrix[y+1][x+1] == "zomb_cheiro" and Matrix[y][x-2] == "zomb_cheiro":
                    var = True

        elif aux2 >= 7 and aux2 < 12:

            if y +1 <lim1:
                if Matrix[y+1][x+1] == "zomb_cheiro" and Matrix[y+1][x-1] == "zomb_cheiro":
                    var = True
                elif y+2 < lim1:   
                    if Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x+1] == "zomb_cheiro":
                        var = True
                    elif Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x-1] == "zomb_cheiro":
                        var = True 
        elif aux2 >= 12 and aux2 < 14:
            if x-2 > lim2 and y-1 >lim2:
                if Matrix[y][x-2] == "zomb_chero" and Matrix[y-1][x-1] == "zomb_cheiro":
                    var= True 
            
        elif aux2 >= 14 and aux2 < 18:
            if y-2 > lim2 and x+1 < lim1 : 
                if Matrix[y-2][x] == "zomb_cheiro" and Matrix[y-1][x+1] == "zomb_cheiro":
                    var = True 
    return var     

####################################################   
# Funcao que retorna se tem de esperar ou          # 
# continuar a sua jogada com objetivo de ir para   #
# a mota, quando encontra jogadas em que pode perde#                      
####################################################
def funcao2():
    global x
    global y
    global Matrix
    global conta_peca
    global existe_bala
    global apanha
    global invert
    global alarme
    global aux
    global aux2

    esperar = False
    if x-1 == lim2:
        if y+2 < lim1 and x+1 <lim1 :
            if Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x+1] == "zomb_cheiro":
                esperar = True
    elif x+1 == lim1:
        if y+2 < lim1 and x-1>lim2:
            if Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x-1] == "zomb_cheiro":
                esperar = True
    
    else:
        if y +1 < lim1:
            if Matrix[y+1][x-1] == "zomb_cheiro" and Matrix[y+1][x+1] == "zomb_cheiro":
                esperar = True
            elif y + 2 < lim1: 
                if Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x+1] == "zomb_cheiro":
                    esperar = True 
                elif Matrix[y+2][x] == "zomb_cheiro" and Matrix[y+1][x-1] == "zomb_cheiro":
                    esperar = True
        

    return esperar

################################################
# Decide a sua jogada consuante o seu objetivo,#
# dependendo do objetivo em que se encontra    #
# da prioridades aos dados obtidos             # 
# no reconhecimento                            #
################################################    

def decidirJogada(peca,bala,zombie,zom_pec):
    print("DECIDIR JOGADA")
    global x
    global y
    global Matrix
    global conta_peca
    global existe_bala
    global apanha
    global invert
    global alarme
    global aux
    global aux2
    
    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    print("giroscopio",gs.value())
  
    posicao = 0
    esperar_sem_peca = funcao()
    esperar_com_peca = funcao2()
    valor = False

#Modo até encontrar as pecas todas


    if conta_peca != 2 and apanha == False:
        #zombie
        if esperar_sem_peca == True:
            posicao = 0
        else:
            if zom_pec > 0 and existe_bala == True:

                ataque_zombie_com_bala(zom_pec)
                posicao = 0
                alarme = True
                apanha = True 
                conta_peca = conta_peca + 1
                jogada(posicao)
            

            elif zom_pec > 0 and existe_bala == False:
                posicao = ataque_zombie(zom_pec)
                jogada(posicao)
                alarme = True
                apanha = True 
                conta_peca = conta_peca + 1

            elif zombie > 0 and existe_bala == True:
                if peca > 0:
                    ataque_zombie_com_bala(zombie)
                    existe_bala = False
                    apanha_peca(peca) 
                    alarme = True
                    apanha = True
                    conta_peca = conta_peca + 1
                    if peca == 1:
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                    elif peca == 2:
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                    elif peca == 3:
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                    elif peca == 4:
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"
                else:
                    ataque_zombie_com_bala(zombie)
                    existe_bala = False
                    jogada(posicao)
        
            elif zombie > 0 and existe_bala == False:
                if peca > 0:
                    apanha_peca(peca)
                    posicao = ataque_zombie_com_peca(zombie)
                    
                    alarme = True
                    apanha = True
                    conta_peca = conta_peca + 1
                    if peca == 1:
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                    elif peca == 2:
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                    elif peca == 3:
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                    elif peca == 4:
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"  

                elif bala > 0: 
                    apanha_bala(bala)              
                    ataque_zombie_com_bala(zombie)
                    
                    existe_bala = True
                    if bala == 1:
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                    elif bala == 2:
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                    elif bala == 3:
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                    elif bala == 4:
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo" 

                else:
                    posicao = ataque_zombie(zombie)
                    jogada(posicao)
                print("posicao decide: ",posicao)

            #pecas
            elif peca > 0 :
                apanha_peca(peca) 
                alarme = True
                apanha = True
                conta_peca = conta_peca + 1
                if peca == 1:
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"
                elif peca == 2:
                    Matrix[y][x] = 0
                    x = x - 1
                    Matrix[y][x] = "robo"
                elif peca == 3:
                    Matrix[y][x] = 0
                    y = y - 1
                    Matrix[y][x] = "robo"
                elif peca == 4:
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo"

                #cheiro
                if y +1 != lim1 and valor == False:
                    if Matrix[y+1][x] =="zomb_cheiro":
                        ent = 1
                        posicao = ataque_zombie_com_peca(ent)
                        Matrix[y+1][x] =="0"
                        valor = True
                    
                if x +1 != lim1 and valor == False:
                    if Matrix[y][x+1] =="zomb_cheiro":
                        ent = 4
                        posicao = ataque_zombie_com_peca(ent)
                        Matrix[y][x+1] =="0" 
                        valor = True           
                if y -1 != lim2 and valor == False:
                    if Matrix[y-1][x] =="zomb_cheiro":
                        ent = 3
                        posicao = ataque_zombie_com_peca(ent)
                        Matrix[y-1][x] =="0"  
                        valor = True               
                
                if x - 1 != lim2 and valor == False:
                    if Matrix[y][x-1] =="zomb_cheiro":
                        ent = 2
                        posicao = ataque_zombie_com_peca(ent) 
                        Matrix[y][x-1] =="0" 
                        valor = True
                
            #bala
            elif bala > 0:
                apanha_bala(bala)
                existe_bala = True
                if bala == 1:
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"
                elif bala == 2:
                    Matrix[y][x] = 0
                    x = x - 1
                    Matrix[y][x] = "robo"
                elif bala == 3:
                    Matrix[y][x] = 0
                    y = y - 1
                    Matrix[y][x] = "robo"
                elif bala == 4:
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo"
                #cheiro
                if y +1 != lim1 and valor == False:
                    if Matrix[y+1][x] =="zomb_cheiro":
                        ent = 1
                        ataque_zombie_com_bala(ent)
                        Matrix[y+1][x] =="0"
                        valor = True
                    
                if x +1 != lim1 and valor == False:
                    if Matrix[y][x+1] =="zomb_cherio":
                        ent = 4
                        ataque_zombie_com_bala(ent)
                        Matrix[y][x+1] =="0" 
                        valor = True           
                if y -1 != lim2 and valor == False:
                    if Matrix[y-1][x] =="zomb_cherio":
                        ent = 3
                        ataque_zombie_com_bala(ent)
                        Matrix[y-1][x] =="0"  
                        valor = True               
                
                if x - 1 != lim2 and valor == False:
                    if Matrix[y][x-1] =="zomb_cherio":
                        ent = 2
                        ataque_zombie_com_bala(ent) 
                        Matrix[y][x-1] =="0" 
                        valor = True 
                
            #caso nao encontre nada
            elif bala == 0 and zombie == 0 and peca == 0 and zom_pec == 0:
                posicao = 0 
                jogada(posicao)
                    
                
            
#Caso ttenha encontrado 1 peca
    elif conta_peca != 2 and apanha == True:
        # ir para a mota e começar o recuonhecimento  e mete apanha = false depois de por tem de inverter a rota invert = True
        #zombie
        if esperar_com_peca == True:
            posicao = 0
        else:
            if zom_pec > 0 and existe_bala == True:
                ataque_zombie_com_bala(zom_pec)
                posicao = 0
                jogada_meter_peca(posicao)
                alarme = True
                apanha = True 
                conta_peca = conta_peca + 1

            elif zom_pec > 0 and existe_bala == False:
                posicao = ataque_zombie_com_peca(zom_pec)
                jogada_meter_peca(posicao)
                alarme = True
                apanha = True 
                conta_peca = conta_peca + 1


            elif zombie > 0 and existe_bala == True:
                ataque_zombie_com_bala(zombie)
                existe_bala = False
                jogada_meter_peca(posicao)

            elif zombie > 0 and existe_bala == False:
                if bala > 0:
                    posicao = ataque_zombie_com_peca(zombie)
                    apanha_bala_2(bala)
                    existe_bala = True

                    if bala == 1:
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                    elif bala == 2:
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                    elif bala == 3:
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                    elif bala == 4:
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo"                      
                #caso nao encontre nada
                else:
                    posicao = ataque_zombie_com_peca(zombie)
                    jogada_meter_peca(posicao)
                    print("posicao decide: ",posicao)
            
            #bala virtualmente
            elif bala > 0:
                apanha_bala_2(bala)
                existe_bala = True
                if bala == 1:
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"
                elif bala == 2:
                    Matrix[y][x] = 0
                    x = x - 1
                    Matrix[y][x] = "robo"
                elif bala == 3:
                    Matrix[y][x] = 0
                    y = y - 1
                    Matrix[y][x] = "robo"
                elif bala == 4:
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo" 

                if y +1 != lim1 and valor == False:
                    if Matrix[y+1][x] =="zomb_cheiro":
                        ent = 1
                        ataque_zombie_com_bala(ent)
                        Matrix[y+1][x] =="0"
                        valor = True
                    
                if x +1 != lim1 and valor == False:
                    if Matrix[y][x+1] =="zomb_cherio":
                        ent = 4
                        ataque_zombie_com_bala(ent)
                        Matrix[y][x+1] =="0" 
                        valor = True           
                if y -1 != lim2 and valor == False:
                    if Matrix[y-1][x] =="zomb_cherio":
                        ent = 3
                        ataque_zombie_com_bala(ent)
                        Matrix[y-1][x] =="0"  
                        valor = True               
                
                if x - 1 != lim2 and valor == False:
                    if Matrix[y][x-1] =="zomb_cherio":
                        ent = 2
                        ataque_zombie_com_bala(ent) 
                        Matrix[y][x-1] =="0" 
                        valor = True 
                    
            #caso nao encontre nada
            elif bala == 0 and zom_pec == 0 and zombie == 0:
                posicao = 0 
                jogada_meter_peca(posicao)

    elif conta_peca == 2 and apanha == True:
        #vai para o fim e acabar
        if esperar_com_peca == True:
            posicao = 0
        else:
                
            if zombie > 0 and existe_bala == True:
                ataque_zombie_com_peca(zombie)
                existe_bala = False
                jogada_final(posicao)

            elif zombie > 0 and existe_bala == False:
                if bala > 0:
                    posicao = ataque_zombie_com_peca(zombie)
                    apanha_bala_2(bala)
                    existe_bala = True
                    if bala == 1:
                        Matrix[y][x] = 0
                        y = y + 1
                        Matrix[y][x] = "robo"
                    elif bala == 2:
                        Matrix[y][x] = 0
                        x = x - 1
                        Matrix[y][x] = "robo"
                    elif bala == 3:
                        Matrix[y][x] = 0
                        y = y - 1
                        Matrix[y][x] = "robo"
                    elif bala == 4:
                        Matrix[y][x] = 0
                        x = x + 1
                        Matrix[y][x] = "robo" 
                #caso nao encontre nada
                else:
                    posicao = ataque_zombie_com_peca(zombie)
                    jogada_final(posicao)
            #bala virtualmente
            elif bala > 0:
                apanha_bala_2(bala)
                existe_bala = True
                if bala == 1:
                    Matrix[y][x] = 0
                    y = y + 1
                    Matrix[y][x] = "robo"
                elif bala == 2:
                    Matrix[y][x] = 0
                    x = x - 1
                    Matrix[y][x] = "robo"
                elif bala == 3:
                    Matrix[y][x] = 0
                    y = y - 1
                    Matrix[y][x] = "robo"
                elif bala == 4:
                    Matrix[y][x] = 0
                    x = x + 1
                    Matrix[y][x] = "robo" 

                if y +1 != lim1 and valor == False:
                    if Matrix[y+1][x] =="zomb_cheiro":
                        ent = 1
                        ataque_zombie_com_bala(ent)
                        Matrix[y+1][x] =="0"
                        valor = True
                    
                if x +1 != lim1 and valor == False:
                    if Matrix[y][x+1] =="zomb_cherio":
                        ent = 4
                        ataque_zombie_com_bala(ent)
                        Matrix[y][x+1] =="0" 
                        valor = True           
                if y -1 != lim2 and valor == False:
                    if Matrix[y-1][x] =="zomb_cherio":
                        ent = 3
                        ataque_zombie_com_bala(ent)
                        Matrix[y-1][x] =="0"  
                        valor = True               
                
                if x - 1 != lim2 and valor == False:
                    if Matrix[y][x-1] =="zomb_cherio":
                        ent = 2
                        ataque_zombie_com_bala(ent) 
                        Matrix[y][x-1] =="0" 
                        valor = True 

            #caso nao encontre nada
            elif bala == 0 and zombie == 0:
                posicao = 0       
                jogada_final(posicao)


#############################################

#############################################
#             Refresh na Matrix             #
#             cheiro do zombie              #
#############################################
def refresh(M):
    global Matrix
    global x
    global y 

    for lin in range(len(M)):
        for col in range(len(M[0])):
            if Matrix[lin][col] == "zomb_cheiro":
                Matrix[lin][col] = 0

#############################################
#             Cheiro do zombie              #
#############################################  
def cheirar():

    global Matrix
    global x
    global y 

    

    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    sensorLuz.mode='COL-COLOR'
    gs.value(0)
    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters

    time.sleep(1)
    if y+2 < lim1:
        if distancia >= distancia_detetar_zombie_2_casas_min and distancia <= distancia_detetar_zombie_2_casas_max :
            Matrix[y+2][x] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_30:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_45:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters
    if y+1 < lim1 and x-1 > lim2:
        if distancia >= distancia_detetar_zombie_L_min and distancia <= distancia_detetar_zombie_L_max: 
            Matrix[y+1][x-1] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]

    
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_60:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_90:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]
    if x-2 > lim2:
        if distancia >= distancia_detetar_zombie_2_casas_min and distancia <= distancia_detetar_zombie_2_casas_max :
            Matrix[y][x-2] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]
    
    #muda
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_115:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_135:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters
    if y-1 > lim2 and x-1 > lim2:
        if distancia >= distancia_detetar_zombie_L_min and distancia<= distancia_detetar_zombie_L_max: 
            Matrix[y-1][x-1] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_150:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_180:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters
    if y-2 > lim2:
        if distancia >= distancia_detetar_zombie_2_casas_min and distancia <= distancia_detetar_zombie_2_casas_max: 
            Matrix[y-2][x] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_200:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_225:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters
    if y-1 > lim2 and x+1 < lim1:
        if distancia >= distancia_detetar_zombie_2_casas_min and distancia <= distancia_detetar_zombie_2_casas_max: 
            Matrix[y-1][x+1] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_240:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_270:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters
    if x+2 < lim1:
        if distancia >= distancia_detetar_zombie_2_casas_min and distancia <= distancia_detetar_zombie_2_casas_max: 
            Matrix[y][x+2] = "zomb_cheiro"
            
        else:
            pass
    sensorSom.mode = sensorSom.modes[1]
    
    #muda2
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_300:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_315:
        pass#90º direita
    tank.off()
    tank.wait_until_not_moving

    sensorSom.mode = sensorSom.modes[0]

    distancia = sensorSom.distance_centimeters
    if y+1 < lim1 and x+1 < lim1:
        if distancia >= distancia_detetar_zombie_2_casas_min and distancia  <= distancia_detetar_zombie_2_casas_max: 
            Matrix[y+1][x+1] = "zomb_cheiro"
            
        else:
            pass
        sensorSom.mode = sensorSom.modes[1]
    
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle <angulo_330:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_360:
        pass#90º direita
    tank.off()
    


    

##################################################

##################################################
#            Reconhecimento
# Verifica os quadrados a volta a ver se encontra#
#  um zombi, peca ou bala e cheiro               #
#   grava em memoria e inicia a funcao dicidir   #
#    jogada                                      #
################################################## 
def iniciaJogada():
    global x
    global y
    global Matrix

    refresh(Matrix)

    print("---------------------")
    print("MATRIZ INICIAL")
    imprime(Matrix)

    gs.mode = 'GYRO-RATE'
    gs.mode = 'GYRO-ANG'
    sensorSom.mode = sensorSom.modes[0]
    sensorLuz.mode='COL-COLOR'
    sensorLuz.calibrate_white
    gs.value(0)
     
    
    zombie = 0 #saber a direçao do zombie
    bala = 0 #posicao da bala
    peca = 0 #posicao da peça
    zom_pec = 0

    

    # se for 0 pode ir pa frente; se for 1 nao pode
        
    #Avanca em cada direcao e faz a verificaçao do espaço e ve se tem algum obj
    #Frente
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_Reconhecimento)#frente
    tank.wait_until_not_moving
    if y+1 != lim1:
        if sensorLuz.color == 5: 
            Matrix[y+1][x] = "zombie"
            zombie = 1
        elif sensorLuz.color == 7:
            Matrix[y+1][x] = "bala"
            bala = 1
        elif sensorLuz.color == 2:
            Matrix[y+1][x] = "peca"
            peca = 1  
        elif sensorLuz.color == 1:
            Matrix[y+1][x] = "zom_pec"
            zom_pec = 1
        else:
            pass        
    tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_Reconhecimento)   #tras
    
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle < angulo_60:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    print(gs.angle)
    while gs.angle < angulo_90:
        pass#90º direita
    tank.off()
    print(gs.angle)
    #Direita
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_Reconhecimento) #frente
    tank.wait_until_not_moving
    
    if x-1 != lim2:
        if sensorLuz.color == 5:
            Matrix[y][x-1] = "zombie"
            zombie = 2
        elif sensorLuz.color == 7:
            Matrix[y][x-1] = "bala"
            bala = 2
        elif sensorLuz.color == 2:
            Matrix[y][x-1] = "peca"
            peca = 2
        elif sensorLuz.color == 1:
            Matrix[y+1][x] = "zom_pec"
            zom_pec = 2
        else:
            pass
    tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_Reconhecimento)
    
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle < angulo_150:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_180:
        pass#90º direita
    tank.off()
     
    #Tras
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_Reconhecimento) #frente    
    tank.wait_until_not_moving
    if y-1 != lim2:
        if sensorLuz.color == 5:
            Matrix[y-1][x] = "zombie"
            zombie = 3
        elif sensorLuz.color == 7:
            Matrix[y-1][x] = "bala"
            bala = 3
        elif sensorLuz.color == 2:
            Matrix[y-1][x] = "peca"
            peca = 3
        elif sensorLuz.color == 1:
            Matrix[y+1][x] = "zom_pec"
            zom_pec = 3
        else:
            pass
    tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_Reconhecimento) #tras
    
    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle < angulo_240:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_270:
        pass#90º direita
    tank.off() 

    #Esquerda
    tank.on_for_rotations(SpeedPercent(potencia_andar_Frente),SpeedPercent(potencia_andar_Frente), rotacoes_andar_Reconhecimento) 
    tank.wait_until_not_moving
    if x+1 != lim2:
        if sensorLuz.color == 5:
            Matrix[y][x+1] = "zombie"
            zombie = 4
        elif sensorLuz.color == 7:
            Matrix[y][x+1] = "bala"
            bala = 4
        elif sensorLuz.color == 2:
            Matrix[y][x+1] = "peca"
            peca = 4
        elif sensorLuz.color == 1:
            Matrix[y+1][x] = "zom_pec"
            zom_pec = 4       
        else:
            pass
    tank.on_for_rotations(SpeedPercent(potencia_andar_Tras),SpeedPercent(potencia_andar_Tras), rotacoes_andar_Reconhecimento)#tras

    tank.on(SpeedPercent(potencia_esquerda_rodar_1), SpeedPercent(potencia_direita_rodar_1))
    while gs.angle < angulo_330:
        pass#90º direita
    tank.on(SpeedPercent(potencia_esquerda_rodar_2), SpeedPercent(potencia_direita_rodar_2))
    while gs.angle < angulo_360:
        pass#90º direita
    tank.off()
    
    
    
    
    print("MATRIZ RECONHECIMENTO")
    imprime(Matrix)  
    print("zombie",zombie)
    print("peca",peca)
    print("bala",bala)
    print("zomb_pec",zom_pec)
    
    cheirar()
    print("MATRIZ CHEIRO")
    imprime(Matrix)  
    
    decidirJogada(peca,bala,zombie,zom_pec)
    

#############################################
#               Retornar alarme             #
#############################################

def getAlarme():
    global alarme
    return alarme 

