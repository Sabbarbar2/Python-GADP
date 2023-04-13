a = input("Alegeti o valoare: ")
try:
    print(int(a))
    print(variabila_nedefinita)
except ValueError:
    print("s-a intalnit o eroare")
    a = input("Alegeti o valoare: ")
except NameError as e:
    variabila_nedefinta = None
    print("Name error: ", e)
except Exception as e:
    print(e)
else:
    print("S-a executat cu succes")
finally:
    print("se executa oricum")
print("A trecut de blocul de try-except", variabila_nedefinta)
