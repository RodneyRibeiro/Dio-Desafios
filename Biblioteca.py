# PARA TESTAR O TÓPICO, COPIE O VALOR ABAIXO DOS COMENTÁRIOS.

# 1 - Variável / Print / CONSTANTES -----------------------------------------------------------------------------------------------------------------
print ("-------------------Variável / Print / CONSTANTES-------------------")
variavel01 = "teste"
print (variavel01)
print ("teste")
print (1,2,3,4)

# 2 - Convertendo os Tipos de Variávels --------------------------------------------------------------------------------------------------------------
'''
Utilizar a função int(),float(),str(),list().
Para converter as variáveis existentes. 
Conforme citado em TIPO de dados.
'''

# 3 - Variável constante deve ser escrita em caixa alta para respeitar a convenção. -----------------------------------------------------------------
VARIAVEL02 = "TESTE"

# 4 - Tipo de Dados ---------------------------------------------------------------------------------------------------------------------------------
'''
Texto       str
Numérico    int,float,complex
Sequência   list,tuple,range
Mapa        dict
Coleção     set,fronzenset
Booleano    bool
Binário     bytes,bytearray,memoryview
'''

# 5 - Modo Iterativo -------------------------------------------------------------------------------------------------------------------------------
'''
Abra o terminal do VSCODE e digite python ou python -i app.py
Vai poder testar o arquivo py ou simular um código ou um teste
rápido.
'''

# 6 - Funções de Entrada e Saída -------------------------------------------------------------------------------------------------------------------
print ("-------------------Funções de Entrada e Saída-------------------")
'''
Para incluir um valor de entrada pelo utilizador.
input()
Também pode Usar:
variavel03=input("Informe Seu nome: ")
'''
#\n representa o espaço e o end adiciona estes valores no final
#sep separa as strings pela string definida
print("nome", "sobrenome", end="...\n")
print("nome", "sobrenome", sep="#")

#Interpolação de de variável
print(f"Variavel01 = ''{variavel01}'' ")

# 7 - Operadores -----------------------------------------------------------------------------------------------------------------------------------
'''
Além das operações padrões da matemáticas, podemos atribuir
valores a variáveis já usando um operador.
'''
variavel03 = 2
variavel03 += 1
variavel03 *= 2
variavel03 **= 2 #Exponencial e %= para módulo
variavel03 /= 1
variavel03 //= 1 #Divisao com resultado em número inteiro

print (variavel03)
# resultado apresenta 36.0, pois mesmo utilizando // após ter dividido por 1,
#apresenta número flutuante.

# 8 - Operadores Lógicos ----------------------------------------------------------------------------------------------------------------------------
print("----------------------Operadores Lógicos----------------------", end="\n")
'''
Operador and / Operador or / Negação not
'''
variavel04  = 100
variavel05 = 100
variavel06 = 500
print(variavel04  == variavel05 and variavel04 != variavel06) #TRUE
print(not variavel04 == variavel06) #TRUE

# 9 - Operadores Identidade --------------------------------------------------------------------------------------------------------------------------
'''
Saber se dois objetos ocupam a mesma posição na memória.
'''
variavel07  = "Curso de Python"
varivel08   = variavel07

# 10 - Operadodes de Associação ----------------------------------------------------------------------------------------------------------------------
print("-------------------Operadores de Associação-------------------", end="\n")
'''
Verificar se um objeto está dentro de uma sequência.
'''
variavel09  = "Curso Python"
variavel10 = ["laranja","uva","limão"]
variavel11  = [1500,100]

print("Python" in variavel09)      # True
print("maçã" not in variavel10)   # True
print(200 in variavel11)           # False

# 11 - Estruturas Condicionais ------------------------------------------------------------------------------------------------------------------------
print("-------------------Estruturas Condicionais-------------------", end="\n")

'''
IF / ELIF / ELSE
'''
variavel12 = 9
variavel13 = 10
if variavel12 == 9:
    print ("Condição verdadeira da variável 12.")
elif variavel13 == 10:
    print ("Condição verdadeira da variável 13, porém o IF é atendido primeiro e não vai ocorrer este elif")
else:
    print ("Condiçõles não foram atendidas.")

'''
IF Ternário
'''
variavel14 = "Sucesso" if variavel12 == 9 else "falha"
print(variavel14)

