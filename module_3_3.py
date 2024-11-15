def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [2, 'cvb',  False]
values_dict = {'a' : 13, 'b' : 15, 'c' : 65}
print_params(**values_dict)
print_params(*values_list)

