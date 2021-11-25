bank=('Stellaris')
namec=str(input(f'''Seja bem-vindo(a) ao Banco {bank}.\n\n>Cadastro...\n\nInsira um nome para a conta.
(nota: será usado em transferências e para o acesso ao sistema!)\nCadastro: '''))

passwordc=float(input(f'''\n>Nome de usuário definido. ({namec})\n-Por favor, defina uma senha para sua conta
(nota: somente números!)\nSenha: '''))
print(f'\n\t> Cadastro concluído! Espero que curta nossos serviços, {namec}!')
e="\nSistema desligando...\n"

name=input('\n- Bem-vindo ao sistema! -\n\t> Por favor, para fazer o log-in entre com seu nome: ')
if name !=namec:
    print(f'\n> Usuário "{name}" não encontrado!\nPor favor reinicie o sistema e tente novamente.')
    exit(print(e))
password=float(input(f'\nBem-vindo, {name}!\n\t\t> Digite sua senha: '))
if password != passwordc:
    print('\nSenha incorreta! Reinicie o sistema e tente novamente.')
    exit(print(e))
else:
    print('Entrada concluida!.')
print('\n\t - Seus dados bancários -')
# Dados
conta=20543
taxa=0.07
rend=0.005
print(f'''\n>Saldo total: {conta} R$\n>Rendimento após um mês: {rend*conta} R$
>Rendimento após um mês + Saldo: {conta+(conta*rend)} R$''')
print('\n# Deseja fazer uma transferência de contas?')

conf=str(input('Digite: s ou n\n'))
if conf=='n':
    print('\nOperação cancelada!')
    exit(print(e))
elif conf !='s':
    print('Sistema só reconhece "s" ou "n", qual foi >:(.')
    exit(print(e))
else:
    print('\n - Operação confirmada! - ')
rec=str(input('+ Insira o nome da conta destino: '))
if rec==name:
    print("Você não pode transferir dinheiro pra si mesmo '-' ")
    exit(print(e))
val=float(input(f'\n- Usuário {rec} encontrado!\n+ Por favor, insira a quantia desejada à transferir.\n\tQuantidade: '))
if val>conta:
    print(f'\nO valor especificado é maior do que sua conta possui atualmente.\nReinicie o sistema e tente novamente.')
    exit(print(e))
else:
    print(f'\n\n> Transferência de {val} para a conta {rec} concluída!\nO usuário recebeu {val-(val*taxa)} R$\nTaxa: 07%')
print(f'''\n>Saldo atual: {conta-val} R$\n>Rendimento após um mês: {rend*(conta-val)} R$
>Rendimento após um mês + Saldo: {(conta-val)+((conta-val)*rend)} R$''')
print('\n\nSaindo da conta...')