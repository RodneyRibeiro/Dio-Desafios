"""Desafio DIO onde devemos implementar sistema de conta bancária
    com saque, depósito e extrato, utilizando funções.
"""
def menu():
    """
    Exibe Menu para saque.
    """
    # Menu aparece todas as vezes que sai da opção selecionada.
    print ("""
            [1] Saque
            [2] Deposito
            [3] Extrato
            [4] Criar Conta
            [5] Novo Usuário
            [6] Listar Contas
            [7] Sair
       """)
       # Seleção do menu
    return int(input())

def depositar(saldo,deposito,extrato,/):
    """Função para depósitar valor em conta.

    Args:
        saldo (Float): Saldo da conta
        deposito (Float): Valor a ser depositado
        extrato (List): Lista com extrato de depósitos e saque

    Returns:
        saldo (Float): Retorno do novo saldo
        extrato (List): Retorno do extrato com lista atualizada
    """
    saldo = saldo + deposito
    extrato.append("Deposito: R$"+str(deposito) + " Saldo: R$" + str(saldo))
    print (f"Seu saldo é de R${saldo}.")

    return saldo,extrato

def sacar(*,saldo,saque,extrato,saques_total):
    """Função para saque de valor do saldo em conta.

    Args:
        saldo (Float): Saldo da conta.
        saque (Float): Valor do saque que será debitado da conta.
        extrato (List): Lista com extrato de depósitos e saque.
        saques_total (int): Limite total de saques.

    Returns:
        saldo (Float): Retorno do novo saldo
        extrato (List): Retorno do extrato com lista atualizada
        saques_total (int): Atualiza o total de saques
    """

    saldo = saldo - saque
    saques_total -= 1
    extrato.append("Saque: R$"+str(saque) + " Saldo: R$" + str(saldo))
    print (f"Seu saldo é de R${saldo} e ainda possui {saques_total} saques hoje.")

    return saldo,extrato,saques_total

def emitir_extrato(saldo,/,*,extrato):
    """Exibe extrato sobre depósitos e saques da conta.

    Args:
        saldo (Float): Saldo da conta.
        extrato (List): Lista com extrato de depósitos e saque.
    """
    print ("Seu Saldo é de: ",saldo," Extrato: ",extrato)

def criar_usuario(usuarios):
    """Cria conta no banco com usuário digitado

    Args:
        usuarios (str): Nome do usuário do sistema
    """
    cpf = input("Informe o CPF do novo usuário(somente números):")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print ("\n Já existe usuário com este CPF!")

        return

    nome = input("Informe o nome completo: ")
    data_nascimento= input ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco= input ("Informe o endereço(logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print ("+++Usuário criado com sucesso!+++")

def filtrar_usuario(cpf,usuarios):
    """Verifica a existência de usuários já cadastrados pelo CPF.
    Caso não exista, retorna lista vazia.

    Args:
        cpf (int): Número de identificação social brasileiro.
        usuarios (str): Nome do usuário do sistema.

    Returns:
        usuarios_filtrados(list): Lista retorna vazia caso não tenha usuários no sistema.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia,numero_conta,usuarios):
    """Cria conta após verificação da ausência de usuáruio com cpf citado.

    Args:
        agencia (int): Agência 0001 com valor constante.
        numero_conta (int): Valor gerado automaticamente, contando valores em lista.
        usuarios (str): Valor já cadastrado na função criar_usuario

    Returns:
        string: Texto com extrato de movimentação da conta.
    """
    cpf = input("Digite o CPF do usuario: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso! ")
        return {"agencia": agencia,"numero_conta":numero_conta,"usuario":usuario}

    print ("Usuário não encontrado, sistema será encerrado!")

def listar_contas (contas):
    """Lista as contas cadastradas

    Args:
        contas (list): Lista com contas cadastradas.

    """
    for conta in contas:
        texto = f"""\
             Agência: \t{conta["agencia"]}
             Conta:\t1t{conta["numero_conta"]}
             Titular:\t{conta["usuario"]["nome"]}
        """
    print (texto)

# Menu Saque ---------------------------------------------------------------------------
def main():
    """Função com as ações principais, chama as outras funções.

    """
    # Variáveis
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 1000.0
    saques_total = 3
    extrato = []

    while True:
        opcao  = menu()
        if opcao == 1:
            print ("Saque\n")
            print ("Digite o Valor para Saque:\n")
            # Round para garantir que o saldo tenha 2 dígitos após a vírgula
            saque = round(float(input()),2)
            # Prevenção de valores negativos
            if saque < 0:
                print ("Valor digitado é inválido. Digite um valor positivo")
            # Limite de saque 500
            elif saque > 500:
                print ("Valor de saque excede o máximo permitido.(500)")
            # Testar se não há saldo
            elif saque >= saldo and saques_total > 0:
                print ("Não há saldo")
            # Condição que o saque seja menor que
            # o Saque e que esteja dentro dos 3 saques disponíveis
            elif saque <= saldo and saques_total > 0:
                saldo,extrato,saques_total = sacar(
                                                   saldo=saldo,
                                                   saque=saque,
                                                   extrato=extrato,
                                                   saques_total=saques_total
                                                   )
            elif saques_total == 0:
                print ("Limite de Saques Atingido.")
        # Menu Depósito --------------------------------------------------------------------------
        elif opcao == 2:
            print ("Depósito")
            print ("Digite o Valor para Depósito:\n")
            # Round para garantir que o saldo tenha 2 dígitos após a vírgula
            deposito = round(float(input()),2)
            # Prevenção de valores negativos ou igual a 0
            if deposito <= 0:
                print ("Valor digitado é inválido. Digite um valor positivo")
            else:
                saldo,extrato = depositar(saldo,deposito,extrato)
        # Menu Extrato ---------------------------------------------------------------------------
        elif opcao == 3:
            emitir_extrato(saldo,extrato=extrato)
        # Menu Conta ---------------------------------------------------------------------------
        elif opcao == 4:
            print ("Criar Conta")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
         #Menu User ---------------------------------------------------------------------------
        elif opcao == 5:
            print ("Novo Usuario")
            criar_usuario(usuarios)
        # Menu Listar ---------------------------------------------------------------------------
        elif opcao == 6:
            print ("Listar Contas")
            listar_contas(contas)
        # Menu Sair ------------------------------------------------------------------------------
        elif opcao == 7:
            print ("Obrigado por ser nosso cliente.")
            break
        # Prevenção de erro-----------------------------------------------------------------------
        else:
            print ("Opção Incorreta, tente de novo.")

main() # End-of-File (EOF).
