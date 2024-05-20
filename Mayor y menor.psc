Algoritmo Mayor_menor
	Escribir "Ingrese el valor de A:"
	Leer A
	Escribir "Ingrese el valor de B:"
	Leer B
	Escribir "Ingrese el valor de C:"
	Leer C
	Si A = B o B = C o A = C Entonces
		Escribir "Los valores deben ser diferentes entre sí."
	Sino
		Si A > B y A > C Entonces
			Escribir "El valor mayor es A:", A
		Sino Si B > A y B > C Entonces
				Escribir "El valor mayor es B:", B
			Sino
				Escribir "El valor mayor es C:", C
			Fin Si
			
			Si A < B y A < C Entonces
				Escribir "El valor menor es A:", A
			Sino Si B < A y B < C Entonces
					Escribir "El valor menor es B:", B
				Sino
					Escribir "El valor menor es C:", C
				Fin Si
			Fin Si
		Fin Si
	Fin Si	
FinAlgoritmo
