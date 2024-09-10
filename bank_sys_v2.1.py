def check_in():
    check_in = """
        Você deseja abrir uma conta com agente?
        [1] Sim
        [2] Não
    => """
    return input(check_in)

# Opções do menu principal
def menu():
    menu = """
        Bem-vindo ao PyBank!
        Escolha uma opção pelo número:
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Abrir nova conta
        [5] Ver minhas contas
        [6] Sair
    => """
    return input(menu)

#Função de criação de cadastro e da conta inicial
def criar_cliente(clientes):

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    clientes.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf" : cpf, "endereco" : endereco})
    print("Usuário cadastrado com sucesso, já vamos abrir sua conta também")
    print("Acesse a opção 4 do menu principal.")
    main()

#Gerador de dados da conta
def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Confirme o CPF para abertura da conta:")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("Conta criada com sucesso!")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "cliente" : cliente}
        
    print("Cadastro de cliente não encontrado, fluxo de criação da conta encerrado.")

#Opção de depósito 
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("O valor de depósito deve ser a partir de R$ 0.01")
    return saldo, extrato

#Opção de saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Atenção! Saldo insuficiente.")

    elif excedeu_limite:
        print("Operação falhou! Limite indisponível.")

    elif excedeu_saques:
        print("Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor informado é inválido.")
    return saldo, extrato

#Opção de extrato
def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não houveram movimentações recentes." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#Validação de dados cliente
def filtrar_cliente(cpf,clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Listar contas que cliente possui
def listar_conta(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['cliente']['nome']}
        """
        print("=" * 100)
        print(linha)

# Operação do menu de conta
def main():
    #Constantes
    LIMITE_SAQUES = 3
    AGENCIA= "0001"
    
    #Variáveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []
    

    #Loop relacionado às opções de menu e retornos
    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)    

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_conta(contas)
        
        elif opcao == "6":
            print("Certo, finalizando seu atendimento agora! Volte sempre que precisar!")
            break

        else:
            print("Opção inválida, por favor selecione a operação desejada.")

#Operação do menu de check-in
def validar():
    #Variáveis
    clientes = []
    cpf = input("Bem-vindo ao PyBank! Antes de iniciar, informe o número do cpf, sem pontuação: ")
    cliente = filtrar_cliente(cpf, clientes)

    #Validar se cliente está no cadastro
    if cliente:
        main()
    else:
        print("Não temos registro desse CPF cadastrado.")
        while True:
            opcao = check_in()
            if opcao == "1":
                print("Certo, então vamos criar seu cadastro.")
                criar_cliente(clientes)
            elif opcao == "2":
                print("Entendido, neste caso, estou encerrando o atendimento")
                print("Volte sempre!")
                break       
            else:
                print("Opção inválida, por favor selecione a operação desejada.")
        
validar()

