#Retorna solo palabras de 4 letras y más
def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda word:len(word)>= 4, words))


words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)