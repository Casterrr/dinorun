import pygame as py

from modules.functions import fonte_principal, fonte_tela_inicial_ou_final, valida_requisitos_para_insercao_no_ranking, insere_jogador_no_ranking

from classes.in_game_screen import In_Game_Screen
from classes.player import Player
from classes.ranking import Ranking

class Game_Over_Screen(In_Game_Screen):
    def __init__(self):
        In_Game_Screen.__init__(self)

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.texto_de_fim_de_jogo = fonte_tela_inicial_ou_final(200).render("Game Over", False, 'Red')
        self.texto_instrutivo_reiniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione 'Enter' para reiniciar o jogo -", False, 'Yellow')

        self._database_path = "modules/database.db"
        self.ranking = Ranking(self._database_path)
        self.game_over_sound = py.mixer.Sound('./assets/sounds/game-over.mp3')

    def atualiza_ranking(self):
        '''
        Atualiza ranking.
        '''

        colocacao_no_ranking = valida_requisitos_para_insercao_no_ranking(self.ranking, self.jogador)

        if colocacao_no_ranking:
            insere_jogador_no_ranking(self.ranking, self.jogador, colocacao_no_ranking)

    def adiciona_top_ranking(self):
        '''
        Adiciona estrutura do top ranking (3 maiores pontuações) na tela.
        '''

        #Exibe moldura do top ranking.
        quadro_top_ranking = py.Rect(145, 160, 510, 200)
        py.draw.rect(self.screen, '#44b528', quadro_top_ranking, 2)

        #Adiciona na tela cabeçalho do top ranking.
        texto_high_score = fonte_principal(40).render(f"HIGH SCORES", False, '#44b528')
        retangulo_high_score = texto_high_score.get_rect(center=(quadro_top_ranking.center[0], 190))
        self.screen.blit(texto_high_score, retangulo_high_score)

        #Adiciona na tela o título de colocação (primeiro lugar).
        texto_primeiro_lugar = fonte_principal(35).render(f"1st", False, '#44b528')
        retangulo_texto_primeiro_lugar = texto_primeiro_lugar.get_rect(topleft=(quadro_top_ranking.left+75, 235))
        self.screen.blit(texto_primeiro_lugar, retangulo_texto_primeiro_lugar)

        #Adiciona na tela o título de colocação em (segundo lugar).
        texto_segundo_lugar = fonte_principal(35).render(f"2nd", False, '#44b528')
        retangulo_texto_segundo_lugar = texto_segundo_lugar.get_rect(topleft=(quadro_top_ranking.left+75, 275))
        self.screen.blit(texto_segundo_lugar, retangulo_texto_segundo_lugar)

        #Adiciona na tela o título de colocação (terceiro lugar).
        texto_terceiro_lugar = fonte_principal(35).render(f"3rd", False, '#44b528')
        retangulo_texto_terceiro_lugar = texto_terceiro_lugar.get_rect(topleft=(quadro_top_ranking.left+75, 315))
        self.screen.blit(texto_terceiro_lugar, retangulo_texto_terceiro_lugar)

        #Adiciona dados do primeiro colocado no top ranking.
        if not self.ranking.primeiro_lugar:
            texto_sem_jogador = fonte_principal(35).render(f"- - - - - - - - - - -", False, '#44b528')
            retangulo_texto_sem_jogador = texto_sem_jogador.get_rect(center=(quadro_top_ranking.center[0], 245))
            self.screen.blit(texto_sem_jogador, retangulo_texto_sem_jogador)

            texto_score_jogador = fonte_principal(35).render(f"- - - -", False, '#44b528')
            retangulo_texto_score_jogador = texto_score_jogador.get_rect(topright=(quadro_top_ranking.right-15, retangulo_texto_sem_jogador.top))
            self.screen.blit(texto_score_jogador, retangulo_texto_score_jogador)

        else:
            texto_nome_do_jogador = fonte_principal(35).render(f"{self.ranking.primeiro_lugar.nome}", False, '#44b528')
            retangulo_texto_nome_do_jogador = texto_nome_do_jogador.get_rect(center=(quadro_top_ranking.center[0], 245))
            self.screen.blit(texto_nome_do_jogador, retangulo_texto_nome_do_jogador)

            texto_score_jogador = fonte_principal(35).render(f"{self.ranking.primeiro_lugar.score}", False, '#44b528')
            retangulo_texto_score_jogador = texto_score_jogador.get_rect(topright=(quadro_top_ranking.right-15, retangulo_texto_nome_do_jogador.top))
            self.screen.blit(texto_score_jogador, retangulo_texto_score_jogador)

        #Adiciona dados do segundo colocado no top ranking.
        if not self.ranking.segundo_lugar:
            texto_sem_jogador = fonte_principal(35).render(f"- - - - - - - - - - -", False, '#44b528')
            retangulo_texto_sem_jogador = texto_sem_jogador.get_rect(center=(quadro_top_ranking.center[0], 285))
            self.screen.blit(texto_sem_jogador, retangulo_texto_sem_jogador)

            texto_score_jogador = fonte_principal(35).render(f"- - - -", False, '#44b528')
            retangulo_texto_score_jogador = texto_score_jogador.get_rect(topright=(quadro_top_ranking.right-15, retangulo_texto_sem_jogador.top))
            self.screen.blit(texto_score_jogador, retangulo_texto_score_jogador)

        else:
            texto_nome_do_jogador = fonte_principal(35).render(f"{self.ranking.segundo_lugar.nome}", False, '#44b528')
            retangulo_texto_nome_do_jogador = texto_nome_do_jogador.get_rect(center=(quadro_top_ranking.center[0], 285))
            self.screen.blit(texto_nome_do_jogador, retangulo_texto_nome_do_jogador)

            texto_score_jogador = fonte_principal(35).render(f"{self.ranking.segundo_lugar.score}", False, '#44b528')
            retangulo_texto_score_jogador = texto_score_jogador.get_rect(topright=(quadro_top_ranking.right-15, retangulo_texto_nome_do_jogador.top))
            self.screen.blit(texto_score_jogador, retangulo_texto_score_jogador)

        #Adiciona dados do terceiro colocado no top ranking.
        if not self.ranking.terceiro_lugar:
            texto_sem_jogador = fonte_principal(35).render(f"- - - - - - - - - - -", False, '#44b528')
            retangulo_texto_sem_jogador = texto_sem_jogador.get_rect(center=(quadro_top_ranking.center[0], 325))
            self.screen.blit(texto_sem_jogador, retangulo_texto_sem_jogador)

            texto_score_jogador = fonte_principal(35).render(f"- - - -", False, '#44b528')
            retangulo_texto_score_jogador = texto_score_jogador.get_rect(topright=(quadro_top_ranking.right-15, retangulo_texto_sem_jogador.top))
            self.screen.blit(texto_score_jogador, retangulo_texto_score_jogador)

        else:
            texto_nome_do_jogador = fonte_principal(35).render(f"{self.ranking.terceiro_lugar.nome}", False, '#44b528')
            retangulo_texto_nome_do_jogador = texto_nome_do_jogador.get_rect(center=(quadro_top_ranking.center[0], 325))
            self.screen.blit(texto_nome_do_jogador, retangulo_texto_nome_do_jogador)

            texto_score_jogador = fonte_principal(35).render(f"{self.ranking.terceiro_lugar.score}", False, '#44b528')
            retangulo_texto_score_jogador = texto_score_jogador.get_rect(topright=(quadro_top_ranking.right-15, retangulo_texto_nome_do_jogador.top))
            self.screen.blit(texto_score_jogador, retangulo_texto_score_jogador)

    def adiciona_conteudo_tela_final(self):
        '''
        Cria e adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela final (após à jogatina).
        '''

        #________________ Adiciona conteúdo fixo na tela. ________________#

        conteudo = [ (self.texto_de_fim_de_jogo, (215, -20)),
                    (self.texto_instrutivo_reiniciar_jogo, (290, 370)) ]

        self.screen.fill('#112e0a')

        for objeto in conteudo:
            self.screen.blit(objeto[0], objeto[1])
        

        #_______________ Adiciona conteúdo dinâmico na tela _______________#

        #Adiciona na tela score final do ultimo jogador.
        pontuacao = fonte_principal(50).render(f"{self.jogador.nome}: {self.jogador.score}", False, 'Orange')
        self.screen.blit(pontuacao, pontuacao.get_rect(center=(self._largura/2, 120)))

        self.adiciona_top_ranking()
        
    def exibe_tela_final_de_jogo(self):
        '''
        Exibe tela de game over (após à jogatina).
        Se alguma tecla for precionada, interrompe a exibição da tela.
        '''
        
        self.game_over_sound.play()
        in_game_over_screen = True

        self.atualiza_ranking()

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