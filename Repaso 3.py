def cuenta_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] = frecuencia[palabra] + 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def palabra_mas_repetida(frecuencia):
    palabra_repetida = max(frecuencia, key=frecuencia.get)
    return (palabra_repetida, frecuencia[palabra_repetida])

frase = input("Ingrese frase para contar sus palabras: ")
frecuencia_palabras = cuenta_palabras(frase)
print(f"Las palabras y sus frecuencias son: {frecuencia_palabras}")

palabra_frecuencia = palabra_mas_repetida(frecuencia_palabras)
print(f"La palabra más repetida es: '{palabra_frecuencia[0]}' con una frecuencia de: {palabra_frecuencia[1]}")

def palabras_mas_repetidas(frecuencia):
    maxima_frecuencia = max(frecuencia.values())
    palabras_frecuentes = [(palabra, freq) for palabra, freq in frecuencia.items() if freq == maxima_frecuencia]
    return palabras_frecuentes

frecuencia_palabras = cuenta_palabras(frase)
palabras_frecuentes = palabras_mas_repetidas(frecuencia_palabras)
print(f"Las palabras más repetidas y sus frecuencias son: {palabras_frecuentes}")