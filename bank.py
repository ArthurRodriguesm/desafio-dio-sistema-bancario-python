def deposito(valor):
    print(f"Depósito de R$ {valor} feito com sucesso!")
    
def saque(valor):
    print(f"Saque de R$ {valor} feito com sucesso!")

def MENU():
    print('''
    ============
        MENU
    ============
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato Bancário
''')
    
    opcao = int(input("Digite o número da operação desejada: "))

    if opcao is 1:
        valor = float(input("Digite o valor que deseja depositar: "))
        deposito(valor)
    elif opcao is 2:
        valor = float(input("Digite o valor que deseja sacar: "))
        saque(valor)

MENU()