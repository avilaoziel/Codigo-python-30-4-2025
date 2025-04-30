'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def preparar_datos(info):
  # Supone que 'info' será un conjunto, pero realmente espera una lista (LISTA PARA MEZCLAR DATOS CON GUIONES)
  acumulador = ""
  for letra in info:
      acumulador += letra + "-"
  return acumulador[:-1]
def mezcla_datos(a, b):
   # Compara dos cosas que no se deberían comparar directamente(SE COMPARAN SEGUN EL NOMBRE)
  if a > b:
     return a + b
  elif a == b:
     return a * 2
  else:
   return b + a
def iniciar():
 entrada1 = input("Ingresa un valor de referencia textual: ")
 entrada2 = input("Ingresa otra unidad: ")
 x = preparar_datos(entrada1) # ¿Por qué usar esto aquí?(PARA LLAMAR A LA FUNCION)
 y = preparar_datos(entrada2)
 resultado = mezcla_datos(x, y)
 print("Resultado no final: ", resultado)
 # El siguiente bloque debe imprimir solo si 'entrada1' está en 'entrada2'(EN CASO DE COINCEDENCIA)
 if entrada1 in entrada2:
     print("Coincidencia detectada.") # Error intencional de indentación(MARCA EL ERROR DEBIDO A lA COINCEDENCIA)
iniciar()