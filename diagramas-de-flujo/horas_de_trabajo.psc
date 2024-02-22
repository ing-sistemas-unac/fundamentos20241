Algoritmo horas_de_trabajo
	Definir horas_chambeadas, sueldo, seguridad_social Como Real
	Escribir "Ingresa cuántas horas has chambeado este mes"
	Leer horas_chambeadas
	sueldo = horas_chambeadas * 4833
	seguridad_social = sueldo * (8.5/100)
	Escribir "Tu sueldo es ", sueldo, " y el pago de seguridad es ", seguridad_social, ", tristemente lo que realmente recibes es ", sueldo - seguridad_social
FinAlgoritmo
