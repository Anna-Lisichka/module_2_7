def print_params(a = 1, b = 'строка', c = True):
    print( a, b, c)


print_params()
print_params(a=146, c='sweety')
print_params(c=2+5, a=(1, 2, 3))
print_params(b=25)  # работает, потому что я изменила параметр по умолчанию
print_params(c=[1, 2, 3])  # работает, просто вместо параметра по умолчанию я определяю список

values_list = (5, 2.3, [1, 2])
values_dict = {'a': 'Helen', 'b': '+', 'c': 'Egor'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2024, 'year']
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)