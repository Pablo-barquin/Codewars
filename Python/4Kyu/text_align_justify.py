'''Modulo que contiene función de redondeo'''
from math import ceil


def justify(text, width):
    '''Función que realiza la justificación del texto'''
    solution = ''
    while text and len(text) > width:
        for break_line in range(width, -1, -1):
            if text[break_line] == ' ':
                break

        cut_line = text[:break_line]  # Corto la linea en la máxima cantidad de texto posible
        text = text[break_line + 1:]
        if len(cut_line) == width or len(cut_line.split()) == 1:
            solution += cut_line + '''\n'''  # La añadimos a la solución
            continue

        words = cut_line.split()    # Separo todas las palabras
        white_spaces = width - len(''.join(words))  # Obtengo cuantos espacios libres tengo que repartir
        gap = ceil(white_spaces / (len(words) - 1))  # Saco el máximo gap entre palabras

        space = gap * ' '
        if len(space.join(words)) == width:  # Si al añadir el gap a todas las palabras se ajusta al ancho
            solution += space.join(words) + '''\n'''  # La añadimos a la solución
            continue

        new_line = words.pop(0) # Creamos una nueva linea
        while words:
            new_line += gap * ' '   # Añadimos espacio original
            space = (gap-1) * ' '   # Creamos un espacio nuevo con 1 menos de ancho
            if len(new_line + space.join(words)) == width:
                new_line += space.join(words)   # Lo unimos todo en una nueva linea
                break
            new_line += words.pop(0)    # Si no, añadimos una palabra más manteniendo el espacio original

        solution += new_line + '''\n''' # Añadimos salto de linea

    solution += text.strip()
    return solution

if __name__ == '__main__':
    cadena = justify('123 45 6', 7)
    print(cadena)
