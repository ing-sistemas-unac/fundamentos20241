Algoritmo calcular_hipotenusa
	// Definir las variables como real para que acepten decimales
	Definir valor_a, valor_b, hipotenusa Como Real
	// Uso Escribir para mostrar un mensaje al usuario que usará el programa
	Escribir 'Ingrese el valor de a'
	// Creo una variable para recibir el valor de a
	Leer valor_a
	Escribir 'Ingrese el valor de b'
	Leer valor_b
	hipotenusa <- RAIZ((valor_a*valor_a)+(valor_b*valor_b))
	Escribir 'La hipotenusa es ', hipotenusa
FinAlgoritmo
