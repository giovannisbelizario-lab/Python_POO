#Exercício 1:
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo:<15} | Cor: {self.cor:<15} | Ano: {self.ano:>4}'

carro1 = Carro('Honda Civic', 'Preto', 2026)
print(carro1)

#Exercício 2, 3 e 4:
class Restaurante: 
    def __init__(self, nome, categoria, capacidade, nota):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota = nota

    def __str__(self):
        return f'''Nome do estabelecimento: {self.nome}
Categoria: {self.categoria}
Ativo: {self.ativo}
Capacidade: {self.capacidade}
Nota: {self.nota}'''

restaurante1 = Restaurante('Tanka', 'Japonês', 200, 5.0)
print(restaurante1)

#Exercício 5:
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome}, {self.idade} anos. Email: {self.email}, telefone: {self.telefone}'

cliente1 = Cliente('Giovanni', 27, 'giovanni@gmail.com', '987-654-3210')
print(cliente1)