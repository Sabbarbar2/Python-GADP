"""
r -> citim, nu adaugam, daca fisierul nu exista apare eroare
w -> scriem, daca fisierul nu exista, il adauga, daca exista ceva scris deja in fisier il rescrie
a -> scriem, daca exista ceva scris in fisier, il adauga pe urmatorul rand, nu rescrie, daca fisierul nu exista, il creeaza
r+ -> scriere, citire, daca fisierul nu exista apare eroare
"""

# file = open('data_2.txt', 'r+')
# file.write('Hello_2')
# file.close()

# file = open('data1.txt', 'r+')
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open('data.txt', 'w') as file:
#     file.write('hello\n')
#     file.write('hello1\n')
#     file.write('hello2\n')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     print(list(file))
#     print(file)
#     for line in list(file):
#         print(line)

# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)


with open('data.txt', 'w') as file:
    file.writelines(f"{i}\n" for i in ['hello', 'hello1', 'hello2'])

