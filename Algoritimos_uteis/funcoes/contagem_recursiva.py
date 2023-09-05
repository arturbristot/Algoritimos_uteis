def regressiva(n):
    if n < 1:
        return
    else:
        print(n)
        n = n-1
        regressiva(n)