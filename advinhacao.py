import random





def play():
    print_wellcome_msg()

    secret_number = random.randrange(1, 101)
    total_try = 0
    turn = 1
    points = 1000

    print('Escolha uma dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Defina a dificuldade: '))

    if nivel == 1:  # seleção de nível
        total_try = 20
    elif nivel == 2:
        total_try = 10
    else:
        total_try = 5

    while turn <= total_try:
        print(f'Tentativas {turn} de {total_try}')
        guess = int(input('Digite o seu palpite entre 1 e 100: '))  # capturando palpite do usuário

        if guess < 1 or guess > 100: # checando se o palpite está dentro do escopo do random
            print('Você deve digitar um número entre 1 e 100!!')
            continue

        if secret_number == guess:  # sistema de acerto
            print(f'Você acertou e fez {points} pontos')
            break
        else:
            if guess > secret_number: # checando se o palpite está maior ou menor que o número secreto
                print(f'{guess} é maior que o número secreto')
            elif guess < secret_number:
                print(f'{guess} é menor que o número secreto')
            losed_points = abs(secret_number - guess) #sistema de pontuação absoluto por questão de possiveis negativos
            points = points - losed_points

        turn += 1 # incrementando o contador

    print(f'Fim de jogo, o número secreto era: {secret_number}')


def print_wellcome_msg():
    print('********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('********************************')


if __name__ == '__main__':
    play()