menu = """
Bem-vindo ao seu sistema bancário.
Escolha uma opção:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor de depósito deve ser a partir de R$ 0.01")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Atenção! Saldo insuficientes.")

        elif excedeu_limite:
            print("Operação falhou! Limite indisponível.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não houveram movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("Certo, finalizando seu atendimento agora! Volte sempre que precisar!")
        break

    else:
        print("Opção inválida, por favor selecione a operação desejada.")