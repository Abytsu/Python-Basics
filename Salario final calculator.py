print('Welcome to Salário Final Calculator!')
nome=str(input("\nInsira o nome do vendedor aqui:"))
sal=int(input("Insira o salário em Reais aqui:"))
ven=int(input("Insira o número de vendas aqui:"))
fin=(sal+ven*0.15)
print(f"\nNome do vendedor: {nome}\nSalário base: {sal} R$\nTotal de vendas/mês: {ven}\nSalário final: {fin} R$")
print('\n# # # #')

