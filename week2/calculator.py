# cerinte
# 2 cifre preluate de la tastatura
# check if introduce litere
# impartire la 0

# operator_1 = input("Adauga primul operator: ")
# operator_2 = input("Adauga al doilea operator: ")
#
# operatie = input("alege operatia pe care doresti sa o executi: ")

# lista_operatii =


while True:
    operator_1 = input("Adauga primul operator: ")
    operator_2 = input("Adauga al doilea operator: ")
    operatie = input("alege operatia pe care doresti sa o executi: ")
    if operatie in ['+', '-', '*', '/'] and operator_1.isdigit() and operator_2.isdigit():
        if int(operator_2) and operatie == '/':
            print(f'Impartirea la 0 nu este permisa')
            continue
        if operatie == '+':
            print(f"Suma celor doua numere este {int(operator_1) + int(operator_2)}")
        elif operatie == '-':
            print(f"Diferenta celor doua numere este {int(operator_1) - int(operator_2)}")
        elif operatie == '*':
            print(f"Produsul celor doua numere este {int(operator_1) * int(operator_2)}")
        else:
            print(f"Diferenta celor doua numere este {int(operator_1) / int(operator_2)}")
        break
    else:
        print(f"Alege o operatie din lista: {','.join(['+', '-', '*', '/'])}")
