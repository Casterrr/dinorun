import pygame as py
from random import randint

from classes.coin import Coin
from classes.stone import Stone
from classes.cloud import Cloud

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

def cria_objetos():
    '''
    Retorna de maneira randômica objetos moedas, pedra ou nuvem.
    '''

    if randint(0,2) == randint(0,2):
        return Coin()
    
    if randint(0,1) == randint(0,1) == randint(0,1):
        return Cloud()
        
    else:
        return Stone()

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
                
            elif objeto.__str__() == "Cloud_Object":
                objeto.move_para_esquerda(1)
                janela_do_jogo.blit(objeto.get_image(), objeto.retangulo)

            #Atualiza lista, removendo objetos totalmente fora da tela.
            lista_de_objetos = [objeto for objeto in lista_de_objetos if objeto.retangulo.x > -100]

    #Retorna lista atualizada.   
    return lista_de_objetos

def main():
    pass

if __name__ == '__main__':
    main()