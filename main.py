import math


def run():
    options = '''
    Selecciona una opción a calcular:
        1. Valor Futuro
        2. Valor presente
        3. Interés del periodo
        4. Total de periodos
     :
    '''
    user_option = int(input(options))
    message_vp = 'Cual es el valor presente?: '
    message_vf = 'Cual es el valor futuro?: '
    message_i = 'De cuando son los intereses?:  '
    message_n = 'Por cuantos periodos?: '

    if user_option == 1:
        vp = int(input(message_vp))
        i = float(input(message_i))
        n = int(input(message_n))
        operations(formula='Valor Futuro', vp=vp, i=i, n=n)

    elif user_option == 2:
        vf = float(input(message_vf))
        i = float(input(message_i))
        n = int(input(message_n))
        operations(formula='Valor presente', vf=vf, i=i, n=n)

    elif user_option == 3:
        n = int(input(message_n))
        vp = int(input(message_vp))
        vf = float(input(message_vf))
        operations(formula='Interés del periodo', vp=vp, vf=vf, n=n)

    elif user_option == 4:
        i = float(input(message_i))
        vp = int(input(message_vp))
        vf = float(input(message_vf))
        operations(formula='Total de periodos', vp=vp, vf=vf, i=i)


def operations(formula,
               vp: float = None,
               vf: float = None,
               i: float = None,
               n: int = None):
    result = None
    if formula == 'Valor Futuro':
        result = round(vp * (1 + i) ** n, 2)
    elif formula == 'Valor presente':
        result = round(vf / (1 + i) ** n)
    elif formula == 'Interés del periodo':
        result = round(pow(vf / vp, 1 / n) - 1, 2)
    elif formula == 'Total de periodos':
        result = round(math.log(vf / vp) / math.log(1 + i))

    return print(f'{formula}: {result}')


if __name__ == '__main__':
    run()
