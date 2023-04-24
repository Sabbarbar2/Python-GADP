from operator import itemgetter

while True:

    alegere = int(input('Alege una dintre optiunile:\n1 - Afiseaza categoriile\n2 - Afiseaza task-urile\n3 - Adauga categorii\n4 - Adauga task-uri\n0 - Iesi din aplicatie\n'))

    if alegere == 1:
        with open('categories.txt', 'r') as file:
            categories = file.read().splitlines()
        file.close()
        print(f"Categoriile sunt:\n {' '.join(categories)}")
    elif alegere == 2:
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
            print('Alege metoda de sortare a task-urilor afisate de mai jos:\n')
            alegere_sortare = int(input('1 - sortare ascendentă task\n2 - sortare descendentă task\n3 - sortare ascendentă data\n4 - sortare descendentă data\n5 - sortare ascendentă persoana responsabilă\n6 - sortare descendentă persoană responsabilă\n7 - sortare ascendentă categorie\n8 - sortare descendentă categorie:\n'))
            if alegere_sortare == 1:
                res = sorted(tasks, key=itemgetter(0), reverse=False)
            elif alegere_sortare == 2:
                res = sorted(tasks, key=itemgetter(0), reverse=True)
            elif alegere_sortare == 3:
                res = sorted(tasks, key=itemgetter(1), reverse=False)
            elif alegere_sortare == 4:
                res = sorted(tasks, key=itemgetter(1), reverse=True)
            elif alegere_sortare == 5:
                res = sorted(tasks, key=itemgetter(2), reverse=False)
            elif alegere_sortare == 6:
                res = sorted(tasks, key=itemgetter(2), reverse=True)
            elif alegere_sortare == 7:
                res = sorted(tasks, key=itemgetter(3), reverse=False)
            elif alegere_sortare == 8:
                res = sorted(tasks, key=itemgetter(3), reverse=True)
            result = '\n'.join(res)
            print(f"Task-urile sunt:\n{result}")
        file.close()
    elif alegere == 3:
        with open('categories.txt', 'r+') as file:
            categories = file.read().splitlines()
            categorie_noua = input('Introdu noua categorie:')
            if categorie_noua in categories:
                print('Categorie pe care incerci sa o adaugi exista deja. Incearca din nou.')
                print(f'Categoriile existente sunt: {categories}')
                continue
            else:
                file.write(f"{categorie_noua}\n")
        file.close()
    elif alegere == 4:
        with open('tasks.txt', 'r+') as file:
            tasks = input('Introdu in ordine task-ul, data la care trebuie executat, persoana responsabila si categoria din care face parte separate prin ,: ')
            tasks_check = tasks.split(",")
            read_tasks = file.read().splitlines()
            with open('categories.txt', 'r+') as file1:
                categ = file1.read().splitlines()
                if tasks_check[3] not in categ:
                    if tasks_check[0] not in read_tasks:
                        file1.write(f"{tasks_check[3]}\n")
                        print(f'A fost adaugata categoria {tasks_check[3]}')
                    else:
                        print('Task-ul pe care incerci sa il adaugi exista deja in lista')
                        continue
            file1.close()
            file.write(f"{tasks}\n")
        file.close()
    elif alegere == 0:
        break


