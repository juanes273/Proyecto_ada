import itertools
from itertools import permutations

estudiantes = [
    {"nombre": 'Estudiante1', 'prioridades': {'MateriaA': 1, 'MateriaB': 2, 'MateriaC': 0}},
    {"nombre": 'Estudiante2', 'prioridades': {'MateriaA': 2, 'MateriaB': 1, 'MateriaC': 3}},
    {"nombre": 'Estudiante3', 'prioridades': {'MateriaA': 3, 'MateriaB': 2, 'MateriaC': 1}},
]

# Genera todas las permutaciones de estudiantes
permutaciones_estudiantes = permutations(estudiantes)

# Lista para almacenar todas las combinaciones
combinaciones_finales = []

# Itera a través de las permutaciones y asigna materias a estudiantes en el nuevo orden
for perm in permutaciones_estudiantes:
    asignaciones = []
    for i, estudiante in enumerate(perm):
        asignacion = {'nombre': estudiante['nombre'], 'prioridades': {materia: estudiante['prioridades'][materia] for materia in estudiante['prioridades']}}
        asignaciones.append(asignacion)
    combinaciones_finales.append(asignaciones)

# Diccionario de materias y sus cupos disponibles
materias_cupos = {
    "MateriaA": 2,
    "MateriaB": 3,
    "MateriaC": 2
}

# Función para generar las asignaciones sin tener en cuenta la prioridad si esta es mayor que 0
def generar_asignaciones(estudiantes, materias_cupos):
    asignaciones = {estudiante["nombre"]: [] for estudiante in estudiantes}
    
    for materia in materias_cupos.keys():
        for estudiante in estudiantes:
            estudiante_nombre = estudiante["nombre"]
            prioridad_materia = estudiante["prioridades"][materia]
            
            if prioridad_materia > 0 and materias_cupos[materia] > 0:
                asignaciones[estudiante_nombre].append(materia)
                materias_cupos[materia] -= 1
    
    return asignaciones

# Variable para almacenar las asignaciones finales
asignaciones_finales = []

# Aplicar la función a cada lista interna
for lista_estudiantes in combinaciones_finales:
    # Reiniciar los cupos para cada lista interna
    materias_cupos_temp = materias_cupos.copy()
    
    asignaciones = generar_asignaciones(lista_estudiantes, materias_cupos_temp)
    
    # Agregar las asignaciones a la lista de asignaciones_finales
    asignaciones_finales.append(asignaciones)

# Ahora, asignaciones_finales contiene las asignaciones de todas las combinaciones de estudiantes
# Puedes acceder a ellas según tus necesidades.
def sublista(lista1, lista2):
    return [x for x in lista1 if x not in lista2]

def convierte(diccionario):
    lista = []
    for materia, prioridad in diccionario.items():
            lista.append(materia)
    return lista

def obtener_prioridad(nombre_estudiante, nombre_materia):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre_estudiante:
            prioridades = estudiante["prioridades"]
            if nombre_materia in prioridades:
                return prioridades[nombre_materia]
            
def cuenta_prioridad(diccionario):
    cuenta = 0
    for materia, prioridad in diccionario.items():
            if(prioridad!=0):
                cuenta+=1
    return cuenta
            
def calcular_insatisfaccion(asignaciones, estudiantes):
    insatisfaccion_general = 0.0  # Inicializar con un valor decimal
    
    for estudiante in estudiantes:
        estudiante_nombre = estudiante["nombre"]
        prioridades = estudiante["prioridades"]
        asignacion_estudiante = asignaciones[estudiante_nombre]
        diferencia = sublista(convierte(prioridades),asignacion_estudiante)
        diferencia_ab = 0
        
        for elemento in diferencia:
            diferencia_ab+= obtener_prioridad(estudiante_nombre, elemento)

        insatisfaccion_general += abs((1-(len(asignacion_estudiante)/cuenta_prioridad(prioridades)))* diferencia_ab)


    return round(insatisfaccion_general, 2)  # Redondear a 2 decimales

# Calcular la insatisfacción para cada asignación en asignaciones_finales
insatisfacciones = []

for asignacion in asignaciones_finales:
    insatisfaccion = calcular_insatisfaccion(asignacion, estudiantes)
    insatisfacciones.append(insatisfaccion)

# La lista 'insatisfacciones' contiene la insatisfacción de cada asignación en el mismo orden que 'asignaciones_finales'.


minimo = max(insatisfacciones)
index = insatisfacciones.index(minimo)
final = asignaciones_finales[index]

print(final)