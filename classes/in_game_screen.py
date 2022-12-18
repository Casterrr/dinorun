import pygame as py
from functions import fonte_principal, cria_objetos, movimenta_objetos,colidiu_com_obstaculo

class In_Game_Screen():
    def __init__(self):
        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.cabecalho_do_jogo = fonte_principal(50).render("Dinorun", False, '#44b528')
        self.background_image = py.image.load('./assets/graphics/Blue-Clean-Sky.png').convert_alpha()
        self.ground_image = py.image.load('./assets/graphics/Green-Ground.png').convert_alpha()
        
        self.conteudo_do_jogo = dict()
        self.game_clock_variable = None
    
    def adiciona_conteudo_tela_durante_jogo(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a jogatina.
        '''

        conteudo_da_tela = [ (self.background_image, (0, 0)), (self.ground_image, (0, 300)), (self.cabecalho_do_jogo, (20, 20)), 
                            (self.conteudo_do_jogo['dinossauro'].get_image(), self.conteudo_do_jogo['dinossauro'].retangulo) ]
        
        for objeto in conteudo_da_tela:
            self.screen.blit(objeto[0], objeto[1])

    def exibe_tela_durante_jogo(self):
        '''
        Exibe tela de jogatina (gameplay).
        Se houver colisão com algum obstáculo que não seja moeda, interrompe a exibição da tela.
        '''
        
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
                            self.conteudo_do_jogo['dinossauro'].gravidade_sofrida = -18
                
                #Criação de objetos do jogo.
                if event.type == object_timer:
                    self.conteudo_do_jogo['objetos'].append(cria_objetos())
            
            if not colidiu_com_obstaculo(self.conteudo_do_jogo['dinossauro'].retangulo, self.conteudo_do_jogo['objetos']):
                #Efeito de pulo do dinossauro na tela.
                self.conteudo_do_jogo['dinossauro'].dino_jump()
                self.conteudo_do_jogo['dinossauro'].gravidade_sofrida += 1
                
                #Adiciona conteúdo sempre em tela à tela.
                self.adiciona_conteudo_tela_durante_jogo()

                #Movimentação dos objetos do jogo na tela.
                self.conteudo_do_jogo['objetos'] = movimenta_objetos(self.screen, self.conteudo_do_jogo['objetos'])
                
                #Atualiza tela.
                py.display.flip()

                #Define FPS do jogo.
                self.game_clock_variable.tick(60)
            else:
                break
    
    def restart_game(self):
        '''
        Redefine atributos para reiniciar a jogatina.
        '''

        self.conteudo_do_jogo['objetos'] = list()
        self.conteudo_do_jogo['dinossauro'].reset_attributes()

    def main():
        pass

if __name__ == '__main__':
    In_Game_Screen().main()
