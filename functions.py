import pygame as py

def main():
    pass

def fonte_principal(tamanho_da_fonte):
    '''
    Retorna a fonte principal do jogo, com tamanho determinado pelo usuário.
    '''

    return py.font.Font("assets/fonts/PixelType.ttf", tamanho_da_fonte)

def fonte_tela_inicial_ou_final(tamanho_da_fonte):
    '''
    Retorna a fonte utilizada nas telas de incio e fim de jogo, com tamanho determinado pelo usuário.
    '''

    return py.font.Font("assets/fonts/game_over.ttf", tamanho_da_fonte)

def inicia_jogo(janela_principal_do_jogo, conteudo_da_tela):
    '''
    Inicia o jogo exibindo a primeira tela do jogo.
    '''
    
    while True:
        game_started = False

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            
            if event.type == py.KEYDOWN:
                game_started = True
        
        exibe_tela_incial(janela_principal_do_jogo, conteudo_da_tela)
        py.display.flip()

        if game_started:
            break

def exibe_tela_incial(janela_do_jogo, conteudo_da_tela):
    '''
    Exibe - adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela inicial (anterior à jogatina).
    Recebe como argumento a tela em que deve exibir as imagens/objetos e uma lista contendo as imagens/objetos a serem exibidos.
    Essa lista deve conter tuplas, onde o primeiro elemento da tupla é a imagem/objeto, e o segundo é sua respectiva posição na tela.
    '''

    janela_do_jogo.fill('#112e0a')

    for elemento in conteudo_da_tela:
        janela_do_jogo.blit(elemento[0], elemento[1])

def exibe_tela_de_jogatina(janela_do_jogo, conteudo_da_tela):
    '''
    Exibe - adiciona imagens/objetos/elementos à tela - tela do jogo durante a jogatina.
    Recebe como argumento a tela em que deve exibir as imagens/objetos e uma lista contendo as imagens/objetos a serem exibidos.
    Essa lista deve conter tuplas, onde o primeiro elemento da tupla é a imagem/objeto, e o segundo é sua respectiva posição na tela.
    '''

    for elemento in conteudo_da_tela:
        janela_do_jogo.blit(elemento[0], elemento[1])

def exibe_tela_de_fim_de_jogo(janela_do_jogo, conteudo_da_tela):
    '''
    Exibe - adiciona imagens/objetos/elementos à tela - tela do jogo durante a tela final (após à jogatina).
    Recebe como argumento a tela em que deve exibir as imagens/objetos e uma lista contendo as imagens/objetos a serem exibidos.
    Essa lista deve conter tuplas, onde o primeiro elemento da tupla é a imagem/objeto, e o segundo é sua respectiva posição na tela.
    '''

    janela_do_jogo.fill('#112e0a')
    
    for elemento in conteudo_da_tela:
        janela_do_jogo.blit(elemento[0], elemento[1])

def movimenta_objetos(janela_do_jogo, lista_de_objetos):
    '''
    Move objetos de uma dada lista na em uma dada tela do jogo.
    Ao final, retorna a lista sem os objetos que estão fora da tela.
    '''
    
    if lista_de_objetos:
        for objeto in lista_de_objetos:

            if objeto.__str__() == "Coin_Object":
                objeto.move_para_esquerda(2)
                janela_do_jogo.blit(objeto.get_image(), objeto.retangulo)
            elif objeto.__str__() == "Stone_Object":
                objeto.move_para_esquerda(5)
                janela_do_jogo.blit(objeto.get_image(), objeto.retangulo)

            #Atualiza lista, removendo objetos totalmente fora da tela.
            lista_de_objetos = [objeto for objeto in lista_de_objetos if objeto.retangulo.x > -100]

    #Retorna lista atualizada.   
    return lista_de_objetos

def dino_jump(dino_rect, dino_gravity):
    '''
    Esta função é responsável pelo efeito de pulo do dinossauro na tela.
    '''

    dino_rect.y += dino_gravity

    if dino_rect.bottom > 310:
        dino_rect.bottom = 310

def colidiu_com_obstaculo(dino_rect, lista_de_objetos):
    '''
    Retorna True se houver colisão entre o dinossauro e um objeto não moeda, e False se não.
    Se houver colisão entre o dinossauro e uma moeda, faz a moeda desaparecer.
    '''
    
    if lista_de_objetos:
        for objeto in lista_de_objetos:
            if dino_rect.colliderect(objeto.retangulo):
                if objeto.__str__() == 'Coin_Object':
                    lista_de_objetos.remove(objeto)
                    return False
                else:
                    return True
        else:
            return False

def exibe_tela_final(janela_do_jogo, potuacao_final):
    '''
    Exibe a tela final do jogo.
    '''

    #Configuração das superfícies de texto da tela.
    texto_fim_de_jogo = fonte_tela_inicial_ou_final.render("Game Over", False, 'Red')
    texto_jogar_novamente = fonte_principal(30).render("- Pressione qualquer tecla para reiniciar o jogo -", False, 'Yellow')

    #Inserção das superfícies de texto na janela do jogo.
    janela_do_jogo.fill('#112e0a')
    janela_do_jogo.blit(texto_fim_de_jogo, (200, -20))
    janela_do_jogo.blit(potuacao_final, (300, 100))
    janela_do_jogo.blit(texto_jogar_novamente, (190, 370))
    py.display.flip()

def reinicia_jogo(lista_de_objetos_do_jogo):
    '''
    Recebe uma lista de objetos e retorna ela vazia.
    '''

    return []

def fonte_do_jogo(tamanho_da_fonte):
        return py.font.Font("assets/fonts/PixelType.ttf", tamanho_da_fonte)

def fonte_inicio_fim_do_jogo(tamanho_da_fonte):
    return py.font.Font("assets/fonts/game_over.ttf", tamanho_da_fonte)

if __name__ == '__main__':
    main()