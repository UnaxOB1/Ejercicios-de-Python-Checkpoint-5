#1

colors = ['Blue', 'Yellow', 'Purple', 'Black']

for color in colors:
  print(color)

#2

def suma(first, second, third):
  print(first + second + third)

suma(14, -7, 3)

#3

suma_lambda = lambda first, second, third: first + second + third
  
print(suma_lambda(14,-7,3))

#4

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
   print('Enrique was found!')
else:
   print('Enrique was not found!')



