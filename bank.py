LIMITE_SAQUE_DIARIO = 3
LIMITE_VALOR_SAQUE = 500
saldo = 0
quantidade_saque = 0
extrato = '''
    =================
         Extrato
    =================

'''

def depositar():
    valor = float(input("Insira o valor do depósito: R$"))

    if valor <= 0: 
        print(f"ERRO: não é possível depositar valor igual a R${valor:.2f}")
        False
    else:
        global saldo 
        saldo += valor
        print(f"\n\nDepósito de R${valor:.2f} feito com sucesso!\n\n")
        extrato()

def sacar():
    global saldo
    global LIMITE_SAQUE_DIARIO
    global quantidade_saque

    valor = float(input("Insira o valor do saque: R$"))

    if valor > saldo:
        print(f"\n\nSaldo insuficiente!")
    else:        
        saldo -= valor
        quantidade_saque += 1

        if quantidade_saque == LIMITE_SAQUE_DIARIO:
            print(f"\n\nLimite de {LIMITE_SAQUE_DIARIO} saques excedidos. Tente novamente em 24 horas.") 
        elif valor > LIMITE_VALOR_SAQUE:
            print(f"\n\nVocê não pode efetuar um saque maior de R${LIMITE_VALOR_SAQUE:.2f}")
        else:
            print(f"\n\nSaque de R${valor:.2f} feito com sucesso!\n\n")
            extrato()

def extrato():
    global saldo
    global quantidade_saque

    extrato = f'''
=================
     EXTRATO
=================

Saldo disponível: R${saldo:.2f} 
Quantidade de saques disponíveis: {LIMITE_SAQUE_DIARIO - quantidade_saque}
'''
    print(extrato)

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
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        print("\n\nObrigado! E até mais :)")
        False
        break