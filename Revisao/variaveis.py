#Tipos imbutidos:
print(2) 
#Para saber o tipo de dados usando o comando type():
print(type(2))  #O tipo de dados é inteiro (int). -> <class 'int'>

print("2")
print(type("2")) #O tipo de dados é string (str) porque está entre aspas. -> <class 'str'>

print(2.2)
print(type(2.2))  #O tipo de dados é float (float) porque tem casa decimal. -> <class 'float'>  

#=============================================================================================
#Regras de Variáveis:

#1 - Não se cria variável iniciando com números, caracteres especiais ou palavras reservadas do python. 
#Exemplo: 1num, @num, def, print, *sobrenome, etc.

#2 - Por Padrão as variáveis são criadas utilizando letras minúsculas, sem acentos e sem espaços.
#Exemplo: nome, sobre_nome, idade, telefone_1, etc.

mensagem = 'Revisão de novo' #O sinal (=) é o operador de atribuição, ou seja, ele atribui um valor a uma variável.
print(mensagem)   #A variável mensagem tem o valor 'Revisão de novo' e quando é chamada no print, ela imprime esse valor.

numero = 2
print(numero)     #A variável numero tem o valor 2 e quando é chamada no print, ela imprime esse valor.
print(type(numero)) #O tipo de dados da variável numero é inteiro (int). -> <class 'int'>

#3 Cometer Erro
# 1frase = "Tem um erro" 
# print(1frase) #Erro de sintaxe (SyntaxError) porque a variável não pode iniciar com um número.
