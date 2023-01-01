import statistics as s


def cal_mmm(listaNumeros, op):
    if op == 12:
        # retorna a média dos números na lista
        avg = s.mean(listaNumeros)

        print('A média dos números informados é {}\n'.format(round(avg, 2)))

    elif op == 13:
        # retorna a moda
        mod = s.mode(listaNumeros)

        print('A moda dos números informados é {}\n'.format(round(mod, 2)))

    elif op == 14:
        # retorna a mediana
        med = s.median(listaNumeros)

        print('A mediana dos números informados é {}\n'.format(round(med, 2)))

        