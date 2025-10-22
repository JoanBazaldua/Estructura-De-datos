from typing import List

def maximo(lst: List[int]) -> int:
    """
    Devuelve el máximo de una lista no vacía recursivamente.
    Precondición: len(lst) >= 1
    """
    if not lst:
        raise ValueError("maximo: la lista no debe estar vacía")
    if len(lst) == 1:
        return lst[0]
    
    max_resto = maximo(lst[1:])
    return lst[0] if lst[0] >= max_resto else max_resto


# Pruebas
assert maximo([3]) == 3
assert maximo([3, 10, -2, 7]) == 10
assert maximo([-5, -1, -9]) == -1
