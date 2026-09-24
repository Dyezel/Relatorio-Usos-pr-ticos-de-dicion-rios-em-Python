

seq = 'CATGATACGTCAGTCACGTCTAGTCAGTCACTGACTAGTC' ##Sequencia Aleatoria de nucleotidios
Contagem = {}  ##Dicionario de contagem vazio para ser preenchido

for nt in seq:  ##Gera o loop de contagem
   if nt in Contagem: ##Vê se aquele determinda nucleotidio esta no dicionario
      prev_count = Contagem[nt]   ##Estabelece o valor para aquele nucleotidio, soma 1 e estabelece o novo valor como o atual
      new_count = prev_count +1
      Contagem[nt] = new_count
   else: ## Se o determinado nucleotidio não estiver no dicionario, adiciona e conta 1
      Contagem[nt]=1;

print(Contagem) ##Printa o dicionario

print(Contagem.get('A')) ## Volta o numero de contagem apenas para o nucleotidio escolhido, neste caso 'A'

if 'U' in Contagem.keys(): ##Verifica se a sequencia é DNA ou RNA, verificando se existe o nucleotidio 'U' no dicionario
   print('A sequencia é um RNA')
else:
   print('A sequencia é um DNA')
