#Crear una lista vacia con mi nombre y agregar 5 elementos con input:(Nombre, Preparatoria, Lugar de residencia, Edad, Carrera)

#Se crea una lista llamada lista de datos
lista_datos = []

print("Lista de Datos")
#Agrega dato
dato1 = input(" Nombre: ")
lista_datos.append(dato1)

#Agregar dato
dato2 = input("Preparatoria: ")
lista_datos.append(dato2)

#Agregar dato
dato3 = input("Lugar de residencia: ")
lista_dato.append(dato3)

#Agregar dato
dato4 = input("Edad: ")
lista_dato.append(dato4)

#Agregar dato
dato5 = input("Carrera: ")
lista_dato.append(dato5)

print("\n📌 Tu lista de datos es:")
for dato in lista_datos:
    print(f"- {dato}")

print("\n✅ ¡Lista creada con éxito!")