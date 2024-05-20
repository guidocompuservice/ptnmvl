Algoritmo Numero_a_letras
	Escribir "Ingrese la calificación numérica del alumno:"
	Leer calificacionNumerica
	Si calificacionNumerica >= 90 y calificacionNumerica <= 100 Entonces
		notaAlfabetica = 'A'
	Sino Si calificacionNumerica >= 70 y calificacionNumerica < 90 Entonces
			notaAlfabetica = 'B'
		Sino Si calificacionNumerica >= 50 y calificacionNumerica < 70 Entonces
				notaAlfabetica = 'C'
			Sino Si calificacionNumerica >= 30 y calificacionNumerica < 50 Entonces
					notaAlfabetica = 'D'
				Sino Si calificacionNumerica >= 0 y calificacionNumerica < 30 Entonces
						notaAlfabetica = 'E'
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si	
	Escribir "La nota alfabética es:", notaAlfabetica
FinAlgoritmo
