# Algoritmo Mayor_menor
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

if A == B or B == C or A == C:
    print("Los valores deben ser diferentes entre sí.")
else:
    if A > B and A > C:
        print(f"El valor mayor es A: {A}")
    elif B > A and B > C:
        print(f"El valor mayor es B: {B}")
    else:
        print(f"El valor mayor es C: {C}")

    if A < B and A < C:
        print(f"El valor menor es A: {A}")
    elif B < A and B < C:
        print(f"El valor menor es B: {B}")
    else:
        print(f"El valor menor es C: {C}")