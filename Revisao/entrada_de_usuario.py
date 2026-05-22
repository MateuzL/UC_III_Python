'''No Python par obter dados do usuário, utilizamos o input().
O input() é uma função que permite ao usuário inserir dados durante a execução do programa quando solicitado.'''

frase = input("Digite uma frase: \n") #O texto entre aspas é a mensagem que será exibida para o usuário, indicando o que ele deve digitar.
print(frase) #O comando print() é usado para exibir a frase digitada pelo usuário na tela.

print(type(frase)) #O tipo de dados da variável frase é string (str) porque o input() sempre retorna uma string, mesmo que o usuário digite um número. -> <class 'str'>


numero = input("Digite um número: \n") #O texto entre aspas é a mensagem que será exibida para o usuário, indicando o que ele deve digitar.
print('O número digitado foi: ' + numero) #O comando print() é usado para exibir a mensagem "O número digitado foi: " seguida do número digitado pelo usuário. O operador de adição (+) é usado para concatenar a string com a variável numero.
print(type(numero)) #O tipo de dados da variável numero é string (str) porque o input() sempre retorna uma string, mesmo que o usuário digite um número. -> <class 'str'>

nome = input("Digite seu nome: \n")
idade = input("Digite sua idade: \n")
print('Seu nome é {}, e sua idade é {}'.format(nome, idade)) #O método format() é usado para formatar a string, substituindo os {} pelos valores das variáveis nome e idade, respectivamente. O resultado será algo como "Seu nome é João e sua idade é 30", dependendo do que o usuário digitar.    
print(f"Seu nome é {nome}, e sua idade é {idade}") #O f-string é uma forma mais moderna de formatar strings, onde as variáveis são inseridas diretamente dentro da string usando chaves {}. O resultado será o mesmo que o método format(), como "Seu nome é João e sua idade é 30", dependendo do que o usuário digitar.   
