import pygame as py;

py.init()


#Instanciando classe clock, para controle de FPS.
clock = py.time.Clock()

#Definições do tamanho da tela do jogo.
dimensoes = largura, altura = 800, 400
tela = py.display.set_mode(dimensoes)

#Definindo legenda do jogo.
py.display.set_caption('Dinorun')