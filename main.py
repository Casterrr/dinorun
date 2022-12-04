## Importação da biblioteca.
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

#Definindo fonte do jogo.
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

## Pega a imagem e gera o retângulo com as dimensões dela. Toda imagem tem sua posição (x,y), originalmente, no canto superior esquerdo
#  dela.
## Porém, ao gerar o retângulo dela, dá pra mudar onde será a posição (x,y) dela. Por exemplo, pro centro seria "center".
dino_rectangle = dino_image.get_rect(midbottom = (dino_x_pos, dino_y_pos))
stone_rectangle = stone_image.get_rect(midbottom = (stone_x_pos, stone_y_pos))


def draw_images ():
    tela.blit(sky_image, (0, 0))
    tela.blit(ground_image, (0, 300))
    tela.blit(cabecalho_do_jogo, (20, 20))

    ## Aqui a posição (x,y) da pedra é a mesma do retângulo gerado pelas dimensões dela.
    tela.blit(stone_image, stone_rectangle)
    ## Aqui a posição (x,y) do dinossauro é a mesma do retângulo gerado pelas dimensões dele.
    tela.blit(dino_image, dino_rectangle)


def keep_obstacle_in_window(obstacle_rectangle):
    obstacle_rectangle.left -= 1
    if obstacle_rectangle.right <= 0:
        obstacle_rectangle.left = 800

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

    #Insere imagens na tela.
    draw_images()

    #Volta a posição da pedra quando ela atravessa a borda da tela.
    keep_obstacle_in_window(stone_rectangle)

    #Atualiza componentes da tela.
    py.display.flip()
    #Define FPS (Frames per Second ou Quadros por Segundo).
    clock.tick(120)