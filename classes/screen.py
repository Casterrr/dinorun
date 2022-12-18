import pygame as py
from classes.start_screen import Start_Screen
from classes.in_game_screen import In_Game_Screen
from classes.game_over_screen import Game_Over_Screen

class Window(Start_Screen, In_Game_Screen, Game_Over_Screen):
    def __init__(self):
        Start_Screen.__init__(self)
        In_Game_Screen.__init__(self)
        Game_Over_Screen.__init__(self)

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))#
        self.caption = py.display.set_caption('Dinorun')

        #self.cabecalho_do_jogo = fonte_principal(50).render("Dinorun", False, '#44b528')
        #self.background_image = py.image.load('./assets/graphics/Blue-Sky.png').convert_alpha()
        #self.ground_image = py.image.load('./assets/graphics/Green-Ground.png').convert_alpha()

        #self.texto_da_tela_de_incio = fonte_tela_inicial_ou_final(200).render("Start Playing", False, 'Green')
        #self.texto_instrutivo_iniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione qualquer tecla para iniciar o jogo -", False, 'Yellow')

        #self.texto_de_fim_de_jogo = fonte_tela_inicial_ou_final(200).render("Game Over", False, 'Red')
        #self.texto_instrutivo_reiniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione qualquer tecla para reiniciar o jogo -", False, 'Yellow')

        #self.conteudo_do_jogo = dict()
        #self.game_clock_variable = None

    """
    def exibe_tela_inicial_de_jogo(self):
        '''
        Inicia o jogo exibindo a primeira tela do jogo.
        Se alguma tecla for precionada, retorna False, interrompendo a exibição da tela.
        '''

        def adiciona_conteudo_tela_de_inicio(self):
            '''
            Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela inicial (anterior à jogatina).
            '''

            conteudo_da_tela = [(self.texto_da_tela_de_incio, (185, -20)), (self.texto_instrutivo_iniciar_jogo, (265, 370))]

            self.screen.fill('#112e0a')

            for objeto in conteudo_da_tela:
                self.screen.blit(objeto[0], objeto[1])
        
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                
                if event.type == py.KEYDOWN:
                    return False
            
            adiciona_conteudo_tela_de_inicio(self)
            py.display.flip()
    """
    """
    def exibe_tela_durante_jogo(self):
        '''
        Exibe tela de jogatina (gameplay).
        Se houver colisão com algum obstáculo que não seja moeda, interrompe a exibição da tela.
        '''

        def adiciona_conteudo_tela_durante_jogo(self):
            '''
            Adiciona imagens/objetos/elementos à tela - tela do jogo durante a jogatina.
            '''

            conteudo_da_tela = [ (self.background_image, (0, 0)), (self.ground_image, (0, 300)), (self.cabecalho_do_jogo, (20, 20)), 
                                (self.conteudo_do_jogo['dinossauro'].get_image(), self.conteudo_do_jogo['dinossauro'].retangulo) ]
            
            for objeto in conteudo_da_tela:
                self.screen.blit(objeto[0], objeto[1])
        
        #Evento utilizado para criação de objetos do jogo.
        object_timer = py.USEREVENT + 1
        py.time.set_timer(object_timer, 1400)

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()

                #Efeito de pulo do dinossauro na tela.
                if event.type == py.KEYDOWN:
                    if self.conteudo_do_jogo['dinossauro'].retangulo.bottom == 310:
                        if event.key == py.K_UP:
                            self.conteudo_do_jogo['dinossauro'].gravidade_sofrida = -20
                
                #Criação de objetos do jogo.
                if event.type == object_timer:
                    self.conteudo_do_jogo['objetos'].append(cria_objetos())
            
            if not colidiu_com_obstaculo(self.conteudo_do_jogo['dinossauro'].retangulo, self.conteudo_do_jogo['objetos']):
                #Efeito de pulo do dinossauro na tela.
                self.conteudo_do_jogo['dinossauro'].dino_jump()
                self.conteudo_do_jogo['dinossauro'].gravidade_sofrida += 1
                
                #Adiciona conteúdo sempre em tela à tela.
                adiciona_conteudo_tela_durante_jogo(self)

                #Movimentação dos objetos do jogo na tela.
                self.conteudo_do_jogo['objetos'] = movimenta_objetos(self.screen, self.conteudo_do_jogo['objetos'])
                
                #Atualiza tela.
                py.display.flip()

                #Define FPS do jogo.
                self.game_clock_variable.tick(60)
            else:
                break
    """
    """
    def exibe_tela_final_de_jogo(self):
        '''
        Exibe tela de game over (após à jogatina).
        Se alguma tecla for precionada, interrompe a exibição da tela.
        '''

        def adiciona_conteudo_tela_final(self):
            '''
            Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela final (após à jogatina).
            '''

            conteudo_da_tela = [ (self.texto_de_fim_de_jogo, (215, -20)), (self.texto_instrutivo_reiniciar_jogo, (265, 370)) ]

            self.screen.fill('#112e0a')

            for objeto in conteudo_da_tela:
                self.screen.blit(objeto[0], objeto[1])

        in_game_over_screen = True

        while in_game_over_screen:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                
                if event.type == py.KEYDOWN:
                    self.restart_game()
                    in_game_over_screen = False
            
            adiciona_conteudo_tela_final(self)
            py.display.flip()
    
    def restart_game(self):
        '''
        Redefine atributos para reiniciar a jogatina.
        '''

        self.conteudo_do_jogo['objetos'] = list()
        self.conteudo_do_jogo['dinossauro'].reset_attributes()
    """
    
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
