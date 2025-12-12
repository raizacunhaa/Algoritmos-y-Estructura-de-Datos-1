
def calcular_promedio_sueldos(sueldos):
    suma_sueldos = 0
    for x in range (len(sueldos)):
        suma_sueldos = suma_sueldos + int(sueldos[x])
    promedio = suma_sueldos / len(sueldos)
    print('El promedio de los sueldos es: ', promedio)
    return promedio

def obtener_empleado_sueldo_max(empleados, sueldos):
    sueldo_max = 0
    for x in range (len(sueldos)):
        if sueldo_max < int(sueldos[x]):
            sueldo_max = int(sueldos[x])
            empleado_sueldo_max = empleados[x]
    print('El empleado con mayor sueldo es: ', empleado_sueldo_max)
    return empleado_sueldo_max
    
def ordenar_por_sueldo(empleados, sueldos):
    for y in range (len(sueldos)-1):
        for x in range (len(sueldos)-1):
            if int(sueldos[x]) > int(sueldos[x+1]):
                auxiliar = sueldos[x+1]
                sueldos[x+1] = sueldos[x]
                sueldos[x] = auxiliar
                auxiliar = empleados[x+1]
                empleados[x+1] = empleados[x]
                empleados[x] = auxiliar
    print('Lista de empleados ordenados por sueldo', empleados, sueldos)
    return [empleados,sueldos]

#Bloque principal
cant= int(input("Ingrese la cantidad de empleados: "))
empleados = []
sueldos = []
for x in range (cant):
    empleados.append(input("Ingrese el nombre del empleado: "))
    sueldos.append(input("Ingrese el sueldo del empleado: "))

promedio_sueldos = calcular_promedio_sueldos(sueldos)
empleado_sueldo_max = obtener_empleado_sueldo_max(empleados, sueldos)
orden = ordenar_por_sueldo(empleados, sueldos)
