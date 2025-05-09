""""Desafio DIO onde devemos modelar o sistema de conta bancária com saque, depósito e extrato.
Não associei a conta ao usuário, irei fazer em versões posteriores.
"""

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

class PessoaFisica(Cliente):
    def __init__(self, endereco):
        super().__init__(endereco)

    def criar_usuario(self, usuarios):
        """Cria conta no banco com usuário digitado
        
        Args:
            usuarios (list): Lista de usuários do sistema
        """
        cpf = input("Informe o CPF do novo usuário(somente números):")
        usuario = self.filtrar_usuario(cpf, usuarios)
        
        if usuario:
            print("\nJá existe usuário com este CPF!")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        
        print("+++ Usuário criado com sucesso! +++")

    def filtrar_usuario(self, cpf, usuarios):
        """Verifica a existência de usuários já cadastrados pelo CPF. Caso não exista, retorna None.
        
        Args:
            cpf (str): Número de identificação social brasileiro.
            usuarios (list): Lista de usuários do sistema.
        
        Returns:
            dict or None: Usuário encontrado ou None se não encontrar.
        """
        usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

class Conta:
    def __init__(self, endereco):
        self.endereco = endereco

class ContaCorrente(Conta):
    def __init__(self, endereco, cpf, numero_conta):
        super().__init__(endereco)
        self.cpf = cpf
        self.numero_conta = numero_conta

    def criar_conta(self, agencia, numero_conta, usuarios):
        """Cria conta após verificação da ausência de usuário com o CPF citado.
        
        Args:
            agencia (int): Agência 0001 com valor constante.
            numero_conta (int): Valor gerado automaticamente, contando valores em lista.
            usuarios (list): Lista de usuários cadastrados na função criar_usuario.
        
        Returns:
            dict or None: Conta criada ou None se o usuário não for encontrado.
        """
        cpf = input("Digite o CPF do usuário: ")
        usuario = PessoaFisica("").filtrar_usuario(cpf, usuarios)
        
        if usuario:
            print("Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
        print("Usuário não encontrado, sistema será encerrado!")
        return None

    @staticmethod
    def listar_contas(contas):
        """Lista as contas cadastradas
        
        Args:
            contas (list): Lista com contas cadastradas.
        """
        for conta in contas:
            texto = f"""
                 Agência: \t{conta["agencia"]}
                 Conta: \t{conta["numero_conta"]}
                 Titular: \t{conta["usuario"]["nome"]}
            """
            print(texto)

class Historico:
    @staticmethod
    def emitir_extrato(saldo, /, *, extrato):
        """Exibe extrato sobre depósitos e saques da conta.
        
        Args:
            saldo (float): Saldo da conta.
            extrato (list): Lista com extrato de depósitos e saques.
        """
        print("Seu Saldo é de: ", saldo, " Extrato: ", extrato)

class Transacao:
    pass

class Deposito(Transacao):
    @staticmethod
    def depositar(saldo, deposito, extrato, /):
        """Função para depositar valor em conta.
        
        Args:
            saldo (float): Saldo da conta
            deposito (float): Valor a ser depositado
            extrato (list): Lista com extrato de depósitos e saques
        
        Returns:
            tuple: Novo saldo e extrato atualizado
        """
        saldo += deposito
        extrato.append(f"Deposito: R${deposito} Saldo: R${saldo}")
        print(f"Seu saldo é de R${saldo}.")
        
        return saldo, extrato

class Saque(Transacao):
    @staticmethod
    def sacar(*, saldo, saque, extrato, saques_total=3):
        """Função para saque de valor do saldo em conta.
        
        Args:
            saldo (float): Saldo da conta.
            saque (float): Valor do saque que será debitado da conta.
            extrato (list): Lista com extrato de depósitos e saques.
            saques_total (int): Limite total de saques.
        
        Returns:
            tuple: Novo saldo, extrato atualizado e total de saques restante
        """
        
        saldo -= saque
        saques_total -= 1
        extrato.append(f"Saque: R${saque} Saldo: R${saldo}")
        print(f"Seu saldo é de R${saldo} e ainda possui {saques_total} saques hoje.")
        
        return saldo, extrato, saques_total

def menu():
    """Exibe Menu para saque."""
    print("""
            [1] Saque
            [2] Deposito
            [3] Extrato
            [4] Criar Conta
            [5] Novo Usuário
            [6] Listar Contas
            [7] Sair
    """)
    return int(input("Selecione uma opção: "))

# Menu Saque ---------------------------------------------------------------------------
def main():
    """Função com as ações principais, chama as outras funções."""
    # Variáveis
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    saldo = 0.0
    extrato = []
    saques_total = 3

    while True:
        opcao = menu()
        if opcao == 1:
            print("Saque")
            print("Digite o Valor para Saque:")
            # Round para garantir que o saldo tenha 2 dígitos após a vírgula
            saque = round(float(input()), 2)
            # Prevenção de valores negativos
            if saque < 0:
                print("Valor digitado é inválido. Digite um valor positivo")
            # Limite de saque 500
            elif saque > 500:
                print("Valor de saque excede o máximo permitido (500).")
            # Testar se não há saldo
            elif saque > saldo and saques_total > 0:
                print("Não há saldo suficiente.")
            # Condição que o saque seja menor que o saldo e que esteja dentro dos 3 saques disponíveis
            elif saque <= saldo and saques_total > 0:
                saldo, extrato, saques_total = Saque.sacar(
                    saldo=saldo,
                    saque=saque,
                    extrato=extrato,
                    saques_total=saques_total
                )
            elif saques_total == 0:
                print("Limite de Saques Atingido.")
        # Menu Depósito --------------------------------------------------------------------------
        elif opcao == 2:
            print("Depósito")
            print("Digite o Valor para Depósito:")
            # Round para garantir que o saldo tenha 2 dígitos após a vírgula
            deposito = round(float(input()), 2)
            # Prevenção de valores negativos ou igual a 0
            if deposito <= 0:
                print("Valor digitado é inválido. Digite um valor positivo")
            else:
                saldo, extrato = Deposito.depositar(saldo, deposito, extrato)
        # Menu Extrato ---------------------------------------------------------------------------
        elif opcao == 3:
            Historico.emitir_extrato(saldo, extrato=extrato)
        # Menu Conta ---------------------------------------------------------------------------
        elif opcao == 4:
            print("Criar Conta")
            numero_conta = len(contas) + 1
            conta = ContaCorrente("", "", numero_conta).criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        # Menu Usuário ---------------------------------------------------------------------------
        elif opcao == 5:
            print("Novo Usuário")
            PessoaFisica("").criar_usuario(usuarios)
        # Menu Listar ---------------------------------------------------------------------------
        elif opcao == 6:
            print("Listar Contas")
            ContaCorrente.listar_contas(contas)
        # Menu Sair ------------------------------------------------------------------------------
        elif opcao == 7:
            print("Obrigado por ser nosso cliente.")
            break
        # Prevenção de erro-----------------------------------------------------------------------
        else:
            print("Opção Incorreta, tente de novo.")

main()
