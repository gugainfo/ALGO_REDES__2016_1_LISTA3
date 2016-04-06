# Centro Universitário de João Pessoa - Unipê
# Redes de Computadores P-2
# Algorítimos e programação
# Professor: Jefferson Ferreira Barbosa
# Aluno: Gustavo Aragão (GugaInfo) Matrícula: 1310200116
# Programa Cinepolis

avaliacao = []

for i in range (0, 5):
 avaliacao.append(int(input("O que achou do Filme? 1 para Regular, 2 para Bom e 3 para Ótimo: ")))


regular = 0
bom = 0
otimo = 0


for resultado in avaliacao:
  if resultado == 3:
    otimo = otimo + 1
  if resultado == 2:
    bom = bom + 1
  if resultado == 1:
    regular = regular + 1

print(" %d Pessoas avaliaram o filme como Ótimo" % otimo)
print(" %d Pessoas avaliaram o filme como Bom" % bom)
print(" %d Pessoas avaliaram o filme como Regular" % regular)
  
 
 
            
