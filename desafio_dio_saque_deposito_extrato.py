'''
    Desafio DIO onde devemos implementar sistema de conta bancária
    com saque, depósito e extrato.
'''

# Variáveis.
SALDO = 1000.0
SAQUES_TOTAL=3
Extrato = []

while True:
    # Menu aparece todas as vezes que sai da opção selecionada.
    print ("""
       [1] Saque
       [2] Deposito
       [3] Extrato
       [4] Sair
       """)
    # Seleção do menu
    menu = int(input())
    # Menu Saque ---------------------------------------------------------------------------
    if menu == 1:
        print ("Saque\n")
        print ("Digite o Valor para Saque:\n")
        # Round para garantir que o SALDO tenha 2 dígitos após a vírgula
        saque = round(float(input()),2)
        # Prevenção de valores negativos
        if saque < 0:
            print ("Valor digitado é inválido. Digite um valor positivo")
        # Limite de saque 500
        elif saque > 500:
            print ("Valor de saque excede o máximo permitido.(500)")
        # Testar se não há SALDO
        elif saque >= SALDO and SAQUES_TOTAL > 0:
            print ("Não há SALDO")
        # Condição que o saque seja menor que o Saque e que esteja dentro dos 3 saques disponíveis
        elif saque <= SALDO and SAQUES_TOTAL > 0:
            SALDO = SALDO - saque
            SAQUES_TOTAL -= 1
            Extrato.append("Saque: R$"+str(saque) + " SALDO: R$" + str(SALDO))
            print (f"Seu saldo é de R${SALDO} e ainda possui {SAQUES_TOTAL} saques hoje.")
        elif SAQUES_TOTAL == 0:
            print ("Limite de Saques Atingido.")
    # Menu Depósito --------------------------------------------------------------------------
    elif menu == 2:
        print ("Depósito")
        print ("Digite o Valor para Depósito:\n")
        # Round para garantir que o SALDO tenha 2 dígitos após a vírgula
        deposito = round(float(input()),2)
        # Prevenção de valores negativos ou igual a 0
        if deposito <= 0:
            print ("Valor digitado é inválido. Digite um valor positivo")
        else:
            SALDO = SALDO + deposito
            Extrato.append("Deposito: R$"+str(deposito) + " SALDO: R$" + str(SALDO))
            print (f"Seu SALDO é de R${SALDO}.")
    # Menu Extrato ---------------------------------------------------------------------------
    elif menu == 3:
        print ("Extrato")
        print (Extrato)
    # Menu Sair ------------------------------------------------------------------------------
    elif menu == 4:
        print ("Obrigado por ser nosso cliente.")
        break
    # Prevenção de erro-----------------------------------------------------------------------
    else:
        print ("Opção Incorreta, tente de novo.")
# End-of-file (EOF)
