import random

num = int(input('Escolha um número de 0 a 5 e tente a sorte!: '))
sorteio = random.randint(0, 5)

if num == sorteio:

    if sorteio == 0:
        print()
        print("S O R T E A N D O:")
        print()
        print([0], 1, 2, 3, 4, 5)
        print()
    elif sorteio == 1:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, [1], 2, 3, 4, 5)
        print()
    elif sorteio == 2:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, [2], 3, 4, 5)
        print()
    elif sorteio == 3:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, 2, [3], 4, 5)
        print()
    elif sorteio == 4:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, 2, 3, [4], 5)
        print()
    elif sorteio == 5:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, 2, 3, 4, [5])
        print()

    print('Parabens, o você esta com sorte o numero sorteado foi {}, o mesmo do seu!!!'.format(sorteio))

else:
    if sorteio == 0:
        print()
        print("S O R T E A N D O:")
        print()
        print([0], 1, 2, 3, 4, 5)
        print()
    elif sorteio == 1:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, [1], 2, 3, 4, 5)
        print()
    elif sorteio == 2:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, [2], 3, 4, 5)
        print()
    elif sorteio == 3:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, 2, [3], 4, 5)
        print()
    elif sorteio == 4:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, 2, 3, [4], 5)
        print()
    elif sorteio == 5:
        print()
        print("S O R T E A N D O:")
        print()
        print(0, 1, 2, 3, 4, [5])
        print()


    print('Que pena, você fez o L!!')