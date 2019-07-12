def numero():

 while true:
    x =int(raw_input("ingrese un numero('*' para terminar)"))
    if x == '*':
        break
    elif x > 0:
         print "numero positivo"

    elif x == 0:
         print "igual a 0"

    else:
        print "numero negativo"
        

a = int(raw_input("escribe un numero:"))
if a == 10:
    print "has escrito 10"
elif a < 10:
    print "escribiste numero menor a 10"
elif a != 10:
    print "no has escrito 10"


from random import randint



def generar_lista(tam):
    lista =[]

    while len(lista)<3:
        numero = randint(1,9)
        if numero not in lista:
            lista.append(numero)

    return lista

def suma(lista):
    acum = 0
    for i in lista:
        acum+=i
    return acum
    
