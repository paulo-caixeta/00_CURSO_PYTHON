def fatorial (n):
    n_fatorial = 1
    i = 0
    pi = 1
    while i < n:
            pi = (n - i)
            i = i + 1
            n_fatorial = n_fatorial * pi
    return n_fatorial
print (n_fatorial)
