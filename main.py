def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

print("Porfavor elige una operacion")
print("1.sumar")
print("2.restar")
print("3.multiplicar")
print("4.dividir")

while True:

    operacion = input("Porfavor indrodusca una operacion: ")

    if operacion in ('1', '2', '3', '4'):

        numero1 = float(input("Porfavor introdusca el primer numero: "))
        numero2 = float(input("Porfavor introdusca el segundo numero: "))

        if operacion == "1":
            print(numero1, "+", numero2, "=", sumar(numero1, numero2))

        elif operacion == "2":
            print(numero1, "-", numero2, "=", restar(numero1, numero2))

        elif operacion == "3":
            print(numero1, "*", numero2, "=", multiplicar(numero1, numero2))

        elif operacion == "4":
            print(numero1, "/", numero2, "=", dividir(numero1, numero2))

        siguente_operacion = input("Deseas hacer mas operaciones (si/no): ")

        if siguente_operacion == "no":
            print("Gracias por utilizar mi programa :)")
            break
    else:
        print("Error: Porfavor introduce una operacion valida!")