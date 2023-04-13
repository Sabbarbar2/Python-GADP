# print("String")
# var1 = 1
# print("String {}".format(var1))
# input()

# def functie_adunare(param1):
#     print('print')
#     return param1, '-'
#
# functie_adunare(1)


# def get_sum(a: int, b: int = 3, c: int = 2) -> int:
#     return a + b + c
#
#
# suma = get_sum(1)
#
# # suma = get_sum('a', 'b')
# print(suma)

# def get_sum(a: int, b: int = 2, c: int = 3, *args) -> (int, int):
#     suma = a + b + c
#     diferenta = a - b - c
#     for i in args:
#         suma += i
#         diferenta -= i
#     print(args, type(args))
#     return suma, diferenta

def get_sum(a: int, b: int = 2, c: int = 3, *args, **kwargs) -> (int, int):
    """

    :param a: primul param
    :param b: al doilea param
    :param c: al treilea param
    :param args:
    :param kwargs:
    :return: suma tuturor param
    """
    suma = a + b + c
    diferenta = a - b - c
    print(args)
    for i in kwargs.values():
        suma += i
        diferenta -= i
    print(kwargs, type(kwargs))
    return suma, diferenta


var1, var2 = get_sum(1, 4, 4, 4, -4, d=3, e=4)

# suma = get_sum('a', 'b')
print(var1, var2)

