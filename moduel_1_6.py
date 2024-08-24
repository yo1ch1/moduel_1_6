my_dict = {'Dima': 2003, 'Vitya': 2001, 'Roma': 2002}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Anotn'))
my_dict.update({'Sasha': 2004, 'Oleg': 1995})
print(my_dict)
d= my_dict.pop('Vitya')
print(d)
print(my_dict)
#Работа с множествами
my_set = {1,2,3,1,2,3,'domina', 'domina', True}
my_set.add(23)
print(my_set)
print(my_set.add(400))
print(my_set)
my_set.discard(2)
print(my_set)