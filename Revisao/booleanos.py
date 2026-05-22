''' Booleanos:
True: representa a verdade, ou seja, é um valor lógico que indica que uma condição é verdadeira.
False: representa a falsidade, ou seja, é um valor lógico que indica que uma condição é falsa.
0 é considerado False, enquanto qualquer valor diferente de 0 é considerado True.
1 é considerado True, enquanto 0 é considerado False.'''

#Exemplo de uso de booleanos:
'''print(1 == '1')
print(2 > 1)
print(2 < 1)
print(bool(2 == 2))
print(bool(0)) 
print(bool(''))
print(bool(None))'''

#================================================================================================

#Operações

'''
== igual
!= diferente
> maior
< menor
<= menor ou igual
>= maior ou igual
'''
#Operações com Bool
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) #O resultado é True porque as listas a e b têm os mesmos elementos na mesma ordem.
c = a
print(a is b) #O resultado é False porque a variável a e a variável b são objetos diferentes na memória, mesmo que tenham os mesmos elementos.
#O operador is verifica se as variáveis apontam para o mesmo objeto na memória, e nesse caso, a e b são objetos diferentes, então o resultado é False.

print(a is c) 

print(id(a)) #O resultado é um número inteiro que representa o endereço de memória onde a lista a está armazenada.
print(id(b)) #O resultado é um número inteiro diferente do id(a) porque a lista b é um objeto diferente da lista a, mesmo que tenham os mesmos elementos.
print(id(c)) #O resultado é o mesmo que id(a) porque a variável c é uma referência à mesma lista que a, ou seja, ambas apontam para o mesmo objeto na memória.

#O id é uma função embutida do Python que retorna o endereço de memória de um objeto.
