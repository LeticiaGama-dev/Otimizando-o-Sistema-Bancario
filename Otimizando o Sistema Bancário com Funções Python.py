def depositar(saldo,extrato):
    deposito = int(input('Digite o valor a ser depositado: R$ '))
    if deposito >0:
        saldo+= deposito
        extrato += f'Movimento do tipo DEPÓSITO no valor de R$ {deposito:.2f}\n'
        print(f'O valor depositado nesta transação foi de R${deposito:.2f}')
    return saldo,extrato

def sacar(saldo, extrato, numero_saques,limite,LIMITE_SAQUES):
    saque = int(input('Digite o valor a ser sacado: R$ '))

    if saque > limite :
        print('O valor é superior ao máximo permitido.Valor limite por saque = R$ 500,00')

    elif saque > saldo:
        print('Saldo insuficiente!')

    elif numero_saques > LIMITE_SAQUES:
        print('Número de saques excedido! Limite diário, 3 saques!')

    elif numero_saques == LIMITE_SAQUES:
        print('ATENÇÃO: Número de saques diários atingidos!')

    else:
        saldo-= saque
        extrato += f'Movimentação do tipo SAQUE no valor de R${saque:.2f}\n'
        numero_saques += 1
        print(f'O valor sacado nesta transação foi de R${saque:.2f}')

    return saldo, extrato, numero_saques

def exibir_extrato(extrato):
    print('-' * 30, 'EXTRATO', '-' * 30)
    print(f'{extrato:^70}')
    print(f'{extrato if extrato else 'Nenhuma movimentação realizada.':^70}')
    print('-' * 69)


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

#definição das variáveis 
saldo = 1800
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0

while True:

    opcao = input(menu).strip().upper()

    if opcao == 'D': #Depósito
        saldo, extrato = depositar(saldo,extrato)
           
    elif opcao == 'E': #Extrato
       # print('-' * 30, 'EXTRATO', '-' * 30)
        #print(f'{extrato:^70}')
        #print('-' * 69)
        print(extrato)
    else:
        print(f'{extrato if extrato else 'Nenhuma movimentação realizada.':^70}')

    elif opcao == 'S': #Saque
        saldo,extrato,numero_saques = sacar(saldo,extrato,numero_saques,limite,LIMITE_SAQUES)

    elif opcao == 'Q': #Sair
        print('-'*60)
        print(f'{'Agradecemos por utilizar o Banco Dio. Até breve!':^60}')
        print('-' * 60)
        break
    
    else:
        print('Opção inválida, selecione uma das opções do menu abaixo:')

        
    
    
    
         


