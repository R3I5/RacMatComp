A = {2,3,5,8}
B = {3,4,5,6,9}
C = {1,6}

uniao = A | B
print("A união dos conjuntos fica:", uniao)

comum = A & B
print("Os valores comuns entre os conjuntos são:", comum)

separado = comum | C
print("A união entre os valores comuns de A e B e os valores de C é:", separado)

