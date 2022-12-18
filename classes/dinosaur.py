import pygame as py
from random import randint

def main():
    pass

class Dinosaur():
    def __init__(self):
        self._path = './assets/graphics/Dinosaur/dinosaur.png'
        self._x_pos = 80
        self._y_pos = 310
        self.retangulo = self.get_image().get_rect(midbottom = (80, 310))
        self.gravidade_sofrida = 0

    def __str__(self):
        '''
        Representação do objeto Dinossauro em string.
        '''

        return 'Dinosaur_Object'

    def get_image(self):
        '''
        Retorna imagem do objeto/elemento dinossauro.
        '''
        
        return py.image.load(self._path).convert_alpha()
    
    def dino_jump(self):
        '''
        Esta função é responsável pelo efeito de pulo do dinossauro na tela.
        '''

        self.retangulo.y += self.gravidade_sofrida

        if self.retangulo.bottom > 310:
            self.retangulo.bottom = 310

    def reset_attributes(self):
        '''
        Redefine atributos para seus valores padrão.
        '''

        self._x_pos = 80
        self._y_pos = 310
        self.retangulo = self.get_image().get_rect(midbottom = (80, 310))
        self.gravidade_sofrida = 0

if __name__ == '__main__':
    main()