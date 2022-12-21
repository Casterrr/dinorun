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

def create_database(path="modules/database.db"):
    '''
    Cria arquivo de banco de dados 'database.db' com a tabela Ranking no diretório 'modules/' por padrão.
    '''

    #Importando biblioteca do banco de dados.
    import sqlite3 as sql3

    #Estabelecendo conexão com o bando de dados.
    conexao = sql3.connect(path)

    with conexao:
        cursor = conexao.cursor()
        
        #Criando tabela Ranking.
        cursor.execute("""CREATE TABLE Ranking(id INTEGER, colocacao INTEGER, nome TEXT, score INTEGER, 
                        PRIMARY KEY(id AUTOINCREMENT) )""")
    
def valida_requisitos_para_insercao_no_ranking(ranking, jogador):
    '''
    Confere se um dado jogador pode entrar no top ranking.
    Se sim, retorna um Integer correspondente a colocação do jogador no pódio.
    Caso não, retorna False.
    '''

    #Confere se o ranking possui colocações vazias.
    if not ranking.primeiro_lugar:
        return 1
    else:
        if not ranking.segundo_lugar:
            return 2
        else:
            if not ranking.terceiro_lugar:
                return 3

    #Realiza conferência proposta pela função.
    if jogador.score >= ranking.terceiro_lugar.score:
        if jogador.score >= ranking.segundo_lugar.score:
            if jogador.score >= ranking.primeiro_lugar.score:
                return int(1)
            else:
                return int(2)
        else:
            return int(3)
    else:
        return False

def insere_jogador_no_ranking(ranking, jogador, colocacao):
    '''
    Adiciona jogador a um ranking e em sua respectiva colocação.
    Atualiza o ranking caso necessário.
    '''

    match colocacao:
        case 1:
            ranking.terceiro_lugar = ranking.segundo_lugar
            ranking.segundo_lugar = ranking.primeiro_lugar
            ranking.primeiro_lugar = jogador
        case 2:
            ranking.terceiro_lugar = ranking.segundo_lugar
            ranking.segundo_lugar = jogador
        case 3:
            ranking.terceiro_lugar = jogador

def main():
    pass

if __name__ == '__main__':
    main()