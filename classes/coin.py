import pygame as py
from random import randint

def main():
    pass

class Coin():
    def __init__(self):
        self._img_path = 'assets/graphics/Coin/semi-borderless-coin.png'
        self._y_pos = 210
        self.retangulo = self.get_image().get_rect(midbottom = (randint(900, 1100), self._y_pos))

    def __str__(self):
        '''
        Representação do objeto Coin em string.
        '''

        return 'Coin_Object'

    def get_image(self):
        '''
        Retorna imagem do objeto/elemento moeda.
        '''
        
        return py.image.load(self._img_path).convert_alpha()

    def move_para_esquerda(self, deslocamento):
        '''
        Modifica posição do objeto no eixo X da tela.
        '''

        self.retangulo.x -= deslocamento
 
if __name__ == '__main__':
    main()