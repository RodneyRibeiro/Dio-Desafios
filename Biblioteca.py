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

#impressão de variável
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

