from classes.player import Player

class Ranking():
    def __init__(self):
        self.primeiro_lugar = Player
        self.segundo_lugar = Player
        self.terceiro_lugar = Player
        
        self.podio = [self.primeiro_lugar, self.segundo_lugar, self.terceiro_lugar]
    
    def atualiza_podio(self, jogador):
        '''
        Confere se um dado jogador pode entrar no pódio.
        Caso sim, atualiza o pódio.
        '''

        if jogador.score >= self.terceiro_lugar.score:
            if jogador.score >= self.segundo_lugar.score:
                
                if jogador.score >= self.primeiro_lugar.score:
                    self.terceiro_lugar = self.segundo_lugar
                    self.segundo_lugar = self.primeiro_lugar
                    self.primeiro_lugar = jogador
                else:
                    self.terceiro_lugar = self.segundo_lugar
                    self.segundo_lugar = jogador
            else:
                self.terceiro_lugar = jogador