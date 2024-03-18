import os
import numpy as np 

asientos = np.zeros((10,10), dtype=object)
lista_asistentes = np.zeros((1,1), dtype=int)
cuenta = 1
numero_platinum = 0
numero_gold = 0
numero_silver = 0
for i in range(10):
    for e in range(10):
        asientos[i][e] = str(cuenta)
        cuenta = cuenta + 1    
def mostrar_asientos():
    print ("Precios:")
    print ("PLATINUM (Asientos del 1 al 20): $120.000")
    print ("GOLD (Asientos del 21 al 50): $80.000")
    print ("SILVER (Asientos del 51 al 100): $50.000")
    print('-------------------------------')
    print('-----------ESCENARIO-----------')
    print('-------------------------------')
    for i in range(1):
        print (asientos[i][0],"", asientos[i][1], "",asientos[i][2],"",  asientos[i][3],"",  asientos[i][4],"",  asientos[i][5],"", asientos[i][6],"", asientos[i][7],"", asientos[i][8],"",asientos[i][9])  
    for i in range(1,10):
        print (asientos[i][0], asientos[i][1], asientos[i][2], asientos[i][3], asientos[i][4], asientos[i][5],asientos[i][6],asientos[i][7],asientos[i][8],asientos[i][9])    


def comprar_entradas():
    menu3 = 1
    while menu3==1:
        os.system('cls')
        print ("¿Cuantas entradas desea comprar (NO SE PUEDEN COMPRAR MAS DE 3 ENTRADAS)")
        try:
            numero_entradas = int(input())
        except ValueError:
            os.system('cls')
            print("El valor ingresado no es valido, vuelva a intentarlo")
            input("Presione enter para continuar")
        else:
            if numero_entradas == 1:
                    while menu3==1:
                        os.system('cls')
                        mostrar_asientos()
                        print ("Seleccione el asiento:  ")
                        try:
                            asiento = int(input(input))
                        except ValueError:
                            os.system('cls')
                            print("El valor ingresado no es valido, vuelva a intentarlo")
                            input("Presione enter para continuar")
                        else:
                            os.system('cls')
                            if asiento < 0 or asiento > 100:
                                print ("El asiento elegido no esta disponible, vuelva a intentarlo")
                                print ("Presione enter para continuar")
                                input()
                            else:
                                
                                pasar = 1
                                for i in range(10):
                                    for e in range(10):
                                        if asientos[i][e] == str(asiento):
                                                print ("Ingrese el rut para el asignar al asiento seleccionado (SIN COMAS, PUNTOS NI DIGITO VERIFICADOR)")
                                                try:
                                                    rut = int(input())
                                                except ValueError:
                                                    os.system('cls')
                                                    print("El valor ingresado no es valido, vuelva a intentarlo")
                                                    input("Presione enter para continuar")
                                                else:
                                                    os.system('cls')
                                                    asistente_lista = np.zeros((1,1), dtype=int)
                                                    asistente_lista[0][0] = rut
                                                    if asiento > 0 and asiento < 21:
                                                        print ("El precio es: $120.000")
                                                        input("Presione enter para confirmar la compra")
                                                    elif asiento > 20 and asiento < 51:
                                                        print ("El precio es: $80.000")
                                                        input("Presione enter para confirmar la compra")
                                                    elif asiento > 50:
                                                        print ("El precio es: $50.000")
                                                        input("Presione enter para confirmar la compra")
                                                    os.system('cls')
                                                    print ("El asiento seleccionado ha sido comprado con exito")
                                                    print ("Presione enter para continuar")
                                                    input()
                                                    menu3=2
                                                    asientos[i][e] = 'X'
                                                    return asistente_lista          
                                                    break
                                                            
                                        else:
                                                    pasar = pasar + 1
                                                    os.system('cls')
                                                    if pasar == 101:
                                                        print("El asiento ingresado no es valido, vuelva a intentarlo")
                                                        print("Presione enter para continuar")
                                                        input()

                
            elif numero_entradas == 2 or numero_entradas == 3:
                asistente_lista3 = np.zeros((1,1), dtype=int)
                precio_final = 0
                while menu3<numero_entradas+1:
                                os.system('cls')
                                mostrar_asientos()
                                print ("Seleccione el asiento:  ")
                                try:
                                    asiento = int(input())
                                except ValueError: 
                                    os.system('cls')
                                    print ("El valor ingresado no es valido, vuelva a intntearlo")
                                    input("Presione enter para continuar")
                                else:

                                    if asiento < 0 or asiento > 100:
                                        os.system('cls')
                                        print ("El asiento elegido no esta disponible, vuelva a intentarlo")
                                        print ("Presione enter para continuar")
                                        input()
                                    else:
                                        os.system('cls')
                                        pasar = 1
                                        for i in range(10):
                                            for e in range(10):
                                                os.system('cls')
                                                if asientos[i][e] == str(asiento):
                                                    print ("Ingrese el rut para el asignar al asiento seleccionado (SIN COMAS, PUNTOS NI DIGITO VERIFICADOR)")
                                                    try:
                                                        rut = int(input())
                                                    except ValueError: 
                                                        os.system('cls')
                                                        print ("El valor ingresado no es valido, vuelva a intntearlo")
                                                        input("Presione enter para continuar")
                                                    else:
                                                        os.system('cls')
                                                        asistente_lista2 = np.zeros((1,1), dtype=int)
                                                        asistente_lista2[0][0] = rut
                                                        asistente_lista3 = np.append(asistente_lista3, asistente_lista2)
                                                        if asiento > 0 and asiento < 21:
                                                            print ("El precio es: $120.000")
                                                            input("Presione enter para confirmar la compra")
                                                            precio_final = precio_final + 120000
                                                        elif asiento > 20 and asiento < 51:
                                                            print ("El precio es: $80.000")
                                                            input("Presione enter para confirmar la compra")
                                                            precio_final = precio_final + 80000
                                                        elif asiento > 50:
                                                            print ("El precio es: $50.000")
                                                            input("Presione enter para confirmar la compra")
                                                            precio_final = precio_final + 50000
                                                        os.system('cls')
                                                        print ("El asiento seleccionado ha sido comprado con exito")
                                                        print ("Presione enter para continuar")
                                                        
                                                        asientos[i][e] = 'X'
                                                        input() 
                                                        menu3= menu3+1
                                                else:
                                                    pasar = pasar + 1
                                                    if pasar == 101:
                                                        print("El asiento ingresado no es valido, vuelva a intentarlo")
                                                        print("Presione enter para continuar")
                                                        input()
                print ("El precio final es:$"+str(precio_final))
                input ("Presione enter para confirmar la compra")
                return asistente_lista3
            else:
                print ("El numero ingresado no es valido, vuelva a intentarlo")
                print("Presione enter para continuar")
                input()
