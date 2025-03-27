from random import randint


class Personagem:
    def __init__(self, nome, race, classe, vida):
        self.nome = nome
        self.race = race
        self.classe = classe
        self.vida = vida
    
    def atacar(self):
        resultado = randint(1,20)
        dano = (randint(1,6) + randint(1,6)) + 3
        if resultado >= 11:
            print('-----------------------------')
            print(f'{self.nome} Ataca...')
            print(f'Dado = {resultado}')
            print(f'{self.nome} Acertou o ataque')
            print(f'O inimigo sofreu {dano} de dano')
            print('-----------------------------')
        if resultado <= 10:
            print('-----------------------------')
            print(f'{self.nome} Errou o ataque')
            print('-----------------------------')
    
    def investigar(self):
        print(f'{self.nome} está investigando...')
    
    def descansar(self):
        print(f'{self.nome} está descansando')

    def __str__(self):
        return f"{__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


otto = Personagem('Otto','Humano','Ranger',11)
print(otto)
otto.atacar()
otto.atacar()
otto.atacar()

