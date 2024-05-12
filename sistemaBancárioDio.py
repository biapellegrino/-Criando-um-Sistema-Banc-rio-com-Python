mensageminicial = f""" 
====================================
Seja bem-vindo(a) ao Banco 24h!

Qual operação gostaria de realizar?

1. Saque
2. Depósito
3. Visualização de status
4. Sair

====================================
"""
saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
limite_saques = 5

while True:

    print(mensageminicial)
    opcao = int(input())

    if opcao == 2:
        mensagemsaldo = """ 
        ====================================
        Seja bem-vindo(a) ao Depósito!

        O que você deseja?

        1. Depositar na conta.
        2. Sair do depósito.

        ====================================
        """
        while True:
            op1 = input(mensagemsaldo)

            if op1 == 1:
                valor = float(input("Informe o valor do depósito: "))
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f}\n"
                    break  # Sai do loop enquanto a opção é válida
                else:
                    print("Operação falhou! O valor informado é inválido.")
            elif op1 == 2:
                break  # Sai do loop
            else:
                print("Operação falhou! O valor informado é inválido.")


    elif opcao == 1:
            mensagemsaque = f""" 
            ====================================
            Seja bem-vindo(a) ao Saque!

            O que você deseja?

            1. Sacar da conta.
            2. Sair do saque.

            ====================================
            """
            while True:
                op2 = int(input(mensagemsaque))
                if op2 == 1:
                    valor = float(input("Informe o valor do saque: "))
                    excedeu_saldo = valor > saldo
                    excedeu_limite = valor > limite
                    excedeu_saques = numero_saques >= limite_saques

                    if excedeu_saldo:
                        print("Você não tem saldo suficiente.")
                    elif excedeu_limite:
                        print("O valor do saque excede o limite.")
                    elif excedeu_saques:
                        print("Número máximo de saques excedido.")
                    elif valor > 0:
                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f}\n"
                        numero_saques += 1
                        break
                    else:
                        print("Operação inválida, por favor selecione uma opção válida")
                elif op2 == 2:
                    break  # Sai do loop
                else:
                    print("Operação falhou! O valor informado é inválido.")


    elif opcao == 3:
         while True:
            mensagemextrato = f""" 
                ====================================
                Seja bem-vindo(a) ao Extrato!

                O que você deseja?

                1. Visualizar extrato da conta.
                2. Sair do extrato.

                ====================================
                """
            op3 = int(input(mensagemextrato))
            if op3 == 1:
                print("\n================ EXTRATO ================")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================\n")
            elif op3 == 2:
                break 
            else:
                print("Operação falhou! O valor informado é inválido.")


    elif opcao == 4:
        break
    else:
        print("Operação inválida, por favor tente novamente.")
