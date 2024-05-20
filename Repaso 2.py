def cuenta_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] = frecuencia[palabra] + 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

frase = input("Ingrese frase para contar sus palabras: ")
frecuencia_palabras = cuenta_palabras(frase)
print(frecuencia_palabras)