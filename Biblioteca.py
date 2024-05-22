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

