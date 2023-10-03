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

# Ahora, combinaciones_finales contiene todas las combinaciones en el formato original
# Puedes acceder a ellas o realizar otras operaciones según tus necesidades.

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

# Aplicar la función a cada lista interna
for lista_estudiantes in combinaciones_finales:
    # Reiniciar los cupos para cada lista interna
    materias_cupos_temp = materias_cupos.copy()
    
    asignaciones = generar_asignaciones(lista_estudiantes, materias_cupos_temp)
    
    # Imprimir las asignaciones para cada lista interna
    for estudiante, materias in asignaciones.items():
        print(f"{estudiante}: {', '.join(materias)}")
    print()
