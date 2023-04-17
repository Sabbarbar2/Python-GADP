"""
Cerinta:
Cu ajutorul celor invatate in ultima saptamana la curs se va realiza un calculator, astfel:
- calculatorul detine cifre de la 0 la 9,
- semnele matematice cu ajutorul carora se vor putea realiza operatii matematice sunt
urmatoarele: + (adunare), - (scadere), / (impartire), * (inmultire)
- pe langa cifrele amintite anterior si semnele matematice se va putea sterge cu ajutorul
litere C
- toate operatiile presupun interactiunea cu utilizatorul (functii de tip input)
- utilizati functii

"""


def suma(a, b):
    return a + b


def diferenta(a, b):
    return a - b


def inmultire(a, b):
    return a * b


def impartire(a, b):
    if b == 0:
        return None
    else:
        return a / b


while True:
    print(f"Calculator\nOperatii posibile:{','.join(['+', '-', '*', '/'])}\nPentru a sterge apasa c")
    operator_1 = input("Adauga primul operator: ")
    operator_2 = input("Adauga al doilea operator: ")
    operatie = input("alege operatia pe care doresti sa o executi: ")
    if operator_1 == 'c' or operator_2 == 'c' or operatie == 'c':
        continue
    if operatie in ['+', '-', '*', '/'] and operator_1.isdigit() and operator_2.isdigit():
        if operatie == '+':
            print(f"Suma celor doua numere este {suma(int(operator_1), int(operator_2))}")
        elif operatie == '-':
            print(f"Diferenta celor doua numere este {diferenta(int(operator_1), int(operator_2))}")
        elif operatie == '*':
            print(f"Produsul celor doua numere este {inmultire(int(operator_1), int(operator_2))}")
        elif impartire(int(operator_1), int(operator_2)) is None:
            print("Nu se poate face impartirea la 0, incearca din nou")
            continue
        else:
            print(f"Catul celor doua numere este {impartire(int(operator_1), int(operator_2))}")
        break
    else:
        print(f"Alege o operatie din lista: {','.join(['+', '-', '*', '/'])}")


