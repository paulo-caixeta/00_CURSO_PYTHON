import math

x1 = float(input("Insira a coordenada x1: "))
y1 = float(input("Insira a coordenada y1: "))
x2 = float(input("Insira a coordenada x2: "))
y2 = float(input("Insira a coordenada y2: "))

dist_xy = math.sqrt((x2-x1)**2+(y2-y1)**2)

print ("A distância entre os dois pontos é de: ", dist_xy,"un. Logo, é considerado:")

if (dist_xy >= 10):
	print ("longe")

else:
	print ("perto")


