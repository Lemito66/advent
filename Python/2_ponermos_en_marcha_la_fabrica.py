
"""
En el taller de Santa, los elfos tienen una lista de regalos que desean fabricar y un conjunto limitado de materiales.

Los regalos son cadenas de texto y los materiales son caracteres. Tu tarea es escribir una función que, dada una lista de regalos y los materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.

Un regalo se puede fabricar si contamos con todos los materiales necesarios para fabricarlo.
"""
def manufacture(gifts, materials):
    #Code here
    materials_modified = list(materials)
    
    list_materials = []
    
    counter = 0
    for gift in range(len(gifts)):
        for letter in range(len(gifts[gift])):
            if gifts[gift][letter] in materials_modified:
                counter += 1
                
        if counter == len(gifts[gift]):
            list_materials.append(gifts[gift])
            counter = 0
        else:
            counter = 0
            
    
    return list_materials


gifts = ['tren', 'oso', 'pelota']
materials = 'tronesa'

print(manufacture(gifts, materials)) # ["tren", "oso"]
# 'tren' SÍ porque sus letras están en 'tronesa'
# 'oso' SÍ porque sus letras están en 'tronesa'
# 'pelota' NO porque sus letras NO están en 'tronesa'

# transform string in list one by one


gifts = ['juego', 'puzzle']
materials = 'jlepuz'

print(manufacture(gifts, materials)) # ["puzzle"]

gifts = ['libro', 'ps5']
materials = 'psli'

print(manufacture(gifts, materials)) # []