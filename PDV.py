# Centro Universitário de João Pessoa - Unipê
# Redes de Computadores P-2
# Algorítimos e programação
# Professor: Jefferson Ferreira Barbosa
# Aluno: Gustavo Aragão (GugaInfo) Matrícula: 1310200116
# Programa  PDV

preco_produtos = [float(input("Digite o valor do Primeiro Produto: ")), 
                  float(input("Digite o valor do Segundo Produto: ")), 
                  float(input("Digite o valor do Terceiro Produto: ")), 
                  float(input("Digite o valor do Quarto Produto: ")), 
                  float(input("Digite o valor do Quinto Produto: "))]

ate_49 = 0
ate_80 = 0
maior_80 = 0

for valor in preco_produtos:
  if valor < 50:
     ate_49 = ate_49 + 1
  if (valor >= 50) and (valor <= 80): 
     ate_80 = ate_80 + 1
  if valor > 80:
     maior_80 = maior_80 + 1

print(" %d Produtos com preço abaixo de R$50,00" % ate_49)
print(" %d Produtos com preço entre R$50,00 e R$80,00" % ate_80)
print(" %d Produtos com preço maior que R$80,00" % maior_80)
