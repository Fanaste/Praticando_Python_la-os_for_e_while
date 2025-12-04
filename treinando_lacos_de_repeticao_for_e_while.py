'''Exercicío 1)
Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.

Resolução:

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)
    
Exercício 2)

André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

contador = 0

while contador < 10:
    print("Processando dados...")


Qual é o problema do código de André e como resolver?
Resolução: O problema do código de André está na falta do incremento do contador, pois assim ficará em um loop infinito.

Exercício 3)
Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, como parte de uma campanha de marketing de sua plataforma chamada Buscante. Ele quer garantir que a mensagem seja exibida 5 vezes.

Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.

Resolução:

mensagem = [ "Bem-vindo ao Buscante!",  "Bem-vindo ao Buscante!",  "Bem-vindo ao Buscante!",  "Bem-vindo ao Buscante!",  "Bem-vindo ao Buscante!"]

for frase in mensagem:
    print(frase)
    
melhor resolução:
for i in range(5):
    print("Bem-vindo ao Buscante!")


Exercício 4)

Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.

valores = [10, 20, 30, 40, 50]

Crie um programa para implementar a soma.

Resolução:

valores = [10, 20, 30, 40, 50]

total = 0

for valor in valores:
    print(valor)
    total = total + valor 

print(f'O valor total da soma é {total}')

Exercício 5)
Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None:

Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".

Resolução:


projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None:
        print('Projeto ausente')
    else:
        print(projeto)



Exercício 6)

José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico é encontrado. A lista de livros já cadastrados no sistema é a seguinte:

Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.




livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f'Livro encontrado: {livro}')
        break


Exercício 7)

Você está desenvolvendo um sistema de controle de estoque para o Buscante. Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.

Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".

Resolução:
'''
'''    
livros = [5, 4, 3, 2, 1]
contador = 5

for estoque_restante in livros:
    contador = estoque_restante - 1
    print(f"Venda realizada! Estoque restante: {contador}")
    
print("Estoque esgotado")

estoque = 5

while estoque > 0:
    estoque = estoque - 1
    print(f"Venda realizada! Estoque restante: {estoque}")

print('Estoque esgotado')


Exercício 8)
Aline está implementando uma funcionalidade que exibe mensagens personalizadas para os clientes durante uma promoção especial da sua nova loja de livros. O sistema deve exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".

Crie um programa que utilize um laço for para exibir as seguintes mensagens:

Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".

Resolução:


regressiva = [11,10,9,8,7,6,5,4,3,2,1]
contador = 11

for numero in regressiva:
    contador = numero - 1
    if contador % 2 == 0: 
        print(f'Faltam apenas {contador} segundos - Não perca essa oportunidade!')
    else: 
        print(f'A contagem continua: {contador} segundos restantes')
        
print('Aproveite a promoção agora!')


Exercício 9)
Ana está implementando um sistema de filtragem de livros no Buscante. A funcionalidade deve percorrer uma lista de livros e exibir o nome de cada livro disponível em estoque. No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.

Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".


Resolução:

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] > 0:
        print(f"Livro disponível {livro["nome"]}")



Exercício 10)
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.

Resolução:


usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

while len(usuario) < 5 or len(senha) < 8:
        print("Usuário deve digitar uma senha ou usuário com mais caracteres")
        usuario = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
            
print("Cadastro realizado com sucesso!")

Resolução sugerida:
while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break
    
'''