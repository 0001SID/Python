list1 =['I','am','a','boy']
list1 = {'good':'dad',1:'suman',2:'Das'}
print(list1['good'])
list1[1] = 'name'
print(list1)
print(list1[2])
for abbrev,city in list(list1.items()):
    print(f'{abbrev} is {city}')
for city,abbrev in list(list1.items()):
    print(f'{city} is {abbrev}')
find = list1.get('goo','from find')
if find:
    print('This is here')
print(find)