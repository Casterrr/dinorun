import pygame as py
from random import randint

class Stone():
    def __init__(self):
        self._path = 'assets/graphics/Stone/stone.png'
        self._x_pos = 800
        self._y_pos = 315
        self.retangulo = self.get_image().get_rect(midbottom = (randint(900, 1100), self._y_pos))
    
    def __str__(self):
        '''
        Representação do objeto Coin em string.
        '''

        return 'Stone_Object'
    
    def get_image(self):
        '''
        Retorna imagem do obstáculo pedra.
        '''

        return py.image.load(self._path).convert_alpha()
        
    def move_para_esquerda(self, deslocamento):
        '''
        Modifica posição do objeto no eixo X da tela.
        '''

        self.retangulo.x -= deslocamento
    
    def main():
        pass

if __name__ == '__main__':
    Stone().main()