import pygame as py

from modules.functions import fonte_principal, fonte_tela_inicial_ou_final

from classes.in_game_screen import In_Game_Screen
from classes.player import Player

class Game_Over_Screen(In_Game_Screen):
    def __init__(self):
        In_Game_Screen.__init__(self)

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.texto_de_fim_de_jogo = fonte_tela_inicial_ou_final(200).render("Game Over", False, 'Red')
        self.texto_instrutivo_reiniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione 'Enter' para reiniciar o jogo -", False, 'Yellow')

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
                        (self.texto_instrutivo_reiniciar_jogo, (290, 370)) ]

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

            #Exibe moldura do top ranking.
            quadro_top_ranking = py.Rect(175, 160, 450, 200)
            py.draw.rect(self.screen, '#44b528', quadro_top_ranking, 2)

            #Adiciona na tela cabeçalho do top ranking.
            texto_high_score = fonte_principal(40).render(f"HIGH SCORES", False, '#44b528')
            retangulo_high_score = texto_high_score.get_rect(center=(quadro_top_ranking.center[0], 190))
            self.screen.blit(texto_high_score, retangulo_high_score)

            #Adiciona na tela a pontuação em primeiro lugar.
            texto_primeiro_lugar = fonte_principal(35).render(f"1st", False, '#44b528')
            self.screen.blit(texto_primeiro_lugar, (190, 235))

            #Adiciona na tela a pontuação em segundo lugar.
            texto_segundo_lugar = fonte_principal(35).render(f"2nd", False, '#44b528')
            self.screen.blit(texto_segundo_lugar, (190, 275))

            #Adiciona na tela a pontuação em terceiro lugar.
            texto_terceiro_lugar = fonte_principal(35).render(f"3rd", False, '#44b528')
            self.screen.blit(texto_terceiro_lugar, (190, 315))

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
            
            self.adiciona_conteudo_tela_final()
            py.display.flip()

    def adiciona_jogador_ao_ranking(self, ranking_file, jogador):
        '''
        Adiciona dados do jogador ao ranking.
        '''

        def valida_insercao_no_ranking(self, ranking_file, jogador):
            '''
            Verifica se o jogador atende aos requisitos para entrar no ranking.
            Retorna True se sim, e False se não.
            '''

            pass

    def get_top_ranking(self, ranking_file):
        '''
        Exibe ranking (Top 5 Pontuações).
        '''

        def get_first_place():
            pass

        def get_second_place():
            pass

        def get_third_place():
            pass

        get_first_place()
        get_second_place()
        get_third_place()

    def restart_game(self):
        '''
        Redefine atributos para reiniciar a jogatina.
        '''

        self.conteudo_do_jogo['objetos'] = list()
        self.conteudo_do_jogo['dinossauro'].reset_attributes()
        self.jogador = Player()
    
    def main():
        pass

if __name__ == '__main__':
    Game_Over_Screen().main()