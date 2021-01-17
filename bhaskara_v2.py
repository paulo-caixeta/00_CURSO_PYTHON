import math

def delta(a, b, c):
        return b**2 - 4 * a * c

def main():
        a_digitado = float(input("Digite o valor de a: "))
        b_digitado = float(input("Digite o valor de b: "))
        c_digitado = float(input("Digite o valor de c: "))
        imprime_raizes(a_digitado, b_digitado, c_digitado)

def imprime_raizes(a, b, c):
        d = delta(a, b, c)

        if (d == 0):
                x= -b/(2*a)
                print ("a raiz desta equação é ", x)

        else:
                if (d < 0):
                        print ("esta equação não possui raízes reais")

                else:
                        x1= (-b + math.sqrt(d))/(2*a)
                        x2= (-b - math.sqrt(d))/(2*a)
                        print ("as raízes da equação são",x1, "e", x2)
