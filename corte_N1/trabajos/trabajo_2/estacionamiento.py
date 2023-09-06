costo_por_minuto = 139
iva = 0.19

tiempo_estacionado = int(input("Ingresa el tiempo en minutos: "))

total = tiempo_estacionado * costo_por_minuto
total_con_iva = total *iva
total_aproximado = ((total_con_iva + 49) // 50) * 50

print("El costo total es: $",total_aproximado)
