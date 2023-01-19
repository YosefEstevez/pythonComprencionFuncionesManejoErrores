#Elimina elementos duplicados usando conjuntos

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

# Escribe tu solución 👇
new_set = countries.union(countries, northAm,centralAm, southAm )
print(new_set)