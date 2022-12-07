import pygame as py;
from sys import exit

#Inciializando jogo.
py.init()

#Instânciando classe clock, para controle de FPS.
clock = py.time.Clock()

#Definições do tamanho da tela do jogo.
dimensoes = largura, altura = 800, 400
tela = py.display.set_mode(dimensoes)

#Definindo legenda do jogo.
py.display.set_caption('Dinorun')

#Declarando variável com tipo de fonte do jogo.
fonte_do_jogo = py.font.Font("assets/font/PixelType.ttf", 50)

#Criando superfície com texto.
cabecalho_do_jogo = fonte_do_jogo.render("Dinorun", False, 'Green')

#Importando imagens do jogo.
sky_image = py.image.load('assets/graphics/Blue-Sky.png').convert_alpha()
ground_image = py.image.load('assets/graphics/Green-Ground.png').convert_alpha()


stone_image = py.image.load('assets/graphics/Stone/stone.png').convert_alpha()
stone_x_pos = 800
stone_y_pos = 315

dino_image = py.image.load('assets/graphics/Dinosaur/dinosaur.png').convert_alpha()
dino_x_pos = 80
dino_y_pos = 310

#Gerando retângulos para cada imagem a partir de suas dimensões, e determinando seus pontos no espaço.
dino_rectangle = dino_image.get_rect(midbottom = (dino_x_pos, dino_y_pos))
stone_rectangle = stone_image.get_rect(midbottom = (stone_x_pos, stone_y_pos))


def draw_images ():
    '''
    Adiciona imagens do jogo sobre a tela principal.
    '''

    tela.blit(sky_image, (0, 0))
    tela.blit(ground_image, (0, 300))
    tela.blit(cabecalho_do_jogo, (20, 20))

    #Variáveis _rectangle utilizadas como tupla de coordenadas.
    tela.blit(stone_image, stone_rectangle)
    tela.blit(dino_image, dino_rectangle)


def move_obstacle_in_window(obstacle_rectangle):
    '''
    Responsável pelo movimento constante dos obstáculos dentro da tela do jogo.
    '''
    
    obstacle_rectangle.left -= 10
    if obstacle_rectangle.right <= 0:
        obstacle_rectangle.left = 800

dino_gravity = 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        
        if event.type == py.KEYDOWN:
            if dino_rectangle.bottom == 310:
                if event.key == py.K_UP:
                    dino_gravity = -20

    draw_images()
    move_obstacle_in_window(stone_rectangle)

    dino_gravity += 1

    dino_rectangle.y += dino_gravity

    if dino_rectangle.bottom > 310:
        dino_rectangle.bottom = 310

    #Atualiza todos os componentes da tela.
    py.display.flip()

    #Define o FPS (Frames per Second - Quadros por Segundo) do jogo.
    clock.tick(60)
