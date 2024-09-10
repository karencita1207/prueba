





# Cantidades conocidas
harina_conocida = 80  # en kg
pan_conocido = 120    # en kg

# Cantidad de pan deseado
pan_deseado = 99      # en kg

# Calcular la harina necesaria para el pan deseado
harina_necesaria = (harina_conocida / pan_conocido) * pan_deseado

# Mostrar el resultado
print(f"Para hacer {pan_deseado} kg de pan se necesitan {harina_necesaria:.2f} kg de harina.")
