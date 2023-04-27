# class Calculator:
#
#     def __int__(self):
#         self.first_op = int(input('Alege primul numar: '))
#         self.second_op = int(input('Alege al doilea numar: '))
#         self.op = input('Alege operatorul')
#
#     def adunare(self):
#         return (self.first_op + self.second_op)
#
#     def scadere(self):
#         return(self.first_op - self.second_op)
#
#     def inmultire(self):
#         return(self.first_op * self.second_op)
#
#     def impartire(self):
#         if self.second_op != 0:
#             return(self.first_op / self.second_op)
#         else:
#             return "Nu functioneaza"
#
#     def __str__(self):
#         if self.op == '-':
#             return str(self.scadere())
#         elif self.op == '+':
#             return str(self.adunare())
#         elif self.op == '*':
#             return str(self.inmultire())
#         else:
#             return str(self.impartire())
#
#
#
# obiect1 = Calculator()
# # obiect2 = Calculator()
# # obiect3 = Calculator()
# # obiect4 = Calculator()
#
# print(obiect1)
# # print(obiect2)
# # print(obiect3)
# # print(obiect4)

class Calculator:

    def __init__(self):
        self.first_op = float(input("Alege primul numar:"))
        self.second_op = float(input("Alege al 2 lea numar:"))
        self.op = input("Operatorul este:")


    def Adunare(self):
        return (self.first_op + self.second_op)

    def Scadere(self):
        return (self.first_op - self.second_op)

    def Inmultire(self):
        return (self.first_op * self.second_op)

    def Impartire(self):
        if(self.second_op !=0):
            return (self.first_op / self.second_op)
        else:
            return "Nu functioneaza"

    def __str__(self):
        if (self.op == '-'):
            return str(self.Scadere())
        elif (self.op == '+'):
            return str(self.Adunare())
        elif (self.op == '/'):
            return str(self.Impartire())
        else:
            return str(self.Inmultire())

obiect1 = Calculator()
# obiect2 = Calculator()
# obiect3 = Calculator()

print(obiect1)
# print(obiect3)
# print(obiect2)
