menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print ("\n========== DEPOSITO ==========")
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print (f"Saldo depositado com sucesso, no valor de R$ {valor:.2f}")
        else: 
            print ("Valor negaivo não é permitido! ")


    elif opcao == "s":
        print ("\n========== SAQUE ==========")
        saque = float(input("Digite o valor que deseja sacar: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você atingiu o limite de 3 saques diários.")
        elif saque > limite:
            print ("Operação falhou! O valor do saque excede o limite (R$ 500,00).")
        elif saque > saldo:
            print ("Operação falhou! Você não tem saldo suficiente.")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"


    elif opcao == "e":
        print ("\n========== EXTRATO ==========")
        if not extrato: 
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print("-" * 30)
            print(f"Saldo atual: R$ {saldo:.2f}")


    elif opcao == "q":
        print("Saindo do sistema. Obrigada!")
        break
    else:
        print ("Opção inválida, por favor selecione novamente a operação desejada: ")