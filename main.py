import pygame as py;
from sys import exit
from random import randint


from start_pygame import *

from texts import *

from images import *

from positions import *

from rectangles import *


def obstacle_movement(obstacle_list):
    #se há algo na lista
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            # obstacle_rect.x -= 5

            if obstacle_rect.bottom == 315:
                obstacle_rect.x -= 5
                tela.blit(stone_image, obstacle_rect)
            else:
                obstacle_rect.x -= 2
                tela.blit(coin_image, obstacle_rect)
        
        '''
        Para cada obstáculo na lista, verifica se a posição X dele é maior que 0. Se sim, retorna esse obstáculo.
        O objetivo aqui, é descartar todos os objetos que já saíram da tela a 100px pelo lado esquerdo.
        '''
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    # No início do jogo, não haverá nada na lista de obstáculos, pois só são adicionados obstáculos na lista a cada 1.4 segundos
    else: return []

obstacle_rect_list = []


def draw_images ():
    '''
    Adiciona imagens do jogo sobre a tela principal.
    '''

    tela.blit(sky_image, (0, 0))
    tela.blit(ground_image, (0, 300))
    
    # tela.blit(coin_image, coin_rectangle)

    tela.blit(cabecalho_do_jogo, (20, 20))

    #Variáveis _rectangle utilizadas como tupla de coordenadas.
    # tela.blit(stone_image, stone_rectangle)
    tela.blit(dino_image, dino_rectangle)


def dino_jump(dino_rect, dino_gravity):
    '''
    Responsável pelo efeito de pulo do dinossauro na tela.
    '''

    dino_rect.y += dino_gravity

    if dino_rect.bottom > 310:
        dino_rect.bottom = 310

gravity = int()

def has_collided_with_obstacles(dino_rect, obstacle_rectangles):
    '''
    Finaliza o jogo se houver colisão entre o dinossauro e um obstáculo.
    '''
    if obstacle_rectangles:
        for obstacle_rect in obstacle_rectangles:
            if dino_rect.colliderect(obstacle_rect):
                # print(obstacle_rect.bottom)
                if obstacle_rect.bottom == 210:
                    obstacle_rectangles.remove(obstacle_rect)
                    return False
                else:
                    return True
                    
                
    return False
def restart_game(obstacle_rectangles):
    obstacle_rectangles = []
    return obstacle_rectangles

def show_initial_game_screen():
    '''
    Exibe tela inicial do jogo.
    '''

    tela.fill('#112e0a')
    tela.blit(initial_game_screen_text, (175, -20))
    tela.blit(start_text, (260, 370))
    py.display.flip()

def show_game_over_screen(game_over_text):
    tela.fill('#112e0a')
    tela.blit(game_over_text, (200, -20))
    tela.blit(restart_text, (190, 370))
    py.display.flip()

obstacle_timer = py.USEREVENT + 1
py.time.set_timer(obstacle_timer, 1400)

#While loop para exibição de tela inicial do jogo.
while True:
    game_started = False

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        
        if event.type == py.KEYDOWN:
            game_started = True
    
    show_initial_game_screen()

    if game_started:
        break

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        
        if event.type == py.KEYDOWN:
            if dino_rectangle.bottom == 310:
                if event.key == py.K_UP:
                    gravity = -20
        
        if event.type == py.KEYDOWN:
            if has_collided_with_obstacles(dino_rectangle, obstacle_rect_list):
                obstacle_rect_list = restart_game(obstacle_rect_list)
        
        '''
        Adiciona o obstáculo pedra na lista de obstáculos que serão desenhados na tela após certo período de tempo.
        Esses obstáculos serão desenhados fora da tela, do lado direito, com posição X aleatória.
        '''
        if event.type == obstacle_timer and not has_collided_with_obstacles(dino_rectangle, obstacle_rect_list):
            if randint(0,2):

                obstacle_rect_list.append(stone_image.get_rect(midbottom = (randint(900, 1100), stone_y_pos)))
            else:
                obstacle_rect_list.append(coin_image.get_rect(midbottom = (randint(900, 1100), coin_y_pos)))

            # print("test")


    # collect_coin(obstacle_rect_list, coin_y_pos)

    if not has_collided_with_obstacles(dino_rectangle, obstacle_rect_list):
        draw_images()
    
        #Efeito de pulo do dinossauro na tela.
        dino_jump(dino_rectangle, gravity)
        gravity += 1

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Atualiza todos os componentes da tela.
        py.display.flip()

        #Define o FPS (Frames per Second - Quadros por Segundo) do jogo.
        clock.tick(60)
    else:
        show_game_over_screen(game_over_text)
