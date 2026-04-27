saldo = 200

while True:
    saque = float(input("Digite o valor do saque: "))

    if saque <= 0:
        print("Digite um valor válido.")
    elif saque <= saldo:
        print("Saque autorizado!")
        saldo -= saque
        print("Saldo restante:", saldo)
    else:
        print("Saque negado, saldo insuficiente.")

    if saldo == 0:
        print("Saldo zerado. Encerrando sistema.")
        break
