inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"]= [ 'seashell', 'strange berry',  'lint' ]
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
inventory['gold'] = [inventory['gold']]

for key, value in inventory.items():
    length = len(key)
    print(key, (8 - length) * ' ' + ": ", end = ' ' )
    print(*value, sep = ', ')
