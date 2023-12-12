"""

En la fábrica de juguetes del Polo Norte, cada juguete tiene un número de identificación único.

Sin embargo, debido a un error en la máquina de juguetes, algunos números se han asignado a más de un juguete.

¡Encuentra el primer número de identificación que se ha repetido, donde la segunda ocurrencia tenga el índice más pequeño!

En otras palabras, si hay más de un número repetido, debes devolver el número cuya segunda ocurrencia aparezca primero en la lista. Si no hay números repetidos, devuelve -1.

"""

def find_first_repeated(list_of_numbers):
    # Write your code here
    repeated = []
    for number in range(len(list_of_numbers)):
        element = list_of_numbers[number]
        print(list_of_numbers.index(element), number) # 0 0, 1 1, 2 2, 3 3, 2 4, 0 5
        if list_of_numbers.index(element) != number:
            repeated.append(element)
    
    if len(repeated) > 0:
        return repeated[0]
    
    return -1

giftIds = [2, 1, 3, 5, 3, 2]
firstRepeatedId = find_first_repeated(giftIds)
print(firstRepeatedId) # 3
# Aunque el 2 y el 3 se repiten
# el 3 aparece primero por segunda vez

giftIds2 = [1, 2, 3, 4]
firstRepeatedId2 = find_first_repeated(giftIds2)
print(firstRepeatedId2) # -1
# Es -1 ya que no se repite ningún número

giftIds3 = [5, 1, 5, 1]
firstRepeatedId3 = find_first_repeated(giftIds3)
print(firstRepeatedId3) # 5

