def grille():
    return [[" " for j in range(3)] for i in range(3)], [[str(j*3 + i + 1) for i in range(3)] for j in range(3)]

def emplacement(L1, L2):
    for j in L1:
        print(j)
    print('\n')
    for i in L2:
        print(i)
    print('\n')

def win(L, j):
    for i in range(3):
        if all(L[i][k] == j for k in range(3)): return True
        if all(L[k][i] == j for k in range(3)): return True
    if all(L[i][i] == j for i in range(3)): return True
    if all(L[i][2-i] == j for i in range(3)): return True
    return False

def jouer():
    L1, L2 = grille()
    for i in range(9):
        while True:
            n = int(input('Choisis une case (1 à 9) : '))
            if n < 1 or n > 9:
                print("Numéro invalide")
                continue
            y = (n-1)//3
            x = (n-1)%3
            if L1[y][x] != " ":
                print("Case déjà prise")
                continue
            break
        joueur = 'X' if i % 2 == 0 else 'O'
        L1[y][x] = joueur
        emplacement(L1, L2)

        if win(L1, joueur):
            print(f"Joueur {joueur} gagne")
            return
    print("Match nul")
jouer()