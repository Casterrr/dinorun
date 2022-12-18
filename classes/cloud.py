import pygame as py
from random import randint

class Cloud():
    def __init__(self):
        self._img_path = 'assets/graphics/Cloud/cloud-2.png'
        self._img_path_index = 0
        self._y_pos = [100, 110, 80][randint(0,2)]
        self.retangulo = self.get_image().get_rect(midbottom = (randint(900, 1100), self._y_pos))

    def __str__(self):
        '''
        Representação do objeto Coin em string.
        '''

        return 'Cloud_Object'

    def get_image(self):
        '''
        Retorna imagem do objeto/elemento moeda.
        '''
        return py.image.load(self._img_path)

    def move_para_esquerda(self, deslocamento):
        '''
        Modifica posição do objeto no eixo X da tela.
        '''

        self.retangulo.x -= deslocamento
    
    def main():
        pass
if __name__ == '__main__':
    Cloud().main()