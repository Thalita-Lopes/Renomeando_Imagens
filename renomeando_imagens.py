#Acesso ao drive
from google.colab import drive
drive.mount('/content/drive')

# Array contendo as imagens da Pasta no drive
import os
Imagens = os.listdir('/content/drive/My Drive/imagens/')
quantidade = len(Imagens)
print('A pasta contém {} imagens:'.format(quantidade))
print(Imagens)

#Renomeando as imagens
i = 0
conjunto = 7
ori = 0
posicao = 0
while i < conjunto:
    posicao = posicao + 1
    while ori <= 315:
      orientacao = ori
      ponto = 'P' + str(posicao) + '_{}'.format(orientacao)
      ori = ori + 45
      if (i < quantidade):
        os.rename('/content/drive/My Drive/imagens/{}'.format(Imagens[i]),'/content/drive/My Drive/renomeadas/{}.jpg'.format(ponto))
        print('Imagem renomeada{}'.format(ponto))

      i = i + 1
      if conjunto < quantidade:
        conjunto = conjunto + 8
    ori = 0

Imagens = os.listdir('/content/drive/My Drive/imagens/')
Renomeadas = os.listdir('/content/drive/My Drive/renomeadas/')
if len(Imagens) == 0:
  print('Todas as imagens foram renomeadas')
  for imagem in Renomeadas:
    print(imagem)
else:
  print('{} imagens não foram renomeadas'.format(len(Imagens)))
