import pygame as py;
from sys import exit
from random import randint


from start_pygame import *
from texts import *
from images import *
from positions import *
from rectangles import *

def object_movement(object_list):
    #Se houver algo na lista.
    if object_list:
        for object_rect in object_list:

            '''
            Verifica se o objeto é um obstáculo ou uma moeda, para desenhar em tela suas respectivas imagens com seus retângulos.
            Também define a velocidade com a qual cada objeto irá andar para a esquerda
            '''
            if object_rect.bottom == 210:
                object_rect.x -= 2
                tela.blit(coin_image, object_rect)
            else:
                object_rect.x -= 5
                tela.blit(stone_image, object_rect)

        '''
        Para cada obstáculo na lista, verifica se a posição X dele é maior que 0. Se sim, retorna esse obstáculo.
        O objetivo aqui, é descartar todos os objetos que já saíram da tela a 100px pelo lado esquerdo.
        '''
        object_list = [obstacle for obstacle in object_list if obstacle.x > -100]
        
        return object_list
    # No início do jogo, não haverá nada na lista de obstáculos, pois só são adicionados obstáculos na lista a cada 1.4 segundos
    else: return []

object_rect_list = []

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
    Finaliza o jogo se houver colisão entre o dinossauro e um obstáculo. Mas se houver colisão entre o dinossauro e uma moeda, 
    faz a moeda desaparecer.
    '''
    if obstacle_rectangles:
        for obstacle_rect in obstacle_rectangles:
            if dino_rect.colliderect(obstacle_rect):
                '''
                Se a colisão for com uma moeda, remove da lista de obstáculos, fazendo ela desaparecer.
                E se a colisão não for com uma moeda, retorna "True" para informar que houve colisão com um obstáculo.
                '''
                if obstacle_rect.bottom == 210:
                    obstacle_rectangles.remove(obstacle_rect)
                    return False
                else:
                    return True
                    
                
    return False

def restart_game(obstacle_rectangles):
    obstacle_rectangles = []
    return obstacle_rectangles

score = 0
start_offset = 0

def display_score():
    '''
    Essa função é responsável por exibir o score na tela de jogo.
    '''

    if active == True:
        score = (py.time.get_ticks() - start_offset)//100    
        score_text = fonte_do_jogo(40).render(f'Score: {score}', False, 'black')
        tela.blit(score_text, (350, 35))    
    return score
        

def show_initial_game_screen():
    '''
    Exibe tela inicial do jogo.
    '''

    tela.fill('#112e0a')
    tela.blit(initial_game_screen_text, (175, -20))
    tela.blit(start_text, (260, 370))
    py.display.flip()

def show_game_over_screen(game_over_text, score):
    tela.fill('#112e0a')
    tela.blit(game_over_text, (200, -20))
    score_final = fonte_inicio_fim_do_jogo(60).render(f"Your score: {str(score)}", False, 'white')
    tela.blit(score_final, (300, 100))
    tela.blit(restart_text, (190, 370))
    py.display.flip()

object_timer = py.USEREVENT + 1
py.time.set_timer(object_timer, 1400)

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
                start_offset = py.time.get_ticks()
        
        '''
        Adiciona o obstáculo pedra na lista de obstáculos que serão desenhados na tela após certo período de tempo.
        Esses obstáculos serão desenhados fora da tela, do lado direito, com posição X aleatória.
        '''
        if event.type == object_timer and not has_collided_with_obstacles(dino_rectangle, object_rect_list):
            if randint(0,2):

                object_rect_list.append(stone_image.get_rect(midbottom = (randint(900, 1100), stone_y_pos)))
            else:
                object_rect_list.append(coin_image.get_rect(midbottom = (randint(900, 1100), coin_y_pos)))


    if not has_collided_with_obstacles(dino_rectangle, object_rect_list):
        draw_images()
    
        #Efeito de pulo do dinossauro na tela.
        dino_jump(dino_rectangle, gravity)
        gravity += 1

        # Obstacle movement
        object_rect_list = object_movement(object_rect_list)

        ##Mostra a pontuação
        score = display_score()
        #Atualiza todos os componentes da tela.
        py.display.flip()

        #Define o FPS (Frames per Second - Quadros por Segundo) do jogo.
        clock.tick(60)
    else:
        
        active = False
        show_game_over_screen(game_over_text, score)
        
