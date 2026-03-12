def calcular_iva(precio):
    return precio * 0.15

print("Modulo de impuestos cargando!")

if __name__ == "__main__":
    print("Probando el modulo directamente...")
    print(f"Prueba de 100: {calcular_iva(100)}")