def piramide(n):
    if n == 0:
        return
    piramide(n-1)
    print('*' * n)

piramide(5)
