
# def grados ():
    
#     usuario = float(input("Ingresa la temperatura en grados: "))
#     temperatura = (usuario - 32)/1.8
#     print(f"su temperatura en farenheit es: {temperatura}")

# def area ():

#     base1 = float(input("Por favor ingresa la base ->: "))
#     altura1 = float(input("Por favor ingresa la altura ->: "))

#     base = (base1 * altura1)/2

#     print(f"El area del triangulo es igual a: {base} ")

def Mayor ():

    numero =[]
    continuar = True
    while continuar:
        usuario =int(input("Por favor ingresa un numero permitido ->"))
        numero.append(usuario)
        salir = str(input("Deseas ingresar otro numero? si/no \n "))
        if salir == "no":
            continuar = False
            print(max(numero))


   


            

            