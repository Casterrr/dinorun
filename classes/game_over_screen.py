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

    def adiciona_conteudo_tela_final(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela final (após à jogatina).
        '''
        
        texto_score_final = fonte_principal(50).render(f"{self.jogador.nome}: {self.jogador.score}", False, 'Green')
        retangulo_texto_score_final = texto_score_final.get_rect()

        #Posição do texto no centro da tela.
        posicao_retangulo_do_texto_score_final = ( int((self._largura - retangulo_texto_score_final.size[0]) / 2), 120)

        conteudo_da_tela = [ (self.texto_de_fim_de_jogo, (215, -20)),
                             (texto_score_final, posicao_retangulo_do_texto_score_final),
                             (self.texto_instrutivo_reiniciar_jogo, (290, 370)) ]

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

    def exibe_ranking(self, ranking_file):
        '''
        Exibe ranking (Top 5 Pontuações).
        '''

        pass

    def exibe_pontuacao_jogador(self):
        '''
        Exibe pontuação final do ultimo jogador.
        '''
        
        pass
    
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