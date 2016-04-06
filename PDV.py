# Centro Universitário de João Pessoa - Unipê
# Redes de Computadores P-2
# Algorítimos e programação
# Professor: Jefferson Ferreira Barbosa
# Aluno: Gustavo Aragão (GugaInfo) Matrícula: 1310200116
# Programa  PDV

preco_produtos = []

for i in range (0, 5):
 preco_produtos.append(float(input("Digite o valor do Produto %d: " % (i + 1))))

ate_49 = 0
ate_80 = 0
maior_80 = 0
media = ((preco_produtos [0]) + (preco_produtos [1]) + (preco_produtos [2]) + (preco_produtos [3]) + (preco_produtos [4])) / 5

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
print(" A Média de Preço foi R$:%.2f " % float(media))
