import pygame as py;
from sys import exit
from random import randint

from functions import *
from Coin import Coin
from Stone import Stone
from Dinosaur import Dinosaur

def cria_objetos(lista_de_objetos):
    '''
    Cria de maneira randômica objetos moedas ou pedra, e os adiciona a uma dada lista.
    '''

    if randint(0,2) == randint(0,2):
        lista_de_objetos.append(Coin())
    else:
        lista_de_objetos.append(Stone())

def main():

    #________________________________________________ DEFINIÇÕES INICIAIS/NECESSÁRIAS DO JOGO ____________________________________________________#
    
    #Inicia biblioteca pygame.
    py.init()

    #Instanciando classe clock, para controle de FPS.
    clock = py.time.Clock()

    #Definições do tamanho da tela do jogo.
    dimensoes = largura, altura = 800, 400
    tela = py.display.set_mode(dimensoes)

    #Definindo legenda do jogo.
    py.display.set_caption('Dinorun')

    #Criando superfícies com texto.
    cabecalho_do_jogo = fonte_do_jogo(50).render("Dinorun", False, '#44b528')

    texto_da_tela_de_incio = fonte_inicio_fim_do_jogo(200).render("Start Playing", False, 'Green')
    texto_instrutivo_iniciar_jogo = fonte_inicio_fim_do_jogo(30).render("- Pressione qualquer tecla para iniciar o jogo -", False, 'Yellow')

    texto_de_fim_de_jogo = fonte_inicio_fim_do_jogo(200).render("Game Over", False, 'Red')
    texto_instrutivo_reiniciar_jogo = fonte_inicio_fim_do_jogo(30).render("- Pressione qualquer tecla para reiniciar o jogo -", False, 'Yellow')
    #_____________________________________________________________________________________________________________________________________________#

    #_______________ DEFININDO PRINCIPAIS VARIÁVEIS DO JOGO _______________#

    dino = Dinosaur()
    lista_de_objetos_no_jogo = list()
    
    background_image = py.image.load('assets/graphics/Blue-Sky.png').convert_alpha()
    ground_image = py.image.load('assets/graphics/Green-Ground.png').convert_alpha()

    conteudo_tela_de_inicio = [(texto_da_tela_de_incio, (185, -20)), (texto_instrutivo_iniciar_jogo, (265, 370))]
    conteudo_tela_de_jogatina = [(background_image, (0, 0)), (ground_image, (0, 300)), (cabecalho_do_jogo, (20, 20)), (dino.get_image(), dino.retangulo)]
    conteudo_tela_de_fim_do_jogo = [(texto_de_fim_de_jogo, (215, -20)), (texto_instrutivo_reiniciar_jogo, (265, 370))]

    #Evento utilizado para criação de objetos do jogo.
    object_timer = py.USEREVENT + 1
    py.time.set_timer(object_timer, 1400)

    #______________________________________________________________________#

    inicia_jogo(tela, conteudo_tela_de_inicio)

    while True:
        active = True
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            
            if event.type == py.KEYDOWN:
                if dino.retangulo.bottom == 310:
                    if event.key == py.K_UP:
                        dino.gravidade_sofrida = -20
            
            if event.type == py.KEYDOWN:
                if colidiu_com_obstaculo(dino.retangulo, lista_de_objetos_no_jogo):
                    lista_de_objetos_no_jogo = reinicia_jogo(lista_de_objetos_no_jogo)
                    #start_offset = py.time.get_ticks()
            
            '''
            Adiciona o obstáculo pedra na lista de obstáculos que serão desenhados na tela após certo período de tempo.
            Esses obstáculos serão desenhados fora da tela, do lado direito, com posição X aleatória.
            '''
            if event.type == object_timer and not colidiu_com_obstaculo(dino.retangulo, lista_de_objetos_no_jogo):
                cria_objetos(lista_de_objetos_no_jogo)

        if not colidiu_com_obstaculo(dino.retangulo, lista_de_objetos_no_jogo):
            exibe_tela_de_jogatina(tela, conteudo_tela_de_jogatina)
        
            #Efeito de pulo do dinossauro na tela.
            dino_jump(dino.retangulo, dino.gravidade_sofrida)
            dino.gravidade_sofrida += 1

            # Obstacle movement
            lista_de_objetos_no_jogo = movimenta_objetos(tela, lista_de_objetos_no_jogo)

            ##Mostra a pontuação
            #score = display_score()

            #Atualiza todos os componentes da tela.
            py.display.flip()

            #Define o FPS (Frames per Second - Quadros por Segundo) do jogo.
            clock.tick(60)
        else:
            active = False
            exibe_tela_de_fim_de_jogo(tela, conteudo_tela_de_fim_do_jogo)
            py.display.flip()



if __name__ == '__main__':
    main()