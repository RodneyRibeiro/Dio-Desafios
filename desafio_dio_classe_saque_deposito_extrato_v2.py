"""Desafio DIO onde devemos modelar o sistema de conta bancária
    com saque, depósito e extrato..
"""

class Cliente():
    pass

class PessoaFisica(Cliente):
    pass

class Conta():
    def __init__(self,endereco):
        self.endereco =  endereco

class ContaCorrente(Conta):
    def __init__(self,endereco,cpf,numero_conta):
        super().__init__(endereco)
        self.cpf = cpf
        self.numero_conta = numero_conta

    def filtrar_usuario(self,cpf,usuarios):
        """Verifica a existência de usuários já cadastrados pelo CPF.
        Caso não exista, retorna lista vazia.
    
        Args:
            cpf (str): Número de identificação social brasileiro.
            usuarios (str): Nome do usuário do sistema.
    
        Returns:
            usuarios_filtrados(list): Lista retorna vazia caso não tenha usuários no sistema.
        """
        usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

class Historico():
    pass

class Transacao():
    pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

def menu():
    """Menu com opções da conta.
    """
    while True:
        menu()
        print("""
              [1] Criar Usuario
              [2] Criar Conta
              [3] Depósito
              [4] Saque
              [5] Listar Contas
              [0] Sair
        """)
        opcao = input("Seleciona opcao desejada: ")
        opcao = int(opcao)
    
        if opcao == 0:
            print("Saindo do Sistema...")
            break
        elif opcao == 1:
            break # FIXME: Criar classe Criar Usuario
        elif opcao == 2:
            break # FIXME: Criar classe Criar Conta
        elif opcao == 3:
            break # FIXME: Criar classe Depósito
        elif opcao == 4:
            break # FIXME: Criar classe Saque
        elif opcao == 5:
            break # FIXME: Criar classe Listar Contas


 # End-of-File (EOF).
