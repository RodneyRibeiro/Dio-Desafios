def menu():
 #Menu aparece todas as vezes que sai da opção selecionada.
 print ("""
       [1] Saque
       [2] Deposito
       [3] Extrato
       [4] Sair
    """)
    #Seleção do menu
 return int(input())

def depositar(saldo,deposito,extrato,/):
   saldo = saldo + deposito
   extrato.append("Deposito: R$"+str(deposito) + " Saldo: R$" + str(saldo))
   print (f"Seu saldo é de R${saldo}.")
   return saldo,extrato

def sacar(*,saldo,saque,extrato,saques_total):
    saldo = saldo - saque
    saques_total -= 1
    extrato.append("Saque: R$"+str(saque) + " Saldo: R$" + str(saldo))
    print (f"Seu saldo é de R${saldo} e ainda possui {saques_total} saques hoje.")
    return saldo,extrato,saques_total

def emitir_extrato(saldo,/,*,extrato):
    print ("Seu Saldo é de: ",saldo," Extrato: ",extrato)

# def criar_usuario(usuario):

# def filtrar_usuario(cpf,usuario):

# def criar_conta (agencia,numero_conta,usuarios):

# def listar_contas (contas):

#Menu Saque ---------------------------------------------------------------------------
def main():
    #variáveis
    AGENCIA="0001"
    saldo = 1000.0
    saques_total=3
    extrato = []

    while True:
       opcao  = menu()
       if opcao == 1:
           print ("Saque\n")
           print ("Digite o Valor para Saque:\n")
           #Round para garantir que o saldo tenha 2 dígitos após a vírgula
           saque = round(float(input()),2)
           #Prevenção de valores negativos
           if saque < 0:
               print ("Valor digitado é inválido. Digite um valor positivo")
           #Limite de saque 500
           elif saque > 500:
                print ("Valor de saque excede o máximo permitido.(500)")
           #Testar se não há saldo    
           elif saque >= saldo and saques_total > 0:
               print ("Não há saldo")
           #Condição que o saque seja menor que o Saque e que esteja dentro dos 3 saques disponíveis
           elif saque <= saldo and saques_total > 0:
               saldo,extrato,saques_total = sacar(saldo=saldo,saque=saque,extrato=extrato,saques_total=saques_total)
           elif saques_total == 0:
               print ("Limite de Saques Atingido.")
       #Menu Depósito --------------------------------------------------------------------------
       elif opcao == 2:
           print ("Depósito")
           print ("Digite o Valor para Depósito:\n")
           #Round para garantir que o saldo tenha 2 dígitos após a vírgula
           deposito = round(float(input()),2)
           #Prevenção de valores negativos ou igual a 0
           if deposito <= 0:
               print ("Valor digitado é inválido. Digite um valor positivo")
           else:
               saldo,extrato = depositar(saldo,deposito,extrato)
       #Menu Extrato ---------------------------------------------------------------------------
       elif opcao == 3:
           emitir_extrato(saldo,extrato=extrato)           
       #Menu Sair ------------------------------------------------------------------------------
       elif opcao == 4:
           print ("Obrigado por ser nosso cliente.")
           break
       #Prevenção de erro-----------------------------------------------------------------------
       else:
           print ("Opção Incorreta, tente de novo.")

main()