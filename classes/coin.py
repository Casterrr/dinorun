import pygame as py
from random import randint

def main():
    pass

class Coin():
    def __init__(self):
        self._img_path = ['assets/graphics/Coin/semi-borderless-coin.png', 'assets/graphics/Coin/coin-flip.png', 'assets/graphics/Coin/coin-flip-2.png']
        self._img_path_index = 0
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
        # Toda vez que essa função get_image for chamada, a variável _img_path_index vai ser acrescentada de 0.1
        self._img_path_index += 0.1
        # random_img_path = randint(0,10)
        
        # if random_img_path in [0,1,2]:

        # Altera a imagem exibida de acordo com a parte inteira da variável _img_path_index
        if int(self._img_path_index) == 1:
            return py.image.load(self._img_path[0]).convert_alpha()
        elif int(self._img_path_index) == 2:
            return py.image.load(self._img_path[1]).convert_alpha()
        elif int(self._img_path_index) == 3:
            if self._img_path_index >= 3.9:
                self._img_path_index = 0
            return py.image.load(self._img_path[2]).convert_alpha()
        else:
            return py.image.load(self._img_path[0])

    def move_para_esquerda(self, deslocamento):
        '''
        Modifica posição do objeto no eixo X da tela.
        '''

        self.retangulo.x -= deslocamento
 
if __name__ == '__main__':
    main()