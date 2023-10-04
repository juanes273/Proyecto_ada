def asignacion_voraz(estudiantes, materias_cupos):
    
    asignaciones = {estudiante["nombre"]: [] for estudiante in estudiantes}
    
    # Ordenar las materias por prioridad descendente
    materias_ordenadas = sorted(materias_cupos.keys(), key=lambda x: sum([estudiante["prioridades"][x] for estudiante in estudiantes]), reverse=True)
    
    for materia in materias_ordenadas:
        estudiantes_disponibles = [estudiante for estudiante in estudiantes if materias_cupos[materia] > 0]
        estudiantes_disponibles = sorted(estudiantes_disponibles, key=lambda x: x["prioridades"][materia], reverse=True)
        
        for estudiante in estudiantes_disponibles:
            if materias_cupos[materia] > 0:
                asignaciones[estudiante["nombre"]].append(materia)
                materias_cupos[materia] -= 1
    
    return asignaciones
    

# Datos de entrada
materias_cupos = {
    "MateriaA": 2,
    "MateriaB": 3,
    "MateriaC": 2
}

estudiantes = [
    {"nombre": 'Estudiante1', 'prioridades': {'MateriaA': 1, 'MateriaB': 2, 'MateriaC': 3}},
    {"nombre": 'Estudiante2', 'prioridades': {'MateriaA': 2, 'MateriaB': 1, 'MateriaC': 3}},
    {"nombre": 'Estudiante3', 'prioridades': {'MateriaA': 3, 'MateriaB': 2, 'MateriaC': 1}},
]

asignaciones = asignacion_voraz(estudiantes, materias_cupos)

# Imprimir las asignaciones para cada estudiante
for estudiante, materias in asignaciones.items():
    print(f"{estudiante}: {', '.join(materias)}")