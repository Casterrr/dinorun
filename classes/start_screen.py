import pygame as py

from modules.functions import fonte_tela_inicial_ou_final

from classes.input_box import Input_Box
from classes.player import Player

class Start_Screen():
    def __init__(self):

        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.background_inicial_image = py.image.load('./assets/graphics/Tela-Inicial.jpg').convert_alpha()
        ##self.texto_da_tela_de_incio = fonte_tela_inicial_ou_final(200).render("Start Playing", False, 'Green')
        self.texto_instrutivo_iniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione 'Enter' para iniciar o jogo -", False, 'Yellow')
        self.texto_input_box = fonte_tela_inicial_ou_final(100).render("Player name:", False, 'Green')

        self.input_box_nome_do_jogador = Input_Box(150, 235, 500, 50)
        self.jogador = Player()

        self.intro_sound = py.mixer.Sound('./assets/sounds/intro.mp3')

    def adiciona_conteudo_tela_de_inicio(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela inicial (anterior à jogatina).
        '''

        conteudo_da_tela = [ (self.background_inicial_image, (0, 0)), 
                             (self.texto_input_box, (290, 170)), 
                             (self.texto_instrutivo_iniciar_jogo, 
                             (295, 370)) ]

        ##self.screen.fill('#112e0a')

        for objeto in conteudo_da_tela:
            self.screen.blit(objeto[0], objeto[1])
        
        self.input_box_nome_do_jogador.desenha_caixa_de_texto_na_tela(self.screen)
    
    def exibe_tela_inicial_de_jogo(self):
        '''
        Inicia o jogo exibindo a primeira tela do jogo.
        Se a tecla enter for precionada, retorna texto da input box (nome do jogador), interrompendo a exibição da tela.
        Se nenhum nome for digitado pelo usuário, retorna o texto 'Jogador Anônimo'.
        '''

        self.intro_sound.play(fade_ms=1000)

        in_start_game_screen = True

        while in_start_game_screen:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()

                if event.type == py.KEYDOWN:
                    if event.key == py.K_KP_ENTER or event.key == py.K_RETURN:
                        
                        self.intro_sound.stop()

                        if self.input_box_nome_do_jogador.texto == '':
                            self.jogador.nome = 'Anonimo'
                            in_start_game_screen = False
                        else:
                            self.jogador.nome = self.input_box_nome_do_jogador.texto
                            in_start_game_screen = False
                
                self.input_box_nome_do_jogador.manipulador_de_eventos(event)
                
            self.input_box_nome_do_jogador.desenha_caixa_de_texto_na_tela(self.screen)
            self.adiciona_conteudo_tela_de_inicio()

            py.display.flip()

    def main():
        pass

if __name__ == '__main__':
    Start_Screen().main()