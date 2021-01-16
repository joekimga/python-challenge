mydictionary = {'d': 34, 'a': 4, 'b': 18, 'c': 1}
print(mydictionary['d'], end = '')
print(mydictionary.get('d'))
print(max(mydictionary, key = mydictionary.get))