# 11 - Estruturas de Repetição ------------------------------------------------------------------------------------------------------------------------
print("-------------------Estruturas de Repetição-------------------", end="\n")
'''
Comandos FOR / ELSE
Usar para percorrer uma repetição, objeto iterável, pode se usar também quando sabemos a quantidade de vezes que o valor da primeira variável depois do "for"
vai ser encontrada da segunda variável depois do "in".
'''
variavel15="TEXTO DE TESTE"
VOGAIS="AEIOU"

for letra in variavel15:
    if letra.upper() in VOGAIS:
        print(letra, end=" ") #EOEEE
else: 
    print() # adiciona uma quebra de linha

print("\n")

'''
Comandos RANGE / RANGE COM FOR
Utilizar quando se sabe a quantidade de vezes que vai repetir.
'''

print(list(range(5))) #[0, 1, 2, 3, 4]

for numero in range(0,10): #0 1 2 3 4 5 6 7 8 9
    print(numero, end=" ")

print("\n")

for numero2 in range(0,51,5): #0 5 10 15 20 25 30 35 40 45 50
    print(numero2, end=" ")

print("\n")

'''
Comandos WHILE / ELSE
Usar quando não se sabe a quantidade de vezes que vai ser executado.
'''

variavel16 = -4

while variavel16 != 0:
    if variavel16 < 0:
        print(f"Passei por aqui com número = {variavel16}") # Passei por aqui com número = -4/-3/-2/-1
    
    variavel16 += 1
else:
    print()


# 12 - String e Fatiamento ------------------------------------------------------------------------------------------------------------------------
print("-------------------String e Fatiamento-------------------", end="\n")

'''
Maiúsculo, Minúsculo, Título
'''
variavel17 = "pYtHon"
print(variavel17.upper()) #TUDO MAIÚSCULO
print(variavel17.lower()) #tudo minúsculo
print(variavel17.title()) #Primeira letra maiúscula

'''
Removendo espaço em Branco
'''
variavel18 = "  Python "
print(variavel18.strip()) #REMOVE TODOS OS ESPAÇOS
print(variavel18.lstrip()) #ESPAÇO DO LADO ESQUERDO
print(variavel18.rstrip()) #ESPAÇO DO LADO DIREITO


'''
Junções e Centralização
'''

variavel19 = "Python"

print(variavel19.center(10,"#"))
print(".".join(variavel19))

'''
Interpolação de de variável
'''

print(f"Utilizar variáveis junto a string como esta {variavel19}")

'''
Formatar String
'''

variavel20 = 3.14159

print(f"Valor da variável com 2 casas após a vírgula: {variavel20:.2f}")
print(f"Valor da variável com 2 casas após a vírgula: {variavel20:10.2f}")

'''
Fatiar String
'''

variavel21 = "Antonio de Pádua Lisboa"

print(variavel21[0])   # SOMENTE PRIMEIRA LETRA
print(variavel21[:10]) # ATÉ O 10º CARACTER
print(variavel21[10:]) # A PARTIR DO 10º CARACTER
print(variavel21[::-1])# AO CONTRÁRIO

'''
String Multiplas Linhas(String Triplas)
'''

variavel22 = """\nOlá, isto é um teste.
Percebe que respeita exata formatação.
Por estar usando a string tripla.
"""

print (variavel22)

# 13 - Listas ------------------------------------------------------------------------------------------------------------------------
print("-------------------Listas-------------------", end="\n")

#EXEMPLO DE LISTA
variavel22 = ["Batata","Maçã","Laranja"]
variavel23 = [1,2,3]
variavel23 = [1,"Batata",[2,"Maçã"]]

'''
Listas Aninhadas
'''

variavel24 =[
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
] 

print(variavel24[0]) # [1, "a", 2]
print(variavel24[0][0]) # 1
print(variavel24[0][-1]) # 2
print(variavel24[-1][-1]) # c
      
#FATIAMENTO DA LISTA FUNCIONA DO MESMO MODO QUE DA STRING

'''
ITERAR Listas
'''
variavel25 = 0
for list in variavel22:
    print(variavel22[variavel25])
    variavel25  += 1

'''
ENUMERATE Saber qual índice do objeto da lista
'''
for indice,list in enumerate(variavel22):
    print(f"{indice}:{list}")
# 0:Batata
# 1:Maçã
# 2:Laranja

# 14 - Métodos da Classe List ------------------------------------------------------------------------------------------------------------------------
print("-------------------Métodos da Classe List-------------------", end="\n")

'''
[].append
Adiciona valores a lista em ordem
'''
variavel26 = []
variavel26.append(1)
variavel26.append("Teste")
variavel26.append([1,2,3]) # [1, 'Teste', [1, 2, 3]]

print(variavel26)

