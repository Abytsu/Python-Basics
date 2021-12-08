q='7'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
try:
    i=float(input('> Insira o valor de i (inteiro e positivo): '))
    q7_test=((i*2)%2)
    while i<0 or q7_test>0:
        q7_test=((i*2)%2)
        if i<0:
            i=float(input('\n> O valor de "i" não pode ser menor que 0. Por favor, insira outro valor.\n> '))
            q7_test=((i*2)%2)
        if q7_test>0:
            i=float(input('\n> A variável "i" não pode ser float, apenas int. Por favor, insira outro valor.\n> '))
            q7_test=((i*2)%2)
except:
    print('\n\n- Erro no sistema! -\n\nmotivo:\n- valor inserido não é int ou não foi reconhecido pelo programa.')
    exit(print('\n\tSaindo...\n'))
a=float(input('> Insira o valor de a (peso 2): '))
b=float(input('> Insira o valor de b (peso 3): '))
c=float(input('> Insira o valor de c (peso 4): '))
if i<=10:
    if i== 2 or i==4 or i==6 or i==8 or i== 10:
        media=(((a)+(b)+(c))/3)
    mediatipo='aritmética simples.'
    if i!= 2 and i!=4 and i!=6 and i!=8 and i!= 10:
        media='calculo não definido'
        mediatipo='indefinido - valor de "i" é impar.'
elif i>10:
    media=(((a*2)+(b*3)+(c*4))/(2+3+4))
    mediatipo='aritmética ponderada.'
print(f'\n- O resultado da média é: {media}\n- O tipo de média calculado foi: {mediatipo}\n- Valor da varíavel "i" inserido: {int(i)}\n')
