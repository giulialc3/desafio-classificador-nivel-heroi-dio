# Escrevendo as classes de um jogo

class hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'a espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        else:
            ataque = 'shuriken'
        return ataque


nome = str(input('Digite o nome do seu herói: '))
idade = int(input('Insira a idade do seu herói: '))
tipo = (input('Insira o tipo do seu herói: '))

heroi = hero(nome, idade, tipo)
ataqueHeroi = heroi.atacar()
print(f'O herói {nome} do tipo {tipo} atacou usando {ataqueHeroi}')


