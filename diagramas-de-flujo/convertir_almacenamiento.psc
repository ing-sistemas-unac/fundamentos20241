Algoritmo convertir_almacenamiento
	Definir gb, tb, kb Como Real
	Escribir "Ingresa la cantidad de GB que deseas convertir a TB y KB"
	Leer gb
	tb = gb / 1024
	kb = gb * 1024 * 1024
	Escribir gb, " GB equivale a ", tb, " TB y ", kb, " KB." 
FinAlgoritmo
