import pygame as py

def main():
    pass

class Dinosaur():
    def __init__(self):
        self._path = 'assets/graphics/Dinosaur/dinosaur.png'
        self._x_pos = 80
        self._y_pos = 310

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

if __name__ == '__main__':
    main()