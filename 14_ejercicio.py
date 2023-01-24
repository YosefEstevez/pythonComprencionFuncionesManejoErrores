def myfunc(a, b):
  return a + b

x = list(map(lambda myfunc:myfunc, {('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')}))

print(x)

#convert the map into a list, for readability:
print(list(x))
