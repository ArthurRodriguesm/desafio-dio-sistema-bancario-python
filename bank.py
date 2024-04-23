LIMITE_SAQUE_DIARIO = 3
LIMITE_VALOR_SAQUE = 500
saldo = 0
quantidade_saque = 0
extrato = '''
    =================
         Extrato
    =================

'''

def depositar(saldo, extrato):
    valor = float(input("Insira o valor do depósito: R$"))

    if valor <= 0:
        print("Erro")
        False
    else:
        saldo += valor
        print(f"Depósito de R${valor:.2f} feito com sucesso!\n")
    print(f"{extrato} Saldo: R${saldo:.2f}")

def sacar():
    valor = float(input("Insira o valor do depósito: R$"))
    

menu = '''
    ==============
         MENU
    ==============
    [1] - Depositar
    [2] - Sacar
    [3] - Exibir Extrato
    [4] - Sair

    Digite o número da operação desejada:'''


while True:
    opcao = int(input(menu))

    if opcao == 1:
        depositar(saldo, extrato)
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        print("Obrigado! E até mais :)")
        False
        break