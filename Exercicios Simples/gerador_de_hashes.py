"""Gerar Hashes com Python
"""
import hashlib

string = input('Digite o texto a ser gerado a hash: ')

opcao = input('''ESCOLHA O TIPO DE HASH

              1) MD5
              2) SHA1
              3) SHA256
              4) SHA512
              Digite o número do hash a ser gerado:
'''
)
opcao = int(opcao)
def menu():
    """Menu criado para selecionar qual hash a ser utilizado
    """
    if opcao == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print('O hash da string é: ', resultado.hexdigest())
    elif opcao == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print('O hash da string é: ', resultado.hexdigest())
    elif opcao == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print('O hash da string é: ', resultado.hexdigest())
    elif opcao == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print('O hash da string é: ', resultado.hexdigest())
    else:
        print('Opção Inválida')
        menu()

menu()

# End of File (EOF)
