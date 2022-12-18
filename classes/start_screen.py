import pygame as py
from functions import fonte_tela_inicial_ou_final

class Start_Screen():
    def __init__(self):
        self._largura = 800
        self._altura = 400

        self.screen = py.display.set_mode((self._largura, self._altura))

        self.texto_da_tela_de_incio = fonte_tela_inicial_ou_final(200).render("Start Playing", False, 'Green')
        self.texto_instrutivo_iniciar_jogo = fonte_tela_inicial_ou_final(30).render("- Pressione qualquer tecla para iniciar o jogo -", False, 'Yellow')

    def adiciona_conteudo_tela_de_inicio(self):
        '''
        Adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela inicial (anterior à jogatina).
        '''

        conteudo_da_tela = [(self.texto_da_tela_de_incio, (185, -20)), (self.texto_instrutivo_iniciar_jogo, (265, 370))]

        self.display_score(True)
        self.screen.fill('#112e0a')

        for objeto in conteudo_da_tela:
            self.screen.blit(objeto[0], objeto[1])
    
    def exibe_tela_inicial_de_jogo(self):
        '''
        Inicia o jogo exibindo a primeira tela do jogo.
        Se alguma tecla for pressionada, retorna False, interrompendo a exibição da tela.
        '''

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                
                if event.type == py.KEYDOWN:
                    return False
            
            self.adiciona_conteudo_tela_de_inicio()
            
            py.display.flip()

    def main():
        pass

if __name__ == '__main__':
    Start_Screen().main()