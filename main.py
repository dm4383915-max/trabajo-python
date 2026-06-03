from src.estadistica import calcular_promedio
from src.estadistica import promedio_diccionario
from src.estadistica import contar_aprobados
from src.estadistica import clasificar_notas

datos =[10,15,20,25,30]

resultado = calcular_promedio(datos)

print("El promedio de la lista es:", resultado)

notas = {
    "Juan": 3.3,
    "Ana": 4.2,
    "Pedro": 2.8,
    "Maria": 4.5
}


promedio_notas = promedio_diccionario(notas)
print("El promedio de las notas es:", promedio_notas)

aprobados = contar_aprobados(notas, 4)
print("El número de aprobados es:", aprobados)

clasificacion_notas = clasificar_notas(notas)
print("La clasificacion de las notas es: ",clasificacion_notas)