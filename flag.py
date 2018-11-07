import re
import numpy as np
import cv2

def mostrarImagem(RGB_MATRIZ):
    # Cria uma imagem nova (tamanho 400x200 e 3 canais RGB)
    largura = 424
    altura = 308
    imagem = np.zeros((altura, largura, 3), dtype=np.uint8)
    # Preenche o fundo de amarelo
    cv2.rectangle(imagem, (0, 0), (largura, altura), (0, 255, 255), -1)
    # Desenha uma borda azul
    cv2.rectangle(imagem, (0, 0), (largura-5, altura-5), (255, 0, 0), 5)
    idx = 0
    for y in range(0, imagem.shape[0] - 1):
        for x in range(0, imagem.shape[1] - 1):
            imagem[y, x] = RGB_MATRIZ[idx]
            idx+=1
    # Exibe a imagem
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)

FILE = open('hackflag.txt', 'r')
line = FILE.read()
matchObj = line.split('\n')
print(len(matchObj))
RGB = []

for group in matchObj:
    aux = group.split(') ')
    pixel = []
    for s in aux:
        s = s.strip('(')
        s = s.strip()
        s = s.strip(')')
        ponto = s.split(', ')
        try:
            int_lst = [int(x) for x in ponto]
            #print("lista: ")
            #print(int_lst)
            RGB.append(int_lst)
        except Exception as e:
            print("%s " % str(e))

print(RGB[0])
print(len(RGB))
mostrarImagem(RGB)
