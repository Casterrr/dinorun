import pygame as py

from classes.in_game_screen import In_Game_Screen
from classes.game_over_screen import Game_Over_Screen

class Window(Game_Over_Screen):
    def __init__(self):
        Game_Over_Screen.__init__(self)

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))
        self.caption = py.display.set_caption('Dinorun')
    
    def set_conteudo_do_jogo(self, conteudo):
        '''
        Define coleção de dados (espera-se um dicionário) com os objetos a serem exibidos na tela.
        '''

        self.conteudo_do_jogo = conteudo
    
    def set_clock_game_variable(self, clock_variable):
        '''
        Define variável reguladora do FPS do jogo.
        '''

        self.game_clock_variable = clock_variable

    def main():
        pass

if __name__ == '__main__':
    Window.main()