'''
[].copy
Copia  a lista
'''
variavel27  = variavel26.copy()
variavel27.append("Variavel27")

print (variavel27)

'''
[].clear
Apaga toda a lista
'''
variavel26.clear()
print(variavel26) # []

'''
[].count
Conta quantos objetos há na lista
'''

print (variavel27.count("Variavel27")) # 1

'''
[].extend
Adiciona elementos ao fim da lista
'''

variavel26.extend(["Teste","Variavel26"])
print (variavel26) #['Teste', 'Variavel26']

'''
[].index
Diz qual o index do objeto citado
'''

print(variavel26.index("Teste")) # 0

'''
[].pop
Remove itens da lista em ordem da direita para esquerda
'''

variavel26.pop() #remove Variavel26
variavel26.pop(0) # remove teste que está no índice 0
print (variavel26)

'''
[].remove
Remove itens da lista citados no valor entre ()
'''
variavel26.append("Variavel26")
variavel26.append("Teste")
variavel26.remove("Variavel26") #remove Variavel26
print (variavel26)

'''
[].reverse
Inverte a Ordem da Lista
'''
variavel27=[1,2,3,4,5,6,7,8,9,10]
variavel27.reverse()
print (variavel27) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

'''
[].sort
Ordena a lista em ordem decrescente ou crescente se o parâmetro for reverse=True
'''
variavel28  = ["python","js","c","java","csharp"] 
variavel28.sort()
print(variavel28) #['c', 'csharp', 'java', 'js', 'python']

variavel28.sort(reverse=True) #['python', 'js', 'java', 'csharp', 'c']
print(variavel28)

'''
len
Conta quantos itens há em uma lista, também pode usar para contar quantos caracteres há em uma string.
'''
print(len(variavel28)) #5
print(len("123456")) #6

# 18 - TUPLAS ------------------------------------------------------------------------------------------------------------------------
print("-------------------TUPLAS-------------------", end="\n")

'''
São praticamente a mesma coisa que lista, no entanto, são imutáveis. Ou seja, não tem como modificá-las.
Os métodos da Tuplas são: [].count,[].index e len
'''

variavel29 = ("teste1","teste2","teste3",)
variavel30 = tuple("python")
variavel31 = ("Brasil",)
print(variavel29)
print(type(variavel29))

# 19 - CONJUNTOS ------------------------------------------------------------------------------------------------------------------------
print("-------------------CONJUNTOS-------------------", end="\n")

'''
SETS
Elimina dados repetidos em conjuntos
'''
print(set([1,2,3,4,4,5,5,6,7,7,8,9,10])) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set("Abacaxi")) #{'b', 'i', 'a', 'c', 'x', 'A'}
print(set(("palio","gol","palio"))) #{'gol', 'palio'}

'''
Também pode usar {} para definir o comando SET
'''
print({1,2,3,4,4,5,5,6,6,7,8,9,10}) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

'''
Acessar dados, deve converter para lista primeiro

variavel32 = {1,2,3,2}
variavel32 = list(variavel32)
variavel32[0]
'''

'''
Métodos de Classe - SET
{}.union
UNIÃO ENTRE OS CONJUNTOS NA ORDEM REQUISITADA
'''

variavel33_a = {1,2}
variavel33_b = {3,4}
print(variavel33_a.union(variavel33_b)) # {1, 2, 3, 4}

'''
Métodos de Classe - SET
{}.intersection
VALORES EM COMUM
'''
variavel34_a = {1,2,3}
variavel34_b = {2,3,4}
print(variavel34_a.intersection(variavel34_b)) # {2, 3}

'''
Métodos de Classe - SET
{}.difference
RETORNA O QUE O DA ESQUERDA TEM E O QUE O DA DIREITA NÃO TEM
'''
variavel35_a = {1,2,3}
variavel35_b = {2,3,4}
print(variavel35_a.difference(variavel35_b)) # {1}
print(variavel35_b.difference(variavel35_a)) # {4}


'''
Métodos de Classe - SET
{}.symmetric_difference
DIFERENÇA ENTRE OS DOIS
'''
variavel36_a = {1,2,3}
variavel36_b = {2,3,4}
print(variavel36_a.symmetric_difference(variavel36_b)) # {1, 4}

'''
Métodos de Classe - SET
{}.issubset
Se o conjunto da esquerda, está inteiramente dentro do da direita.
Caso tenha algum objeto que não esteja, retorna Falso.
TRUE -> ESQUERDA ESTA DENTRO DA DIREITA
FALSE -> ESQUERDA NÃO ESTA DENTRO DA DIREITA
'''
variavel37_a = {1,2,3}
variavel37_b = {4,1,2,5,6,3}
print(variavel37_a.issubset(variavel37_b)) # True
print(variavel37_b.issubset(variavel37_a)) # False

