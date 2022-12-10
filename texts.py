import pygame as py;

#Declarando variável com tipo de fonte do jogo.
def fonte_do_jogo(tamanho_da_fonte):
    return py.font.Font("assets/fonts/PixelType.ttf", tamanho_da_fonte)

def fonte_inicio_fim_do_jogo(tamanho_da_fonte):
    return py.font.Font("assets/fonts/game_over.ttf", tamanho_da_fonte)

    
fonte_fim_do_jogo = py.font.Font("assets/fonts/game_over.ttf", 200)

#Criando superfícies com texto.
cabecalho_do_jogo = fonte_do_jogo(50).render("Dinorun", False, '#44b528')

initial_game_screen_text = fonte_inicio_fim_do_jogo(200).render("Start Playing", False, 'Green')
start_text = fonte_inicio_fim_do_jogo(30).render("- Pressione qualquer tecla para iniciar o jogo -", False, 'Yellow')

game_over_text = fonte_fim_do_jogo.render("Game Over", False, 'Red')
restart_text = fonte_do_jogo(30).render("- Pressione qualquer tecla para reiniciar o jogo -", False, 'Yellow')