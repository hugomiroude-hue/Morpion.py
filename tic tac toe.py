def grille():
    return [[" " for j in range(3)] for i in range(3)], [[str(j*3 + i + 1) for i in range(3)] for j in range(3)]

def emplacement(L1, L2):
    for j in L1:
        print(j)
    print('\n')
    for i in L2:
        print(i)
    print('\n')

def win_condition(L1, joueur):
    for ligne in L1:
        if all(case == joueur for case in ligne):
            return True
    for i in range(3):
        if all(L1[j][i] == joueur for j in range(3)):
            return True
    if all(L1[i][i] == joueur for i in range(3)):
        return True
    if all(L1[i][2-i] == joueur for i in range(3)):
        return True
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

        if win_condition(L1, joueur):
            print(f"Joueur {joueur} gagne")
            return
    print("Match nul")
jouer()