'''
Métodos de Classe - SET
{}.issuperset
Se o conjunto da esquerda, NÃO está inteiramente dentro do da direita.
Caso tenha algum objeto que esteja, retorna True.
TRUE -> DIREITA ESTA DENTRO DA ESQUERDA
FALSE -> DIREITA NÃO ESTA DENTRO DA ESQUERDA
'''

variavel37_a = {1,2,3}
variavel37_b = {4,1,2,5,6,3}
print(variavel37_a.issuperset(variavel37_b)) # False
print(variavel37_b.issuperset(variavel37_a)) # True

'''
Métodos de Classe - SET
{}.isdisjoint
Se o conjunto da esquerda, não possui nenhum elemento dentro do conjunto da direita.
Comparar se são distintos sem exceção.
TRUE -> SÃO DISTINTOS
FALSE -> POSSUI ALGUM ELEMENTO EM COMUM
'''
variavel38_a = {1,2,3,4,5}
variavel38_b = {6,7,8,9}
variavel38_c = {1,0}
print(variavel38_a.isdisjoint(variavel38_b)) # True
print(variavel38_a.isdisjoint(variavel38_c)) # False

'''
Métodos de Classe - SET
Alguns métodos utilizado pelo SET são os mesmos da LISTA:
{}.add -> Adiciona valores DISTINTOS no final da lista. Se existir o valor ignora o comando.
{}.clear / {}.copy
{}.discart -> Descarta o valor citado, variavel.discart(45) por exemplo e ignora se não existir.
{}.pop -> Apaga da esquerda para direita, ao contrário da lista
{}.remove -> O mesmo que o discart, mas ocorre erro se o valor não existir.
len / in
'''

# 20 - DICIONÁRIOS ------------------------------------------------------------------------------------------------------------------------
print("-------------------DICIONÁRIOS-------------------", end="\n")

'''
DICIONÁRIOS
Criação
'''

variavel39 = {"nome":"Antonio","idade":48}
variavel39 = dict(nome="Antonio", idade=48)
variavel39["telefone"] = "3333-1234"

print(variavel39)

'''
DICIONÁRIOS
Acessar
'''
print(variavel39["telefone"]) #3333-1234

'''
DICIONÁRIOS
Iterar
'''
for chave in variavel39:
    print(chave,variavel39[chave])

# nome Antonio
# idade 48
# telefone 3333-1234

'''
Métodos de Classe - DICT (DICIONÁRIO)
{}.fromkeys
ADICIONA VALOR EM COMUM A CHAVES CITADAS
'''
variavel40 = dict.fromkeys(["nome","telefone"],"ValorTeste")
print(variavel40) #{'nome': 'ValorTeste', 'telefone': 'ValorTeste'}

'''
Métodos de Classe - DICT (DICIONÁRIO)
{}.get
PROCURA CHAVE NO DICIONÁRIO E SE NÃO ENCONTRAR, RETORNA NONE OU SE,
CASO TENHA CITADO VALOR APÓS ENTRE {}, RETORNA ESTE VALOR.
'''
print(variavel40.get("nome")) #None
print(variavel40.get("NãoExiste"),{"Não encontrei"}) #{'Não encontrei'}

'''
Métodos de Classe - DICT (DICIONÁRIO)
{}.itens
EXIBE OS ITENS
'''
print(variavel40.items()) #dict_items([('nome', 'ValorTeste'), ('telefone', 'ValorTeste')])

'''
Métodos de Classe - DICT (DICIONÁRIO)

EXIBE OS ITENS
'''

'''
Métodos de Classe - DICT (DICIONÁRIO)
Alguns métodos utilizado pelo SET são os mesmos da LISTA:
{}.clear / {}.copy
{}.keys -> Retorna as Chaves do Dicionário
{}.pop -> Apaga somente se citar o valor entre () e se não achar o valor, pode retornar algo depois da ,.
len / in
'''

# 20 - Programação Orientada a Objeto(POO)/(OOP) ------------------------------------------------------------------------------------------------------------------------
print("-------------------Programação Orientada a Objeto(POO)/(OOP)-------------------", end="\n")

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()

# 21 - Herança na (POO)/(OOP) ------------------------------------------------------------------------------------------------------------------------
print("-------------------Herança na (POO)/(OOP)-------------------", end="\n")

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
