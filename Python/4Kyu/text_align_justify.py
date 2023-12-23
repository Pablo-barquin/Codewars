'''Modulo que contiene función de redondeo'''
from math import ceil


def justify(text, width):
    '''Función que realiza la justificación del texto'''
    print(text, width)
    sol = ''
    while text and len(text) > width:
        adj = 0
        for adj in range(width, -1, -1):
            if text[adj] == ' ':
                break
        if adj == width:
            sol += text[:adj] + '''\n'''
            text = text[adj:]
            continue
        old_line = text[:adj+1]
        text = text[adj+1:]
        words = old_line.strip().split()
        start, end = words[0], words[-1]
        if start == end:
            sol += start + '''\n'''
            continue
        characters = len(''.join(words))
        white_spaces = width - characters
        if white_spaces:
            fill = ceil(white_spaces / (len(words) - 1))
        else:
            fill = 1
        if len(words) <= 2:
            sol += start + (fill) * ' ' + end + '''\n'''
        else:
            for word in words[1:-1]:
                start += fill * ' ' + word
            sol += start + (fill-1) * ' ' + end + '''\n'''
    sol += text
    return sol

if __name__ == '__main__':
    cadena = justify('123 45 6', 7)
    print(cadena)
