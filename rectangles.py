from images import *

from positions import *

#Gerando retângulos para cada imagem a partir de suas dimensões, e determinando seus pontos no espaço.
dino_rectangle = dino_image.get_rect(midbottom = (dino_x_pos, dino_y_pos))
stone_rectangle = stone_image.get_rect(midbottom = (stone_x_pos, stone_y_pos))
coin_rectangle = coin_image.get_rect(midbottom = (80, 230))