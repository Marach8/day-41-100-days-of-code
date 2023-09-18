import time
dict = {'name': None, 'URL': None, 'description': None, 'rating': None}

c = list(dict.keys())

for key in dict:
  print(f'Input the {key} of the website: ')
print('\033[31mIn that order each seperated by a comma!')
print()

a = input('''\033[0m>> ''').split(',')
print()

for i in a:
  dict[c[a.index(i)]] = a[a.index(i)]

for i, j in dict.items():
  time.sleep(1.5)
  print(f'\033[0m{i}: \033[34m{j}')
  print()
