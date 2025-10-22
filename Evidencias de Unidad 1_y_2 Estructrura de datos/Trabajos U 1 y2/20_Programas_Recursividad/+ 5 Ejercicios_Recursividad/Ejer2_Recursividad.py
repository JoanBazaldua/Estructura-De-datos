from typing import Dict

def fibo(n: int) -> int:
    """
    Regresa el n-ésimo número de Fibonacci (0-index)
    recursivamente (versión simple).
    Precondición: n >= 0
    Nota: Esta versión es exponencial; se incluye por claridad teórica.
    """
    if n < 0:
        raise ValueError("fibo: n debe ser >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibo_memo(n: int, memo: Dict[int, int] | None = None) -> int:
    """
    Fibonacci recursivo con memoización (O(n)).
    """
    if n < 0:
        raise ValueError("fibo_memo: n debe ser >= 0")
    if memo is None:
        memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]


# Pruebas
assert fibo(0) == 0
assert fibo(1) == 1
assert fibo(7) == 13

assert fibo_memo(0) == 0
assert fibo_memo(1) == 1
assert fibo_memo(30) == 832040
