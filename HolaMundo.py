#Este es un comentario
print("Hola Mundo")
#operadores aritmeticos
print (4+6)

#precedencia de operadores
print (5+8*(3+2))

#tipo de datos
print(type(2))
print(type(8.62))
print(type("Texto"))
#variables
mensaje = "esto es un mensaje"
print(mensaje)
mensaje = "mensaje modificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)

textoUno = "mi texto"
textoDos = "mi segundo texto"

print(textoUno + textoDos)

#str() int() float()
edad = 20
print("la edad del usuario es: " + str(edad) )
print("el tipo de dato de edad es " + str(type(edad))) 

import math

grados = 45
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("seno de 45° : " + str (seno))

def saludar(nombre):
    print("Hola "+ nombre) 
    print("Como estas")
    print("te saludo de lejos x el virus u.u")
def despedir():
    print ("ya me voy")
    print ("ya que pase eso nos abrazamos")

def concatenar (parte1, parte2):
    return parte1 + parte2

print ("esto no es parte d la funcion")
saludar ("Rominice")
despedir()

frase = concatenar ("Hola ", "Adios")
print (frase)