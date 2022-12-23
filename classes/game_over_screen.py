import pygame as py

from modules.functions import fonte_principal, fonte_tela_inicial_ou_final

from classes.in_game_screen import In_Game_Screen
from classes.start_screen import Start_Screen

class Game_Over_Screen(In_Game_Screen):
    def __init__(self):
        In_Game_Screen.__init__(self)

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.texto_de_fim_de_jogo = fonte_tela_inicial_ou_final(200).render("Game Over", False, 'Red')
        self.texto_instrutivo_reiniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione 'Enter' para reiniciar o jogo ", False, 'Yellow')
        self.texto_instrutivo_tela_inicial = fonte_tela_inicial_ou_final(30).render(" Ou 'Espaco' para volta a tela inicial -", False, 'Yellow')

        self.game_over_sound = py.mixer.Sound('./assets/sounds/game-over.mp3')

    def adiciona_conteudo_tela_final(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela final (após à jogatina).
        '''

        def adiciona_conteudo_estatico():
            '''
            Adiciona conteúdo da tela de game over que nunca é alterado (possui sempre os mesmos valores).
            '''

            conteudo = [ (self.texto_de_fim_de_jogo, (215, -20)),
                        (self.texto_instrutivo_reiniciar_jogo, (290, 360)), 
                        (self.texto_instrutivo_tela_inicial, (300, 375))]

            self.screen.fill('#112e0a')

            for objeto in conteudo:
                self.screen.blit(objeto[0], objeto[1])

        def adiciona_conteudo_dinamico():
            '''
            Adiciona conteúdo da tela de game over que é alterado (possui seus valores passíveis de alteração).
            '''

            #Adiciona na tela score final do ultimo jogador.
            pontuacao = fonte_principal(50).render(f"{self.jogador.nome}: {self.jogador.score}", False, 'Orange')
            self.screen.blit(pontuacao, pontuacao.get_rect(center=(self._largura/2, 120)))

        adiciona_conteudo_estatico()
        adiciona_conteudo_dinamico()
        
    def exibe_tela_final_de_jogo(self):
        '''
        Exibe tela de game over (após à jogatina).
        Se alguma tecla for precionada, interrompe a exibição da tela.
        '''
        
        self.game_over_sound.play()
        in_game_over_screen = True

        while in_game_over_screen:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                
                if event.type == py.KEYDOWN:
                    if event.key == py.K_KP_ENTER or event.key == py.K_RETURN:
                        self.restart_game()
                        in_game_over_screen = False
                    if event.key == py.K_SPACE:
                        self.exibe_tela_inicial_de_jogo()
                        in_game_over_screen = False
                        self.restart_game()
             
            self.adiciona_conteudo_tela_final()
            py.display.flip()

    def restart_game(self):
        '''
        Redefine atributos para reiniciar a jogatina.
        '''

        self.conteudo_do_jogo['objetos'] = list()
        self.conteudo_do_jogo['dinossauro'].reset_attributes()
        
    
    def main():
        pass

if __name__ == '__main__':
    Game_Over_Screen().main()