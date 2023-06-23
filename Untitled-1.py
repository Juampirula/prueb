import random
while True:
    print ("----MENÚ----")
    print ("1 grabar")
    print ("2 buscar")
    print ("3 imprimir certificados")
    print ("4 salir")
    opcion= int(input("ingrese una opcion"))
    print 
    if opcion== 1:
        vehiculos_=[]
        tipo=input("ingrese tipo")
        patente=input("ingrese patente")
        if len(patente) >= 2 or len(patente)<=10:
            print("no ingreso bien la patente, debe tener entre 2 a 10 caracteres")

        marca=input("ingrese marca")
        precio=input("ingrese precio")
        multas=int(input("ingrese multas con su fecha"))
        fecha_registro=input("ingrese fecha de registro")
        nombre_dueño=input("ingrese nombre del propietario")
        
        vehiculos
        [
        {
        tipo:tipo,
        patente:patente,
        marca:marca,
        precio:precio,
        multas:multas,
        fecha_registro:fecha_registro,
        nombre_dueño:nombre_dueño
        }]
        vehiculos.append(vehiculos)
    if opcion ==2:
        print ([vehiculos])
        print
        for vehiculos in nombre_dueño:
            print({nombre_dueño})
            print({patente})

    if opcion ==3:
        print("imprimir certificados, que certificado desea imprimir?")
        valor= random.randint(1500,3000)
        print("usted debe pagar por impuesto verde un valor de"+valor+ "ademas debe cancelar el precio de"+multas+"pague rapido o muera")
        
        
    if opcion==4:
        print("gracias por usar auto seguro, hasta pronto")
        break

    

