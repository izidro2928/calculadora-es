def sumar(x, y):
  return x + y

while True:

  operacion = input("Porfavor indrodusca una operacion: ")

  if operacion in ('1', '2', '3', '4'):

    numero1 = float(input("Porfavor introdusca el primer numero: "))
    numero2 = float(input("Porfavor introdusca el segundo numero: "))

    if operacion == "1":
      print(numero1, "+", numero2, "=", sumar(numero1, numero2))

    siguente_operacion = input("Deseas hacer mas operaciones (si/no): ")

    if siguente_operacion == "no":
      break