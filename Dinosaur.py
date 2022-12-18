import pygame as py
from random import randint

def main():
    pass

class Dinosaur():
    def __init__(self):
        dinosaur_walk_1 = 'assets/graphics/Dinosaur/dinosaur.png'
        dinosaur_walk_2 = 'assets/graphics/Dinosaur/dinosaur_walk_2.png'
        self._path = [dinosaur_walk_1, dinosaur_walk_2]
        self.path_index = 0
        self._x_pos = 80
        self._y_pos = 310
        self.retangulo = self.get_image().get_rect(midbottom = (80, 310))
        self.gravidade_sofrida = 0

    def __str__(self):
        '''
        Representação do objeto Dinossauro em string.
        '''

        return 'Dinosaur_Object'
    
    # def dino_animation(self):
        
    #     if self.retangulo.bottom < 300:
    #         self._path = self._path[1]
    #     else:
    #         self.path_index += 0.1
    #         print(self.path_index)
    #         if self.path_index >= len(self._path):self.path_index = 0


    def get_image(self):
        '''
        Retorna imagem do objeto/elemento dinossauro.
        '''
        # pegar um valor aleatório entre 0 e 1 para definir o path da imagem dinamicamente
        randomPath = self._path[randint(0,1)]
        # print(randomPath)
        return py.image.load(randomPath).convert_alpha()


    # def update(self):
    #     # self.dino_animation()
    #     self.retangulo = self.get_image().get_rect(midbottom = (80, 310))

if __name__ == '__main__':
    main()