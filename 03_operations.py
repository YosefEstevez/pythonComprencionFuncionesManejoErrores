set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#.union une conjuntos
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Elementos en comun &
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#Elementos diferentes -
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#sin elementos que esten en comun  ^
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
 

 # esto es una trem
