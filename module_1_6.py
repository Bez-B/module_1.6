my_dict = {'Alexandr': 1984, 'Mikhail': 1990, 'Marusia': 1998, 'Vasilisa': 1980}
print(my_dict)
print(my_dict['Marusia'])

my_dict.update({'Alisa': 2001, 'Sergey': 1989})
my_dict['Dasha'] = 1993
woman = my_dict.pop('Vasilisa')
print(woman)
print(my_dict)

my_set = {'раз', 2, 3, 4, 5, 'вышел', False, 6.25, 3, 4, 'раз', 2, False}
print(my_set)

my_set.add('car')
my_set.add(my_dict['Dasha'])
my_set.discard(False)
print(my_set)