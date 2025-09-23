#Crear un diccionario con los siguientes datos
Edades = {
    "Brayan": 25,
    "Luis": 30,
    "José": 22
}
print("Edad de Luis:", Edades["Luis"])    
Edades["Brayan"] = 28
print("\nDespués de añadir a Brayan:")
print(Edades)  
#Se añadio un nuevo dato
Edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(Edades)    
#Eliminando un dato del diccionario
del Edades["José"]
print("\nDespués de eliminar a José:")
print(Edades)                               
#El diccionario se recorrera
print("\nRecorriendo el diccionario:")
for Nombre, Edad in Edades.items():         
     print(f"{Nombre} tiene {Edad} años")