# Conhecendo métodos úteis da classe string

# Maiúscula
print('python'.upper())  # PYTHON
# Minúscula
print('PYTHON'.lower())  # python
# Primeira letra maiúscula
print('python'.capitalize())  # Python
# Primeira letra de cada palavra maiúscula
print('python é uma linguagem de programação'.title())  # Python É Uma Linguagem De Programação

#Eliminando espaços em branco

curso = "   Curso de Python   "
print(curso.strip())  # "Curso de Python"
print(curso.lstrip())  # "Curso de Python   "
print(curso.rstrip())  # "   Curso de Python"

#Junções e centralizações

curso = "Python"

print(curso.center(10, "#"))  # "#######Python#######"
print(".".join(curso))  # "P.y.t.h.o.n"
