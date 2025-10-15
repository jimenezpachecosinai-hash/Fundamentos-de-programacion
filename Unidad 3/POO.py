{
  "metadata": {
    "kernelspec": {
      "name": "xpython",
      "display_name": "Python 3.13 (XPython)",
      "language": "python"
    },
    "language_info": {
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "version": "3.13.1"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "64d8182c-01ee-4672-a7b1-bb6383cbb195",
      "cell_type": "code",
      "source": "class Libro:\n    def __init__(self, titulo, autor):\n        self.titulo = titulo          # atributo de instancia\n        self.autor = autor            # atributo de instancia\n        self.disponible = True        # atributo de estado\n\n    def prestar(self):\n        if self.disponible:\n            self.disponible = False\n            print(f'«{self.titulo}» ha sido prestado.')\n        else:\n            print(f'Lo siento, «{self.titulo}» ya está prestado.')\n\n    def devolver(self):\n        if not self.disponible:\n            self.disponible = True\n            print(f'«{self.titulo}» ha sido devuelto.')\n        else:\n            print(f'«{self.titulo}» ya estaba en la estantería.')\n\n    def __str__(self):\n        estado = 'Disponible' if self.disponible else 'Prestado'\n        return f'\"{self.titulo}\" de {self.autor} [{estado}]'\n\n\nclass Biblioteca:\n    def __init__(self):\n        self.catalogo = []   # lista vacía para guardar libros\n\n    def agregar_libro(self, libro):\n        self.catalogo.append(libro)\n\n    def buscar_por_titulo(self, titulo):\n        resultados = [l for l in self.catalogo if titulo.lower() in l.titulo.lower()]\n        return resultados\n\n    def mostrar_catalogo(self):\n        print(\"\\nCatálogo de la biblioteca:\")\n        for libro in self.catalogo:\n            print(\"  -\", libro)\n\n\nif __name__ == \"__main__\":\n    # Creamos la biblioteca y algunos libros\n    bib = Biblioteca()\n    bib.agregar_libro(Libro(\"Cien años de soledad\", \"Gabriel García Márquez\"))\n    bib.agregar_libro(Libro(\"Don Quijote de la Mancha\", \"Miguel de Cervantes\"))\n    bib.agregar_libro(Libro(\"El Principito\", \"Antoine de Saint-Exupéry\"))\n\n    # Mostramos el catálogo completo\n    bib.mostrar_catalogo()",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "\nCatálogo de la biblioteca:\n  - \"Cien años de soledad\" de Gabriel García Márquez [Disponible]\n  - \"Don Quijote de la Mancha\" de Miguel de Cervantes [Disponible]\n  - \"El Principito\" de Antoine de Saint-Exupéry [Disponible]\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "57918f9d-2e2f-4ce2-a1d1-43caf0343254",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}