def calcular_pago(num_piezas, precio_unitario):
    monto_total = num_piezas * precio_unitario
    
    if monto_total > 500000:
        inversion_empresa = monto_total * 0.55
        prestamo_banco = monto_total * 0.30
        credito_fabricante = monto_total * 0.15
    else:
        inversion_empresa = monto_total * 0.70
        prestamo_banco = 0
        credito_fabricante = monto_total * 0.30
    
    interes_fabricante = credito_fabricante * 0.20
    total_credito_fabricante = credito_fabricante + interes_fabricante
    
    return {
        "Número de piezas": num_piezas,
        "Precio unitario": precio_unitario,
        "Monto total": monto_total,
        "Inversión de la empresa": inversion_empresa,
        "Préstamo del banco": prestamo_banco,
        "Crédito al fabricante": total_credito_fabricante,
        "Intereses del fabricante": interes_fabricante
    }


def main():
    try:
        num_piezas = int(input("Ingrese el número de piezas a comprar: "))
        precio_unitario = float(input("Ingrese el precio unitario de la pieza: "))
        
        resultado = calcular_pago(num_piezas, precio_unitario)
        
        print("\nResumen de la compra:")
        for clave, valor in resultado.items():
            print(f"{clave}: {valor:.2f}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()
