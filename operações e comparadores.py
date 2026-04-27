print (2+2) #adição
print (2-2) #subtração
print (2*2) #multiplicação
print (2/2) #divisão
print (2**2) #potência
print (2%2) #resto da divisão
print (2//2) #divisão inteira
print (2+2*2) #ordem de precedência
print ((2+2)*2) #uso de parênteses para alterar a ordem de precedência
# Comentário de linha única

""" Comentário de múltiplas linhas
que pode ser usado para explicar o código ou para desativar temporariamente um bloco de código
"""
# Variáveis
x = 10
y = 5
z = x + y
print (z) # Imprime o valor de z
# Tipos de dados
a = 10 # inteiro
b = 3.14 # float
c = "Olá, mundo!" # string
d = True # booleano
print (a, b, c, d) # Imprime os valores das variáveis

"""Operadores de comparação
"""
print (x > y) # maior que
print (x < y) # menor que
print (x == y) # igual a
print (x != y) # diferente de
print (x >= y) # maior ou igual a
print (x <= y) # menor ou igual a

"""Operadores de atribuição
"""
saldo = 1000
saldo += 500 # saldo = saldo + 500
print (saldo) # Imprime o novo saldo
saldo -= 200 # saldo = saldo - 200
print (saldo) # Imprime o novo saldo
saldo *= 2 # saldo = saldo * 2
print (saldo) # Imprime o novo saldo
saldo /= 4 # saldo = saldo / 4
print (saldo) # Imprime o novo saldo
saldo **= 2 # saldo = saldo ** 2
print (saldo) # Imprime o novo saldo
saldo %= 3 # saldo = saldo % 3
print (saldo) # Imprime o novo saldo
saldo //= 2 # saldo = saldo // 2
print (saldo) # Imprime o novo saldo

"""Operadores Lógicos
"""
True and True # Retorna True
True and False # Retorna False
False and False # Retorna False
True or True # Retorna True
True or False # Retorna True
False or False # Retorna False
not True # Retorna False
not False # Retorna True
print (x > 5 and y < 10) # operador AND
print (x > 5 or y < 10) # operador OR
print (not (x > 5)) # operador NOT

"""Operadores de identidade
"""
a = [1, 2, 3]
b = a
print (a is b) # Retorna True, pois a e b referenciam o mesmo objeto
c = [1, 2, 3]
print (a is c) # Retorna False, pois a e c são objetos diferentes, mesmo que tenham o mesmo conteúdo
print (a == c) # Retorna True, pois a e c têm o mesmo conteúdo

"""Operadores de associação
"""
a = [1, 2, 3]
print (1 in a) # Retorna True, pois 1 está no objeto a
print (4 not in a) # Retorna True, pois 4 não está no objeto a

