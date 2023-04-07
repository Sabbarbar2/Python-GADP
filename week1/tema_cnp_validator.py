# cnp format: S AA LL ZZ JJ NNN C
# s - sex intre 1-9
# aa - ultimele 2 cifre din anul nasterii
# ll - luna din 2 cifre ex: 01 ianuarie
# zz - ziua din 2 cifre
# jj - codul judetului intre 1-52
# nnn - nr din 3 cifre intre 001-999
# c - cifra de control calculata conform : : fiecare cifră din CNP este înmulțită cu
# cifra de pe aceeași poziție din numărul 279146358279; rezultatele sunt însumate,
# iar rezultatul final este împărțit cu rest la 11.
# Dacă restul este 10, atunci cifra de control este 1, altfel cifra de
# control este egală cu restul.
#         s a a l l z z j j n n  n  c
#         1 2 3 4 5 6 7 8 9 1 2  3  4
#         0 1 2 3 4 5 6 7 8 9 10 11 12

print("Welcome to the CNP Validator")
cnp = input("Input a cnp to check if its valid: ")

valid = True
calcul_c = 0
nr_calc = '279146358279'

for i in range(12):
    calcul_c = calcul_c + (int(nr_calc[i]) * int(cnp[i]))


if calcul_c % 11 == 10:
    dif = 1
else:
    dif = calcul_c % 11


if len(cnp) == 13 and cnp.isnumeric() is True:
    if cnp[0] == 0:
        valid = False
    elif cnp[3] not in (0, 1) and int(cnp[4]) > 9:
        valid = False
    elif cnp[5] not in (0, 1, 2, 3) and int(cnp[4]) > 9:
        valid = False
    elif int(cnp[12]) != dif:
        valid = False
    elif int(cnp[7:9]) > 52:
        valid = False


if valid:
    print("CNP-ul este valid")
else:
    print("CNP-ul nu este valid")


print(f"calcul_c = {calcul_c}, dif = {dif}, valid = {valid}, cnp ={cnp}")



