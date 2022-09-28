def trata_cpnj(c):

    c_teste = cnpj.split('.')
    c_teste = ''.join(c_teste)
    c_teste = c_teste.split('/')
    c_teste = ''.join(c_teste)
    c_teste = c_teste.split('-')
    c_teste = ''.join(c_teste)

    copia = list()
    lst = list()

    for num in c_teste:
        copia.append(int(num))
        lst.append(int(num))

    lst = lst[:-2]

    return lst, copia


def prim_digito(lista):

    lst = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    s = 0

    for c in range(12):
        s += lst[c] * lista[c]

    d = 11 - (s % 11)

    first_digit = 1 if d <= 9 else 0

    lista.append(first_digit)

    arr = lista

    return arr


def segund_digito(lista):
    lst = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    s = 0

    for c in range(13):
        s += lst[c] * lista[c]

    d = 11 - (s % 11)

    second_digit = 1 if d <= 9 else 0

    lista.append(second_digit)

    arr = lista

    return arr


cnpj = input("Digite seu CNPJ: ")
x, cnpj_passado = trata_cpnj(cnpj)
primeiro = prim_digito(x)
segundo = segund_digito(primeiro)

print(cnpj_passado)
print(segundo)

print('Válido') if (segundo == cnpj_passado) else print('Inválido')