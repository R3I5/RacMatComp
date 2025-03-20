backend = {"Python", "Java", "C#", "Ruby"}
frontend = {"JavaScript", "TypeScript", "Python", "HTML", "CSS"}

todas = backend | frontend  #o operador | serve para unir os dois conjuntos, ele não garante uma ordem na saída
print("Todas as linguagens:", todas)

comum = backend & frontend #o operador & serve para retornar um valor verdadeiro do que está presente nos dois sets
print("Linguagens usadas nos dois:", comum)

exclusivo_backend = backend - frontend #o operador - serve para mostrar o que esta presente em apenas um set
print("Linguagens apenas do backend", exclusivo_backend)