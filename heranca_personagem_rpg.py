class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome 
        self.vida = vida

class Classe():
    def __init__(self, nome_classe, habiliadade_primaria):
        self.nome_classe = nome_classe
        self.habiliadade_primaria = habiliadade_primaria
    def __str__(self):
        return f"{__class__.__name__} : {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"        

class Raça():
    def __init__(self, nome_raca, deslocamento, tamanho):
        self.nome_raca = nome_raca
        self.deslocamento = deslocamento
        self.tamanho = tamanho 
    def __str__(self):
        return f"{__class__.__name__} : {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"        

class Player(Personagem):
    def __init__(self, nome, vida, classe, raca):
        super().__init__(nome, vida)
        self.classe = classe
        self.raca = raca
    def __str__(self):
        return f"{__class__.__name__} : {', \n'.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}" 

raca_anao = Raça('Anão',7.5,'Médio')
classe_guerreiro = Classe('Guerreiro','Força')

travok = Player('Travok Balderk', 12, classe_guerreiro, raca_anao)

print(travok)


# class Inimigo:
#     pass