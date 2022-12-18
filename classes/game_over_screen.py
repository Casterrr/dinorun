import pygame as py
from functions import fonte_tela_inicial_ou_final

class Game_Over_Screen():
    def __init__(self):
        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.texto_de_fim_de_jogo = fonte_tela_inicial_ou_final(200).render("Game Over", False, 'Red')
        self.texto_instrutivo_reiniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione qualquer tecla para reiniciar o jogo -", False, 'Yellow')

    def adiciona_conteudo_tela_final(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela final (após à jogatina).
        '''

        conteudo_da_tela = [ (self.texto_de_fim_de_jogo, (215, -20)), (self.texto_instrutivo_reiniciar_jogo, (265, 370)) ]

        self.screen.fill('#112e0a')

        for objeto in conteudo_da_tela:
            self.screen.blit(objeto[0], objeto[1])
    
    def exibe_tela_final_de_jogo(self):
        '''
        Exibe tela de game over (após à jogatina).
        Se alguma tecla for precionada, interrompe a exibição da tela.
        '''
        in_game_over_screen = True

        while in_game_over_screen:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                
                if event.type == py.KEYDOWN:
                    self.restart_game()
                    in_game_over_screen = False
            
            self.adiciona_conteudo_tela_final()
            py.display.flip()

    def main():
        pass

if __name__ == '__main__':
    Game_Over_Screen().main()