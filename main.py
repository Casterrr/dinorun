## Importação da biblioteca
import pygame as py;
from sys import exit

## Inicia o pygame
py.init()

## Diz o tamanho da janela
screen = py.display.set_mode((800, 400))

## Altera o nome do jogo
py.display.set_caption('Dinorun')

## Usado pra definir o FPS posteriormente
clock = py.time.Clock()

## Define uma fonte de texto
# test_font = py.font.SysFont("chiller", 50)
test_font = py.font.Font("assets/font/PixelType.ttf", 50)

## Define um plano advindo de uma imagem, que é convertida pra um formato que o pygame entende melhor.
sky_surface = py.image.load('assets/graphics/Blue-Sky.png').convert_alpha()
ground_surface = py.image.load('assets/graphics/Green-Ground.png').convert_alpha()

## Define um plano para a fonte, onde o primeiro parâmetro é o texto, o segundo é um boolean pro anti-aliasing, e o terceiro é a cor do texto.
text_surface = test_font.render("Dinorun", False, 'Green')


stone_surface = py.image.load('assets/graphics/Stone/stone.png').convert_alpha()
stone_x_pos = 800
stone_y_pos = 315

dino_surface = py.image.load('assets/graphics/Dinosaur/dinosaur.png').convert_alpha()
dino_x_pos = 80
dino_y_pos = 310

## Pega a imagem e gera o retângulo com as dimensões dela. Toda imagem tem sua posição (x,y), originalmente, no canto superior esquerdo
#  dela.
## Porém, ao gerar o retângulo dela, dá pra mudar onde será a posição (x,y) dela. Por exemplo, pro centro seria "center".
dino_rectangle = dino_surface.get_rect(midbottom = (dino_x_pos, dino_y_pos))
stone_rectangle = stone_surface.get_rect(midbottom = (stone_x_pos, stone_y_pos))


def draw_surfaces ():
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (20, 20))

    ## Aqui a posição (x,y) da pedra é a mesma do retângulo gerado pelas dimensões dela.
    screen.blit(stone_surface, stone_rectangle)
    ## Aqui a posição (x,y) do dinossauro é a mesma do retângulo gerado pelas dimensões dele.
    screen.blit(dino_surface, dino_rectangle)


def keep_obstacle_in_window(obstacle_rectangle):
    obstacle_rectangle.left -= 1
    if obstacle_rectangle.right <= 0:
        obstacle_rectangle.left = 800

while True:
    ## Para cada evento disparado
    for event in py.event.get():
        ## verifique se o tipo dele é do tipo "SAIR" (fechar o jogo)
        if event.type == py.QUIT:
            py.quit()
            exit()

    ## Coloca o plano na janela
    draw_surfaces()

    ## Volta a posição da pedra quando ela atravessa a borda da janela.
    keep_obstacle_in_window(stone_rectangle)

    ## atualiza a tela
    py.display.update()
    ## define quantos quadros serão exibidos a cada segundo.
    clock.tick(120)