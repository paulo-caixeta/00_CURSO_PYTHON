largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = 1
y = 1
while y <= altura:
        while x <= largura:
                if y == 1 or y == altura:
                        print("#",end = "")
                else:
                        if x == 1 or x == largura:
                                print("#",end = "")
                        else:
                                print(" ",end = "")
                x = x + 1
        y = y + 1
        print()
        x = 1
