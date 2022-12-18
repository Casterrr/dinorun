import pygame as py;
from sys import exit
from random import randint

from classes.dinosaur import Dinosaur
from classes.screen import *

def main():
    
    #_______________________ DEFINIÇÕES INICIAIS/NECESSÁRIAS DO JOGO ____________________#
 
    #Iniciando biblioteca pygame.
    py.init()

    #Instanciando classe clock, para controle de FPS.
    clock = py.time.Clock()

    #Declarando principais variáveis de instância do jogo.
    tela = Window()
    dino = Dinosaur()
    
    #Configurando instâncias.
    tela.set_conteudo_do_jogo({'dinossauro': dino, 'objetos': list()})
    tela.set_clock_game_variable(clock)
    #____________________________________________________________________________________#

    tela.exibe_tela_inicial_de_jogo()

    while True:
        tela.exibe_tela_durante_jogo()
        tela.exibe_tela_final_de_jogo()

if __name__ == '__main__':
    main()
