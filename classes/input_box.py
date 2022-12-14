import pygame as py

from modules.functions import fonte_principal

class Input_Box():
    def __init__(self, x, y, largura, altura, texto=''):
        self.largura = largura
        self.retangulo = py.Rect(x, y, largura, altura)
        self.cor = (0,100,0)
        self.texto = texto
        self.superficie_de_texto = fonte_principal(50).render(self.texto, True, "white")
        self.status = False

    def manipulador_de_eventos(self, evento):
        '''
        Manipula eventos de seleção e entrada de dados na caixa de texto.
        '''

        if evento.type == py.MOUSEBUTTONDOWN:
            if self.retangulo.collidepoint(evento.pos):
                self.status = True
            else:
                self.status = False
            self.cor = (0,255,0) if self.status else (0,100,0)

        if evento.type == py.KEYDOWN:
            if self.status:
                if evento.key == py.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                else:
                    if len(self.texto) <= 20:
                        if evento.unicode != " ":
                            self.texto += evento.unicode
                            
                self.superficie_de_texto = fonte_principal(50).render(self.texto, True, "white")

    def desenha_caixa_de_texto_na_tela(self, screen):
        '''
        Adiciona texto digitado à caixa de texto e desenha a caixa de texto na tela.
        '''

        #O centro do retangulo está localizado no centro da input box.
        retangulo_do_texto = self.superficie_de_texto.get_rect(center=(self.retangulo.center))

        #Adiciona superfície com texto à tela, na posição da variável retangulo_do_texto.
        screen.blit(self.superficie_de_texto, retangulo_do_texto)

        #Desenha retângulo da caixa de texto (input box) à tela.
        py.draw.rect(screen, self.cor, self.retangulo, 2)
    
    def main():
        pass

if __name__ == '__main__':
    Input_Box().main()