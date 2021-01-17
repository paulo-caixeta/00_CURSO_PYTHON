def primo (x):
    i = 2
    eh_primo = True
    while i < x and eh_primo != False:
        if x % i != 0:
            i = i + 1
        else:
            eh_primo = False       
    if eh_primo == True:
        return eh_primo
    else:
        print(eh_primo)
