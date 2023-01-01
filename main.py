from Calculation import calculation
from Calculation_mmm import cal_mmm
import os

print("""1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão""")
print("""5. Potência\n6. Logaritmo\n7. Raiz quadrada""")
print("""8. Seno\n9. Cosseno\n10. Tangente\n11. Fatorial""")
print("""12. Média\n13. Moda\n14. Mediana\n0. Sair""")
op = int(input('Informe a operação desejada: '))

if op == 0:
    print("Muito obrigado! Volte sempre! <3")

listNum = []

while op != 0:
    if op not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
        print('Oops! Operando inexistente. Tente novamente.')
    try:
        
        if op == 5:
            n1 = float(input('Informe a base: '))
            n2 = float(input('Informe o expoente: '))
            os.system('clear')
            calculation(op, n1, n2)
            
        elif op == 6:
            n1 = float(input('Informe o logaritmando: '))
            n2 = float(input('Informe a base: '))
            os.system('clear')
            calculation(op, n1, n2)

        elif op == 7:
            n1 = float(input('Informe o número: '))
            os.system('clear')
            calculation(op, n1, 2)

        elif op == 8:
            n1 = float(input('Informe o número: '))
            os.system('clear')
            calculation(op, n1, 0)

        elif op == 9:
            n1 = float(input('Informe o número: '))
            os.system('clear')
            calculation(op, n1, 0)

        elif op == 10:
            n1 = float(input('Informe o número: '))
            os.system('clear')
            calculation(op, n1, 0)

        elif op == 11:
            n1 = float(input('Informe o número: '))
            os.system('clear')
            calculation(op, n1, 0)

        elif op == 12:
            qtd = int(input('Informe quantos números serão inseridos: '))
            print('Informe os números: ')

            for i in range(0, qtd):
                n = float(input('{}º: '.format(i + 1)))
                listNum.append(n)

            os.system('clear')
            cal_mmm(listNum, op)

        elif op == 13:
            qtd = int(input('Informe quantos números serão inseridos: '))
            print('Informe os números: ')

            for i in range(0, qtd):
                n = float(input('{}º: '.format(i + 1)))
                listNum.append(n)

            os.system('clear')
            cal_mmm(listNum, op)

        elif op == 14:
            qtd = int(input('Informe quantos números serão inseridos: '))
            print('Informe os números: ')

            for i in range(0, qtd):
                n = float(input('{}º: '.format(i + 1)))
                listNum.append(n)

            os.system('clear')
            cal_mmm(listNum, op)

        else:
            n1 = float(input('Informe o primeiro número: '))
            n2 = float(input('Informe o segundo número: '))
            os.system('clear')
            calculation(op, n1, n2)
                
    except:           
        print("Não é possível efetuar a operação. Número não fornecido ou número zero inserido no divisor.")

    print("""1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão""")
    print("""5. Potência\n6. Logaritmo\n7. Raiz quadrada""")
    print("""8. Seno\n9. Cosseno\n10. Tangente\n11. Fatorial""")
    print("""12. Média\n13. Moda\n14. Mediana\n0. Sair""")
    op = int(input('Informe a operação desejada: '))

    if op == 0:
        print("Muito obrigado! Volte sempre! <3")