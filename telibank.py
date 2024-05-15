menu = """
============== TELI BANK ==============
|    Selecione a operação desejada:   |
|                                     |
|          [D] - Depositar            |
|          [S] - Sacar                |
|          [E] - Extrato              |
|          [Q] - Sair                 |
|                                     |
=======================================
"""

saldo = 0
extrato = ""
n_saques = 0

LIM_POR_SAQUE = 500
LIM_SAQUES_DIARIOS = 3

while True:
    opcao = input(menu)
    
    if opcao.lower() == "d":
        print("\nVocê selecionou a opção \"Depósito!\"")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo+=valor
            extrato+=f"|   Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação mal sucedida! O valor informado é inválido.")
    elif opcao.lower() == "s":
        print("\nVocê selecionou a opção \"Saque!\"")
        if n_saques >= 3:
            print("Operação mal sucedida! Limite diário de saques excedido.\nPara mais informações verifique o extrato.")
        else:
            valor = float(input("Informe o valor do saque: "))
            if valor > LIM_POR_SAQUE:
                print("Operação falhou! O valor informado supera o limite máximo por saque.")
            elif valor > saldo:
                print("Operação falhou! Saldo insuficiente.")
            else:
                saldo-=valor
                n_saques+=1
                extrato+=f"|   Saque: R$ {valor:.2f}\n"
    elif opcao.lower() == "e":
        print("\n============== EXTRATO ==============")
        print("|   Não foram realizadas movimentações." if not extrato else extrato)
        print(f"|   Saldo: R$ {saldo:.2f}")
        print("=====================================")
    elif opcao.lower() == "q":
        print("\nObrigado por ser nosso cliente! TeliBank agradece.\n\n")
        break
    else:
        print("\nOperação inválida, por favor selecione uma das opções mostradas no menu.")