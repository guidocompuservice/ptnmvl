def iva_total(factura,iva):
    total_facturado=float(factura)+float(factura)*float(iva)/100
    return total_facturado

factura=input("Importe de la factura?: ")
iva=input("Porcentaje de IVA?: ")
if not iva:
    iva=21
total=iva_total(factura,iva)
print("El total de la factura con IVA incluido es:", total)