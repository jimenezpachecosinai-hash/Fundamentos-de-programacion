import json

#Colocar en ISBN de los libros
biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    "978-84-164-4092-0":{
         "título": "La razon de estár contigo",
         "autor": ["W. Bruce Cameron"],
         "géneros":["Novela contemporánea","Ficción","Narrativa de animales"]
    },
    "841-62-4092-2":{
         "título":"Las cinco personas que te encotrarás en el cielo",
         "autor":["Mitch Albom"],
         "géneros":["Narrativa espiritual y filosófica", "Fábula contemporánea"]
    }, 
    "978-60-738-6051-2":{
         "título":"Cadáver exquisito",
         "autor":["Agustina María Bazterrica"],
         "géneros":["Distopía","Ficción contemporánea","Terror social"]
    }   
}
#Seleccionar libro deseado para buscarlo
isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)