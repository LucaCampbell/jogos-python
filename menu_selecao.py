import advinhacao
import forca
import jogo_da_velha

print('********************************')
print('*********Escolha um jogo********')
print('********************************')

print('(1) Forca (2) Adivinhação (3) Jogo da Velha')
game = int(input('Qual jogo? '))

if game == 1:
    print('Jogando Forca')
    forca.play()
elif game == 2:
    print('Jogo da adivinhação')
    advinhacao.play()
elif game == 3:
    print('Jogo da Velha')
    jogo_da_velha.play()
