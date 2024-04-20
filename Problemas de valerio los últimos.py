#Problema 1



def Calcular_el_producto(d):
    ans=1 #Ans tiene que estar fuera del bucle for, pues siempre se repetirá que ans vale 1,  y como el último valor es 9, entonces 9*1=9 por lo tanto se pone dentro de la función y fuera del for
    for value in d.values():
       
        ans *= value #Esto funciona porque al devolverse a ans (Nuestro valor inicial) se multiplica por un valor (value) cada vez diferente debido al bucle for

    
    return ans

dicccionario1 = {"Valor1":5,"Valor2":2,"Valor3":7,"Valor4":9}
resultado = Calcular_el_producto(dicccionario1)
#Print(resultado)

#2
Diccionario2 = {"a":1,"b":3,"c":5} #Los valores a b y c tienen que estár entre comillas, pues son cadenas.
Valor_eliminado = Diccionario2.pop("b") #Esto también tiene que estar entre comillas.

#print(Diccionario2)

#3
#Los diccionarios tienen claves y valores, entonces una lista será de claves y otra de valores, para crear el diccionario
lista_clave = ["Christian", "Melina", "Danna"]
lista_valores = ["Alonso", "Jessica", "Paola"]

Diccionario3=dict(zip(lista_clave,lista_valores))# El método zip() combina los elementos de dos listas en tuplas, y luego dict() convierte esas tuplas en pares clave-valor en un diccionario.
#print(f"diccionario resultante: {Diccionario3}")


#4

# Diccionario de ejemplo
mi_diccionario = {'Roberto': 10, 'Felipe': 9, 'Melina': 15, 'Christian': 2, 'Arianna': 32}# Los valores se ordenan alfabéticamente

# Ordenar las claves alfabéticamente
claves_ordenadas = sorted(mi_diccionario.keys())

# Crear un nuevo diccionario con las claves ordenadas
diccionario_ordenado = {clave: mi_diccionario[clave] for clave in claves_ordenadas}

# Imprimir el diccionario ordenado
#print(diccionario_ordenado)

#5
# Crear un diccionario de ejemplo
mi_diccionario = {'a': 1000, 'b': 10, 'c': 350, 'd': 2100, 'e': 180}

# Obtener el valor máximo del diccionario
valor_maximo = max(mi_diccionario.values())

# Obtener el valor mínimo del diccionario
valor_minimo = min(mi_diccionario.values())

# Imprimir los resultados
#print(f"Valor máximo: {valor_maximo}")
#print(f"Valor mínimo: {valor_minimo}")

#6

# Diccionario de ejemplo
tercer_diccionario = {'Derek': 10, 'Felipe': 15, 'Alan': 20, 'Felix': 10, 'Jesus': 20}

# Crear un nuevo diccionario utilizando setdefault()
res = {}
for key, val in tercer_diccionario.items():
    res.setdefault(val, key)

# Imprimir el diccionario resultante
#print("El diccionario después de eliminar los valores duplicados:", dict((v, k) for k, v in res.items()))

#7

# Crear un diccionario
mi_diccionario = {}

# Verificar si el diccionario está vacío
if bool(mi_diccionario):
#    print("El diccionario no está vacío")
else:
#    print("El diccionario está vacío")

#8
    
def extraer_valores_por_asignatura(diccionarios, asignatura):
    # Filtrar los diccionarios que contienen la asignatura especificada
    diccionarios_filtrados = [d for d in diccionarios if asignatura.lower() in d]

    # Extraer los valores asociados a la asignatura
    valores_asignatura = [diccionario[asignatura.lower()] for diccionario in diccionarios_filtrados]

    return valores_asignatura
#9, 10 Y 11
# Diccionarios de ejemplo
diccionarios_ciencias = [
    {'Matematicas': 90, 'ciencia': 92},
    {'matematicas': 89, 'ciencia': 94},
    {'Matematicas': 92, 'ciencia': 88}
]

diccionarios_matematicas = [
    {'matematicas': 90, 'ciencia': 92},
    {'Matematicas': 89, 'ciencia': 94},
    {'Matematicas': 92, 'ciencia': 88}
]

# Asignaturas
asignatura_ciencias = 'ciencia'
asignatura_matematicas = 'matematicas'

# Extraer valores para Ciencias y Matemáticas
valores_ciencias = extraer_valores_por_asignatura(diccionarios_ciencias, asignatura_ciencias)
valores_matematicas = extraer_valores_por_asignatura(diccionarios_matematicas, asignatura_matematicas)

# Imprimir resultados
print(f"Valores para la asignatura '{asignatura_ciencias}': {valores_ciencias}")
print(f"Valores para la asignatura '{asignatura_matematicas}': {valores_matematicas}")

#12
# Diccionario de ejemplo
mi_diccionario = {'Nombre': 'Derek', 'Edad': 18, 'Designación': 'Nada'}

# Obtener la longitud del diccionario (número de valores)
longitud_diccionario = len(mi_diccionario)

# Imprimir la longitud
#print(f"La longitud del diccionario es: {longitud_diccionario}")

#13
from collections import deque

def depth(d):
    queue = deque([(id(d), d, 1)])
    memo = set()

    while queue:
        id_, o, level = queue.popleft()
        if id_ in memo:
            continue
        memo.add(id_)
        for k, v in o.items():
            if isinstance(v, dict):
                queue.append((id(v), v, level + 1))

    return level

# Otro diccionario de ejemplo
otro_diccionario = {'a': 1, 'b': {'c': {'d': {}}}}

# Calcular la profundidad del diccionario
profundidad_otro = depth(otro_diccionario)

# Imprimir la profundidad
#print(f"La profundidad del otro diccionario es: {profundidad_otro}")

#14
def get_key_by_index(d, index):
    keys = list(d.keys())
    if 0 <= index < len(keys):
        return keys[index]
    else:
        return None

# Diccionario de ejemplo
mi_diccionario = {'física': 90, 'matemáticas': 85, 'química': 78}

# Acceder a las claves por índice
indice_fisica = get_key_by_index(mi_diccionario, 0)
indice_matematicas = get_key_by_index(mi_diccionario, 1)
indice_quimica = get_key_by_index(mi_diccionario, 2)

# Imprimir los resultados
print(f"Clave en el índice 0: {indice_fisica}")
print(f"Clave en el índice 1: {indice_matematicas}")
print(f"Clave en el índice 2: {indice_quimica}")
#15
def dict_to_list_of_lists(d):
    return [[key, value] for key, value in d.items()]

# Diccionario de ejemplo
diccionario_original = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}

# Convertir el diccionario en una lista de listas
lista_de_listas = dict_to_list_of_lists(diccionario_original)

# Imprimir el resultado
print("Lista de listas resultante:")
for sublist in lista_de_listas:
#    print(sublist)
#16
def filter_even_numbers(d):
    filtered_dict = {}
    for key, values in d.items():
        filtered_values = [value for value in values if value % 2 == 0]
        filtered_dict[key] = filtered_values
    return filtered_dict

# Diccionario de ejemplo
diccionario_valores = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

# Filtrar números pares del diccionario
diccionario_filtrado = filter_even_numbers(diccionario_valores)

# Imprimir el resultado
#print("Diccionario filtrado:")
for key, values in diccionario_filtrado.items():
#    print(f"{key}: {values}")
