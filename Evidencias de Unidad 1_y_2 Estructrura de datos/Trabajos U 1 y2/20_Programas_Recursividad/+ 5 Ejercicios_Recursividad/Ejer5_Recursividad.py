from typing import List, Union

Anidado = List[Union[int, "Anidado"]]

def aplanar(x: Anidado) -> List[int]:
    """
    Aplana una lista potencialmente anidada de enteros,
    preservando el orden.
    Ejemplo: [1, [2, [3, 4], 5], [], 6] -> [1, 2, 3, 4, 5, 6]
    """
    if not x:
        return []
    
    cabeza, resto = x[0], x[1:]
    if isinstance(cabeza, int):
        return [cabeza] + aplanar(resto)
    return aplanar(cabeza) + aplanar(resto)


# Pruebas
# termina en el caso base
assert aplanar([]) == []
assert aplanar([1, 2, 3]) == [1, 2, 3]
assert aplanar([1, [2, [3, 4], 5], [], 6]) == [1, 2, 3, 4, 5, 6]

#Pacheco Bazaldua Carlos Joan