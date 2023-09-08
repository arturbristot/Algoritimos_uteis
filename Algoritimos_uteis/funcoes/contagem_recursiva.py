def regressiva(n):
    if n < 1:
        return
    else:
        print(n)
        regressiva(n-1)

print(regressiva(19))