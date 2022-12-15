import pygame as py;
from sys import exit
from random import randint

from start_pygame import *
from texts import *
from images import *
from rectangles import *
from functions import *
from Coin import *
from Stone import *

def cria_objetos(lista_de_objetos):
    '''
    Cria de maneira randômica objetos moedas ou pedra, e os adiciona a uma dada lista.
    '''

    if randint(0,2):
        lista_de_objetos.append(Coin())
    else:
        lista_de_objetos.append(Stone())
    
    print(lista_de_objetos)

def movimenta_objetos(janela_do_jogo, lista_de_objetos):
    '''
    Move objetos de uma dada lista na em uma dada tela do jogo.
    Ao final, retorna a lista sem os objetos que estão fora da tela.
    '''
    
    if lista_de_objetos:
        for objeto in lista_de_objetos:

            if objeto.__str__() == "Coin_Object":
                objeto.move_para_esquerda(2)
                janela_do_jogo.blit(objeto.get_image(), objeto.retangulo)
            elif objeto.__str__() == "Stone_Object":
                objeto.move_para_esquerda(5)
                tela.blit(objeto.get_image(), objeto.retangulo)

            #Atualiza lista, removendo objetos fora da tela.
            lista_de_objetos = [objeto for objeto in lista_de_objetos if objeto.retangulo.x > -100]

    #Retorna lista atualizada.   
    return lista_de_objetos

object_rect_list = list()

conteudo_tela_de_inicio = [(texto_da_tela_de_incio, (185, -20)), (texto_instrutivo_iniciar_jogo, (265, 370))]
conteudo_tela_de_jogatina = [(sky_image, (0, 0)), (ground_image, (0, 300)), (cabecalho_do_jogo, (20, 20)), (dino_image, dino_rectangle)]
conteudo_tela_de_fim_do_jogo = [(texto_de_fim_de_jogo, (215, -20)), (texto_instrutivo_reiniciar_jogo, (265, 370))]

gravity = int()

def has_collided_with_obstacles(dino_rect, lista_de_objetos):
    '''
    Finaliza o jogo se houver colisão entre o dinossauro e um obstáculo. 
    Se houver colisão entre o dinossauro e uma moeda, faz a moeda desaparecer.
    '''

    if lista_de_objetos:
        for objeto in lista_de_objetos:
            if dino_rect.colliderect(objeto.retangulo):
                '''
                Se a colisão for com uma moeda, remove da lista de obstáculos, fazendo ela desaparecer.
                E se a colisão não for com uma moeda, retorna "True" para informar que houve colisão com um obstáculo.
                '''
                if objeto.__str__() == 'Coin_Object':
                    lista_de_objetos.remove(objeto)
                    return False
                else:
                    return True
        else:
            return False

def restart_game(obstacle_rectangles):
    '''
    Recebe uma lista de objetos e retorna ela vazia.
    '''

    obstacle_rectangles = []
    return obstacle_rectangles

object_timer = py.USEREVENT + 1
py.time.set_timer(object_timer, 1400)

inicia_jogo(tela, conteudo_tela_de_inicio)

while True:
    active = True
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        
        if event.type == py.KEYDOWN:
            if dino_rectangle.bottom == 310:
                if event.key == py.K_UP:
                    gravity = -20
        
        if event.type == py.KEYDOWN:
            if has_collided_with_obstacles(dino_rectangle, object_rect_list):
                object_rect_list = restart_game(object_rect_list)
                #start_offset = py.time.get_ticks()
        
        '''
        Adiciona o obstáculo pedra na lista de obstáculos que serão desenhados na tela após certo período de tempo.
        Esses obstáculos serão desenhados fora da tela, do lado direito, com posição X aleatória.
        '''
        if event.type == object_timer and not has_collided_with_obstacles(dino_rectangle, object_rect_list):
            cria_objetos(object_rect_list)

    if not has_collided_with_obstacles(dino_rectangle, object_rect_list):
        exibe_tela_de_jogatina(tela, conteudo_tela_de_jogatina)
    
        #Efeito de pulo do dinossauro na tela.
        dino_jump(dino_rectangle, gravity)
        gravity += 1

        # Obstacle movement
        object_rect_list = movimenta_objetos(tela, object_rect_list)

        ##Mostra a pontuação
        #score = display_score()

        #Atualiza todos os componentes da tela.
        py.display.flip()

        #Define o FPS (Frames per Second - Quadros por Segundo) do jogo.
        clock.tick(60)
    else:
        active = False
        exibe_tela_de_fim_de_jogo(tela, conteudo_tela_de_fim_do_jogo)
        py.display.flip()