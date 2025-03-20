versao1 = {"login","registro","perfil","mensagens","notificações","relatórios"}
versao2 = {"login","registro","perfil","pagamentos","notificações","ajuda","relatórios","backup"}

exclusiva1 = len(versao1 - versao2)
exclusiva2 = len(versao2 - versao1)
compartilhadas = len(versao1 & versao2)

print("Numero de funcionalidades exclusivas da versão 1:",exclusiva1)
print("Numero de funcinoalidades exclusivas da versao 2:",exclusiva2)
print("Numero de funções compartilhadas:",compartilhadas)

#A função "Len" é utilizada para contar a quantidade de coisas presentes na lista


## Problema: Se a divisão resultar em um número decimal (ex: 5/2 = 2,5), a parte decimal será truncada, pois 'resultado' é um inteiro
## Pergunta para reflexão: Como podemos modificar o código para que a divisão retorne um valor real corretamente?

## Resposta: Para que a divisão retorne um valor corretamente, mantendo as boas práticas de programação e buscando deixar otimizado seria -
## - possível mudar apenas o tipo da variavel resultado para float(real), assim os valores de entrada continuam int(inteiro) 
