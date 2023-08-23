# string
name = 'Prabhakaran Vettum Perumal'
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace('Vettum Perumal', 'Tamilan'))
print(name[-1::-1])
print(name.split())
print(name.count('a'))

# list
details = ['Prabhakaran', 20, 'Bsc-IT', 'SIES', 'OSP', 'Python Developer']
details1 = details.copy()
details.append('Dahisar')
print(details)
details.extend(['Dharavi', 'Tamilnadu'])
print(details)
print(details.count('Prabhakaran'))
print(details.index('OSP'))
details.sort(key=str)
print(details)
print(details1)

# tuple
details = ('Prabhakaran', 20, 'Bsc-IT', 'SIES', 'OSP', 'Python Developer')
print(details.count(20))
print(all(details))
print(any(details))
print(details.index('SIES'))

# set
pro_lang = {'Python', 'Java', 'C', 'C++', 'Ruby', 'HTML'}
pro_lang.add('Javascript')
print(all(pro_lang))
print(any(pro_lang))
print(pro_lang)
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
s1.intersection_update(s2)
print(s1)
s2.difference_update(s1)
print(s2)
s2.symmetric_difference_update(s1)
print(s2)

# dictionary
details = {'name': 'Prabhakaran', 'age': 20, 'stream': 'Bsc-IT',
           'college': 'SIES', 'office': 'OSP', 'role': 'Python Developer'}
num = [1, 2, 3, 4, 5, 6]
num_1 = {}.fromkeys(num, 'number')
details_1 = details.copy()
print(details.items())
print(details.keys())
print(details.values())
print(details_1)
print(details.setdefault('gender'))
print(num_1)
