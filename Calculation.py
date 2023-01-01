import math as m


def calculation(op, n1, n2):
    if op == 1:
        print('O resultado de {} + {} = {}\n'.format(n1, n2, round(float(n1) + float(n2), 2)))

    elif op == 2:
        print('O resultado de {} - {} = {}\n'.format(n1, n2, round(float(n1) - float(n2), 2)))

    elif op == 3:
        print('O resultado de {} * {} = {}\n'.format(n1, n2, round(float(n1) * float(n2), 2)))

    elif op == 4:
        print('O resultado de {} / {} = {}\n'.format(n1, n2, round(float(n1) / float(n2), 2)))

    elif op == 5:
        print('O resultado da base {}  no expoente {} = {}\n'.format(n1, n2, round(m.pow(n1, n2), 2)))
       
    elif op == 6:
        print('O resultado do logaritmo de {} na base {} = {}\n'.format(n1, n2, round(m.log(n1, n2), 2)))

    elif op == 7:
        print('O resultado da raiz quadrada de {} = {}\n'.format(n1, round(m.sqrt(n1), 2)))

    elif op == 8:
        print('O seno de {}° = {}\n'.format(n1, round(m.sin(n1), 2)))

    elif op == 9:
        print('O cosseno de {}° = {}\n'.format(n1, round(m.cos(n1), 2)))

    elif op == 10:
        print('A tangente de {}° = {}\n'.format(n1, round(m.tan(n1), 2)))

    elif op == 11:
        print('O fatorial de {} = {}\n'.format(n1, round(m.factorial(n1), 2)))