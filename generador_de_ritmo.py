import sys
import pygame 
from pygame import mixer 
import random

pygame.init()
size = 800, 600
sonido_hihat = mixer.Sound(r'./hihat.ogg')
sonido_snare = mixer.Sound(r'./snare.ogg')
sonido_kick = mixer.Sound(r'./kick.ogg')
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Generador de ritmo")
run = True
beatTimer = 0
halfBeatTimer = 0
quaterBeatTimer = 0
beatFullCount = 0
halfBeatFullCount = 0
quaterBeatFullCount = 0
BPM = int(input("ingrese los bpm: "))
beatInterval = (60/BPM)*1000
halfBeatInterval = beatInterval / 2
quaterBeatInterval = beatInterval / 4

cl = [random.randint(3,4), 4]
print(str(cl))

opciones = [1,2,4]
opcion = random.choice(opciones)
subdivision_clave = opcion * cl[0]
print(str(subdivision_clave))

clave = []
filler = []
metrica = []

for i in range(0, subdivision_clave):
    clave.append(random.randint(0,1))
    filler.append(random.randint(0,1))
    metrica.append(random.randint(0,1))

print("clave: " + str(clave))
print("filler: " + str(filler))
print("metrica: " + str(metrica))

while run:
    beatFull = False
    halfBeatFull = False
    quaterBeatFull = False
    pygame.time.delay(1)
    beatTimer += 1
    halfBeatTimer += 1
    quaterBeatTimer += 1
    
    if opcion == 1:
        if(beatTimer >= beatInterval):
            beatTimer -= beatInterval
            beatFull = True
            beatFullCount += 1
            if clave[beatFullCount % subdivision_clave] == 1:
                sonido_kick.play()
            if filler[beatFullCount % subdivision_clave] == 1:
                sonido_snare.play()
            if metrica[beatFullCount % subdivision_clave] == 1:
                sonido_hihat.play()
            # print("Full Beat")

    if opcion == 2:
        if(halfBeatTimer >= halfBeatInterval):
            halfBeatTimer -= halfBeatInterval
            halfBeatFull = True
            halfBeatFullCount += 1
            if clave[halfBeatFullCount % subdivision_clave] == 1:
                sonido_kick.play()
            if filler[halfBeatFullCount % subdivision_clave] == 1:
                sonido_snare.play()
            if metrica[halfBeatFullCount % subdivision_clave] == 1:
                sonido_hihat.play()
            # print("Half Beat")

    if opcion == 4:
        if(quaterBeatTimer >= quaterBeatInterval):
            quaterBeatTimer -= quaterBeatInterval
            quaterBeatFull = True
            quaterBeatFullCount += 1
            if clave[quaterBeatFullCount % subdivision_clave] == 1:
                sonido_kick.play()
            if filler[quaterBeatFullCount % subdivision_clave] == 1:
                sonido_snare.play()
            if metrica[quaterBeatFullCount % subdivision_clave] == 1:
                sonido_hihat.play()
            # print("Quater Beat")

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

pygame.quit()


