import pygame as py;

#Declarando variável com tipo de fonte do jogo.
def fonte_do_jogo(tamanho_da_fonte):
    return py.font.Font("assets/fonts/PixelType.ttf", tamanho_da_fonte)

def fonte_inicio_fim_do_jogo(tamanho_da_fonte):
    return py.font.Font("assets/fonts/game_over.ttf", tamanho_da_fonte)

#Criando superfícies com texto.
cabecalho_do_jogo = fonte_do_jogo(50).render("Dinorun", False, '#44b528')

texto_da_tela_de_incio = fonte_inicio_fim_do_jogo(200).render("Start Playing", False, 'Green')
texto_instrutivo_iniciar_jogo = fonte_inicio_fim_do_jogo(30).render("- Pressione qualquer tecla para iniciar o jogo -", False, 'Yellow')

texto_de_fim_de_jogo = fonte_inicio_fim_do_jogo(200).render("Game Over", False, 'Red')
texto_instrutivo_reiniciar_jogo = fonte_inicio_fim_do_jogo(30).render("- Pressione qualquer tecla para reiniciar o jogo -", False, 'Yellow')