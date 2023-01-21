def message_creator(text):
   # Escribe tu solución 👇
   respuesta = {'computadora':'Con mi computadora puedo programar usando Python', 'celular':'En mi celular puedo aprender usando la app de Platzi', 'cable':'¡Hay un cable en mi bota!'}
   if text in respuesta.keys():
      return respuesta[text]
   else:
      return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)