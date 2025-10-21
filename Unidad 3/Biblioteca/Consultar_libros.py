def Consultar_libros():
    try:
        with open("libros.txt", "r", encoding="utf-8") as f:
            libros = f.readlines()

        if libros:
            print("\nLista de libros:")
            for linea in libros:
                try:
                    titulo, autor = linea.strip().split(",", 1)
                    print(f" {titulo} — {autor}")
                except ValueError:
                    print("Linea con el formato esta mal:", linea.strip())
        else:
            print("No hay libros registrados.")
            
    except FileNotFoundError:
        print(" Aún no existe el archivo de libros.")


