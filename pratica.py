class Restaurante: 
    nome = ''
    # Exercício 4:
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'

# Exercício 1:
restaurante_praca.categoria = 'Italiana'

# Exercício 2:
print(restaurante_praca.nome)

# Exercício 3:
print(restaurante_praca.ativo)
if restaurante_praca.ativo:
    print('Restaurante ativo.')
else:
    print('Restaurante inativo.')

# Exercício 5:
restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

# Exercício 6:
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Exercício 7:
print(restaurante_pizza.categoria)

# Exercício 8:
restaurante_pizza.ativo = True
print(restaurante_pizza.ativo)

# Exercício 9:
print(vars(restaurante_praca))