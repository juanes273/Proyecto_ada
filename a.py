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
