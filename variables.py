#En python las variables pueden cambiar de tipo
#Como en la mayoria de los lenguajes dinámicos
var_one = 42
var_one = "karen"
print(var_one)

#cambiar tipos de variables
var_two = 50
var_two_str = str(var_two)
var_two_float = float(var_two)
print(var_two_str)
print(var_two_float)

#Obteniendo el tipo de la variable
print(type(var_two))
print(type(var_two_str))
print(type(var_two_float))

#Los nombres de las variables no puden tener espacios
# ni operaciones matemáticas y tampoco partir con un número

# 2var = 42 esto estaria malo las variables no pueden partir por un numero
# my-var = 42 esto tambien estaria malo por usar la resta
# my var = 42 estaria malo por usar espacio