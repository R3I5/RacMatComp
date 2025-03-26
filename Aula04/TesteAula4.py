#Crie um programa em python que solicita ao usuário quatro números reais: a,b,c e d
#Em seguida, calcule o valor da expressão

a = float(input("Insira o valor de A:"))
b = float(input("Insira o valor de B:"))
c = float(input("Insira o valor de C:"))
d = float(input("Insira o valor de D:"))
F = (a**b+c)/((b*c)**(1/d)+d)
print(f"O valor da expressão é{F:.2f}")
