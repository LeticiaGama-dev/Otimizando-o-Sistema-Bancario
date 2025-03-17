print('-='*30)
print(F'{'BANCO DIO':^60}')
print('-='*30)
print('Bem-vindo ao Banco Dio.Selecione a opção desejada:')
menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
 """
saldo = 1800
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0

while True:

    opcao = input(menu).strip().upper()

    if opcao not in 'DSEQ':
        print('Opção inválida, selecione uma das opções do menu abaixo:')
       

    if opcao == 'D': #Depósito
        deposito = int(input('Digite o valor a ser depositado. R$:'))

        if deposito > 0:
            saldo += deposito
            extrato += f'Movimentação do tipo DEPÓSITO no valor de R${deposito:.2f}\n'
            print(f'O valor depositado nesta transação foi de R${deposito:.2f}')

    if opcao == 'Q': #Sair
        print('-'*60)
        print(f'{'Agradecemos por utilizar o Banco Dio. Até breve!':^60}')
        print('-' * 60)
        break

    if opcao == 'E': #Extrato
        print('-' * 30, 'EXTRATO', '-' * 30)
        print(f'{extrato:^70}')
        print(f'{extrato if extrato else 'Nenhuma movimentação realizada.':^70}')
        print('-' * 69)

    if opcao == 'S': #Saque
        saque = int(input('Digite o valor a ser sacado: R$'))

        if saque > limite:
            print('O valor é superior ao máximo permitido. Valor limite por saque = R$500.00')

        elif saque <= saldo and numero_saques <=3 and numero_saques < 3 :
            numero_saques +=1
            saldo -= saque
            extrato += f'Movimentação do tipo SAQUE no valor de R${saque:.2f},\n'
            print(f'O valor sacado nesta transação foi de R${saque:.2f}')
            print(f'O número de saques diário é de: {numero_saques}')

        if numero_saques > 3:
            print('Número de saques excedido!')

        elif numero_saques == 3:
            print('Limite diário de 03 saques atingido!')

        elif saque > saldo:
            print('Saldo insuficiente!')






