versao1 = {"login","registro","perfil","mensagens","notificações","relatórios"}
versao2 = {"login","registro","perfil","pagamentos","notificações","ajuda","relatórios","backup"}

exclusiva1 = len(versao1 - versao2)
exclusiva2 = len(versao2 - versao1)
compartilhadas = len(versao1 & versao2)

print("Numero de funcionalidades exclusivas da versão 1:",exclusiva1)
print("Numero de funcinoalidades exclusivas da versao 2:",exclusiva2)
print("Numero de funções compartilhadas:",compartilhadas)

#A função "Len" é utilizada para contar a quantidade de coisas presentes na lista

