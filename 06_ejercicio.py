#Crea una lista usando List Comprehension
#           0   1   2   3   4   5     
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for elements in numbers:
  if elements % 2 == 0:
    even_numbers.append(elements)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [ number for number in numbers if number % 2 == 0]
print('v2 =>', even_numbers_v2)

""" nombres = ['yosef', 3,'simon', 10, 'mauri', False, True, 20, 25]

sin_simon = []
for elementosDelArray in nombres:
 if elementosDelArray != "simon":
   sin_simon.append(elementosDelArray)
 if elementosDelArray: 
   sin_simon.append(elementosDelArray)
print(sin_simon) 
 """

