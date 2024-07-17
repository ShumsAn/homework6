my_dict = {'Rik':1950,'Morty':2000}
print('Мои записи:',my_dict)
print('Год рождения Рика :',my_dict['Rik'])
print('Знаем ли мы год рождения Big?:', my_dict.get('Big'))
my_dict['Max'] = 2005
my_dict.update({'Den': 1973})
print('Мои обновленные записи:',my_dict)
Den_Del = my_dict.pop('Den')
print('Какой год Рождения у Den:',Den_Del)
print('Мои обновленные записи 2:',my_dict)


my_set = {0,0,1,1,'two','two',3,3,4,4,5}
print(my_set)
print(my_set.add(6))
print(my_set.discard(0))
print(my_set)

