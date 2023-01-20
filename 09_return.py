#multiples retornos
def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

#retorna segun el valor de la tupla
result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)