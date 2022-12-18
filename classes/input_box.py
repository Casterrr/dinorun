import pygame as py

from modules.functions import fonte_principal

class Input_Box():
    def __init__(self, x, y, largura, altura, texto=''):
        self.retangulo = py.Rect(x, y, largura, altura)
        self.cor = (0,100,0)
        self.texto = texto
        self.superficie_de_texto = fonte_principal(50).render(self.texto, True, (0,0,0))
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
                        self.texto += evento.unicode
                self.superficie_de_texto = fonte_principal(50).render(self.texto, True, (0,0,0))

    def atualiza_dimensoes(self):
        '''
        Atualiza dimensões da caixa de texto se o texto for muito longo.
        '''

        width = max(500, self.superficie_de_texto.get_width()+10)
        self.retangulo.w = width

    def desenha_caixa_de_texto_na_tela(self, screen):
        '''
        Adiciona texto digitado à caixa de texto e desenha a caixa de texto na tela.
        '''

        #Adiciona superfície com texto à tela.
        screen.blit(self.superficie_de_texto, (self.retangulo.x+70, self.retangulo.y+10))

        #Desenha retângulo da caixa de texto (input box) à tela.
        py.draw.rect(screen, self.cor, self.retangulo, 2)
    
    def main():
        pass

if __name__ == '__main__':
    Input_Box().main()