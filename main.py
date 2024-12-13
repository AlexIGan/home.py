def print_params(z = 1, x = 'строка', c = True):
    print(z, x, c)

values_list = [45, 'Москва', False]
values_dict = {'z':10, 'x':'Чита', 'c':None}
values_list_2 = [63, 'Сочи']


print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)