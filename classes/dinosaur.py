import pygame as py
from random import randint

def main():
    pass

class Dinosaur():
    def __init__(self):
        # O path vai ficar variando entre esses 2 caminhos enquanto o dinossauro estiver no chão.
        self._path = ['./assets/graphics/Dinosaur/dinosaur.png', './assets/graphics/Dinosaur/dinosaur_walk_2.png']
        self._path_index = 0
        self._x_pos = 80
        self._y_pos = 310
        self.is_jumping = False
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

        '''
        Se o dinossauro não está pulando, a imagem do path vai variar aleatoriamente. 
        Mas caso esteja pulando, a imagem do path será fixa
        '''
        if not self.is_jumping:
            random_path = randint(0,1)
            return py.image.load(self._path[random_path]).convert_alpha()
        else:
            return py.image.load(self._path[0]).convert_alpha()

    
    def dino_jump(self):
        '''
        Esta função é responsável pelo efeito de pulo do dinossauro na tela.
        '''

        # Informa que o dinossauro está pulando
        self.is_jumping = True


        self.retangulo.y += self.gravidade_sofrida

        # Faz com que o dinossauro nunca passe do piso
        if self.retangulo.bottom > 310:
            self.retangulo.bottom = 310

            # Avisa que enquanto o dinossauro estiver no piso, ele não está pulando.
            self.is_jumping = False

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