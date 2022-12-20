import pygame as py

from modules.functions import fonte_principal, cria_objetos, movimenta_objetos

from classes.start_screen import Start_Screen
from classes.player import Player

class In_Game_Screen(Start_Screen):
    def __init__(self):
        Start_Screen.__init__(self)

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.cabecalho_do_jogo = fonte_principal(50).render("Dinorun", False, '#44b528')
        self.background_image = py.image.load('./assets/graphics/Blue-Clean-Sky.png').convert_alpha()
        self.ground_image = py.image.load('./assets/graphics/Green-Ground.png').convert_alpha()

        self.momento_de_inicio_do_jogo = int()
        self.momento_em_tempo_real_do_jogo = int()

        self.pontuacao_por_tempo = (self.momento_em_tempo_real_do_jogo - self.momento_de_inicio_do_jogo) / 100
        self.pontuacao_bonus = int()
        
        self.score = int()
        self.texto_score = fonte_principal(35).render(f"Score: {str(self.score)}", False, 'Black')

        self.conteudo_do_jogo = dict()
        self.game_clock_variable = None

        self.in_game_sound = py.mixer.Sound('./assets/sounds/in-game-sound.mp3')
    
    def adiciona_conteudo_tela_durante_jogo(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a jogatina.
        '''

        conteudo_da_tela = [ (self.background_image, (0, 0)), 
                             (self.ground_image, (0, 300)), 
                             (self.cabecalho_do_jogo, (20, 20)), 
                             (self.conteudo_do_jogo['dinossauro'].get_image(), self.conteudo_do_jogo['dinossauro'].retangulo),
                             (self.texto_score, (355, 20)) ]
        
        for objeto in conteudo_da_tela:
            self.screen.blit(objeto[0], objeto[1])

    def exibe_tela_durante_jogo(self):
        '''
        Exibe tela de jogatina (gameplay).
        Se houver colisão com algum obstáculo que não seja moeda, interrompe a exibição da tela.
        '''

        self.in_game_sound.play(loops=-1, fade_ms=1000)
        
        #Evento utilizado para criação de objetos do jogo.
        object_timer = py.USEREVENT + 1
        py.time.set_timer(object_timer, 1400)

        self.momento_de_inicio_do_jogo = int(py.time.get_ticks())

        while True:
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()

                #Efeito de pulo do dinossauro na tela.
                if event.type == py.KEYDOWN:
                    if self.conteudo_do_jogo['dinossauro'].retangulo.bottom == 310:
                        if event.key == py.K_UP:
                            self.conteudo_do_jogo['dinossauro'].jump_sound.play()
                            self.conteudo_do_jogo['dinossauro'].gravidade_sofrida = -18
                
                #Criação de objetos do jogo.
                if event.type == object_timer:
                    self.conteudo_do_jogo['objetos'].append(cria_objetos())
            
            if not self.colidiu_com_objeto():

                #Efeito de pulo do dinossauro na tela.
                self.conteudo_do_jogo['dinossauro'].dino_jump()
                self.conteudo_do_jogo['dinossauro'].gravidade_sofrida += 1
                
                #Adiciona conteúdo sempre em tela à tela.
                self.adiciona_conteudo_tela_durante_jogo()

                #Movimentação dos objetos do jogo na tela.
                self.conteudo_do_jogo['objetos'] = movimenta_objetos(self.screen, self.conteudo_do_jogo['objetos'])
                
                #Atualiza tela.
                py.display.flip()

                #Atualiza score.
                self.atualiza_score()

                #Define FPS do jogo.
                self.game_clock_variable.tick(60)
            else:
                self.jogador.score = self.score
                break

    def colidiu_com_objeto(self):
        '''
        Trata colisões do objeto dinossauro com os objetos moeda ou objetos pedra.
        '''
        
        if self.conteudo_do_jogo['objetos']:
            for objeto in self.conteudo_do_jogo['objetos']:
                if self.conteudo_do_jogo['dinossauro'].retangulo.colliderect(objeto.retangulo):

                    if objeto.__str__() == 'Stone_Object':
                        self.in_game_sound.fadeout(500)
                        return True

                    elif objeto.__str__() == 'Coin_Object':
                        self.conteudo_do_jogo['objetos'].remove(objeto)
                        objeto.coin_sound.play()
                        self.pontuacao_bonus += 10
                        return False
            else:
                return False

    def atualiza_score(self):
        '''
        Atualiza variáveis do score.
        '''

        def atualiza_pontuacao_por_tempo():
            '''
            Atualiza variável de pontuação por tempo.
            '''

            self.momento_em_tempo_real_do_jogo = py.time.get_ticks()
            self.pontuacao_por_tempo = (self.momento_em_tempo_real_do_jogo - self.momento_de_inicio_do_jogo) / 100

        atualiza_pontuacao_por_tempo()
        self.score = int(self.pontuacao_por_tempo + self.pontuacao_bonus)
        self.texto_score = fonte_principal(35).render(f"Score: {str(self.score)}", False, 'Black')

    def main():
        pass

if __name__ == '__main__':
    In_Game_Screen().main()
