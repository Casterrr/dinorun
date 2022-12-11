import pygame as pg
from texts import fonte_do_jogo
from start_pygame import tela



##screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
##FONT = fonte_do_jogo(50)


class InputBox():
 
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = fonte_do_jogo(50).render(text, False, self.color)
        self.active = False

    ##Coordena os eventos na tela
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                self.txt_surface = fonte_do_jogo(50).render('', True, self.color)
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = fonte_do_jogo(50).render(self.text, True, self.color)

    ## Redimensiona a tela se o nome for muito grande
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    ## Mostra a o texto e o retângulo na tela
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)


## Função principal
def main():
    name_player = InputBox(300, 130, 200, 35, 'PLAYER NAME')
    ##input_box1 = InputBox(100, 100, 140, 32)
    ##input_box2 = InputBox(100, 300, 140, 32)
    input_box = [name_player]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_box:
                box.handle_event(event)
            
        for box in input_box:
            box.update()
        

        for box in input_box:
            box.draw(tela)

        pg.display.flip()
        

main()
 