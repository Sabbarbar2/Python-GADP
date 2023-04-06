# a = '0'
# a += '3'
# print(a)
# a = 3
# print(a)
nr_mere = 2
nr_pere = 3
#mesaj = f"Ana are {nr_mere} mere si {nr_pere} pere"
# mesaj = "Ana are {} mere si {} pere".format(nr_mere, nr_pere)
# mesaj2 = "Ana are {0} mere si {1} pere".format(nr_mere, nr_pere)
# mesaj2 = "Ana are {0} mere si {2} pere".format(nr_mere, nr_pere) # daca nu are variabila 2 primim error

# mesaj = "Ana are " + str(nr_mere) + " mere si " + str(nr_pere) + " pere"
# mesaj = f'Ana are "{nr_mere}" si "{nr_pere}" pere'
# mesaj = f"Ana are '{nr_mere}' si '{nr_pere}' pere"
# mesaj = f'Ana are \'{nr_mere}\' si \n \'{nr_pere}\' pere' # \ interpreteaza un caracter ca string
mesaj = """\tAna are mere 
si pere
"""
# nu conteaza tipul de ghilimele cand scriem pe mai multe linii
print(mesaj)

#print(mesaj2)