def ganancias_totales():
    numero_platinum = 0
    numero_gold = 0
    numero_silver = 0
    for i in range (2):
        for e in range (10):
            if asientos[i][e] == 'X':
                numero_platinum = numero_platinum + 1
    for i in range (2,5):
        for e in range (10):
            if asientos[i][e] == 'X':
                numero_gold = numero_gold + 1
            
    for i in range (5,10):
        for e in range (10):
            if asientos[i][e] == 'X':
                numero_silver = numero_silver + 1
    numero_final = numero_platinum + numero_gold + numero_silver
    dinero_platinum = 120000 * numero_platinum
    dinero_gold = 80000 * numero_gold
    dinero_silver = 50000 * numero_silver
    dinero_total = dinero_platinum + dinero_gold + dinero_silver
    print ("Tipo de Entrada        Cantidad          Total")
    print ("Platinum $120.000","    ", numero_platinum,"               ", dinero_platinum)
    print ("Gold $80.000","         ", numero_gold, "               ",dinero_gold)
    print ("Silver $50.000","       ", numero_silver, "               ",dinero_silver)
    print ("Total                 ", numero_final,"               ", dinero_total )
    input("Presione enter para continuar")

    
            
    
def listado():
    print ("Lista de asistenes por su rut: ")
    lista_final = np.sort(lista_asistentes)
    for i in range(len(lista_asistentes)):
            if lista_final[i] == 0:
                pass
            else:
                print (lista_final[i])
    input("Presione enter para continuar")

                                
menu1= 1
while menu1==1:
    os.system('cls')
    print ("Bienvenido a Creativos.CL")
    print ("Ingrese una opcion:")
    print ("1. Comprar entradas")
    print ("2. Mostrar ubicaciones disponibles")
    print ("3. Ver listado de asistentes")
    print ("4. Mostrar ganancias totales")
    print ("5. Salir")
    try:
        opcion = int(input())
    except ValueError:
        print("La opcion ingresada no es valida, vuelva a intentarlo")
        input("Presione enter para continuar")
    if opcion == 1:
        asistente_lista = comprar_entradas()
        lista_asistentes = np.append(lista_asistentes, asistente_lista)
    elif opcion == 2:
        print("Listado de asientos:")
        mostrar_asientos()
        input("Presione enter para continuar")
    elif opcion == 3:
        listado()
    elif opcion == 4:
        ganancias_totales()
    elif opcion==5:
        print ("Gracias por usar el sistema")
        print ("El sistema ahora esta apagandose...")
        print ("Sistema hecho por: Pablo Figueroa Ojier")
        print ("Fecha en la que se hizo el trabajo: 10/07/2023")
        print("Presione enter para continuar")
        input()
        menu1 =2
    else:
        print("La opcion ingresada no es valida, vuelva a intentarlo")
        input("Presione enter para continuar")
    
    
