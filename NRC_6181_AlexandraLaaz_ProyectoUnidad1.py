"""
Aplicacion de delivery para comidas rapidas
"""
#operador que permite tomar el primer elemento de objeto al igual a una lista 
from operator import itemgetter

"""
La primera esta funcion con nombre  menu la que no requiere de parametros en donde 
se mostrara una bienvenida y nombre del sowftware y las opciones a escoger
     ***Primera opcion permite el inicio de secion del cliente
     ***Segunda opcion permitira al cliente hacer su pedido
"""


def Menu():
    """
    Se hace la utilidad de un bclu While not 
    la cual es in bucle infinito, en el cual si ingresa mal 
    o una opcion a parte de las que estan, siguira pidiendo el dato 
    hasta que ingrese uno correcto.
    """
    opcion='0'
    print("****** BIENVENIDOS A EASY SERVICE ******")
    print("1.- Inicio seccion") 
    print("2.- Mirar el menu de comida")
    while not (opcion == '2'):# bucle infinito mientras que el valor de la condicion devuelva false
        opcion=int(input("Ingrese una opcion del menu a presentar: "))
        if (opcion == 1):
            print("***** OPCION 1 INICIO SESION *****")
            Cliente()#Llama a la clase Cliente
            
        if (opcion == 2):
            print("***** OPCION 2 *****")
            Restaurant() #Invocacion a la funcio restaurant
            


"""
 En esta parte se le pide al cliente
 ingresar un ID al cliente para iniciar
 sesion, en caso que no sea dato correcto se 
 pasara a realizar el registro---para aquello
 se utiliza if
"""
class Cliente():
    def __init__(self):
        """

        """
        nombreApellidos=[ ]
        dirDomicilio=[ ]
        telefono=[ ]
        cedula=[ ]
        print("******Recordar que para cliente ya registrados su ID es 123******")
        cedulaIngresada=int(input( "Bienvenid@s, ingresar el ID  de usuario: " ))
        IdCliente = 123
        if (cedulaIngresada == IdCliente):
            print ("Hola querido ** Cliente registrado**")
            MenuPedidos()#Llamado o invocacion a la clase MenuPedidos

        else:
            print("Cliente no registrado") 
            print("Iniciar con el registro de datos para que sea nuestro cliente" )
            nombreApellidos=str(input( "Nombres Apellidos: " ))
            dirDomicilio=str(input( "Dirrecion de domicilio: " ))
            telefono=str(input( "Telefono: "))
            cedula=int(input( "Cedula: " ))
            print( "===========================================================================================")
            print( " *** REGISTRO SATISFACTORIO, DESDE AHORA ERES NUESTRO/A CLIENTE *** ", nombreApellidos )
            print("============================================================================================")
            print("****Recuerde que despues del registro su ID sera el numero de cedula******")
            cedulaIngresada=int(input( "Bienvenid@s, ingresar el ID de usuario: " ))
            IdCliente = cedula
            lista=['Nombre Apellido','  Direccion Domicilio',' Numero de telefono',' Numero de cedula']
            list=[nombreApellidos,dirDomicilio,telefono,cedula]
            """
            Extend nos ayudara agregar
            elementos de una lista
            """
            print(lista)
            print(list)
            MenuPedidos()#Llamado a la clase MenuPedidos

"""
La siguiente funcion nos permite 
leer el archivo y nos devuelve una 
lista de restaurantes de comida rapida

*Se tiene el metodo split()-->el cual toma
        una cadena de caracteres y segun el parametro
        del metodo divira la cadena y convierte
        cada uno de los elementos en una lista
"""
def Leer_restaurant():
    archivo=open("restaurant.txt","r")
    lista=[ ]
    for linea in archivo:
        linea_archivo=linea.split("-")
        lista.append(linea_archivo)
    archivo.close()#Ayuda a cerrar el archivo para despues poder utilizarlo
    return lista

"""

"""
def imprimir_menu(lista_Restaurant):
    if lista_Restaurant:
        encabezado='{:>12} {:>12} {:>12}'.format('nombre','comida','precio')
        print(encabezado)
        print("-"*45)
        
        for item in lista_Restaurant:
            item_precio="$",item[2]
            """
            El metodo format--> agrega a la cadena una serie de llaves 
                    para indicar a python lo que se va agregar en esas llaves
            """
            linea='{:>12} {:>12} {:>12}'.format(item[0],item[1],item_precio)
            print(linea)
    else:
        print("No se ha encontrado ninguna lista")



"""
En la parte de REstaurant tendremos un menu 
en el cual se puede:
    *Listar --> Permite ordenar por nombre y precio, tambien podra ver la lista del menu,
                segunda la respuesta o opcion escogida por el usuario ordenara la lista
                por el indice esfecifico
    *Buscar --> Permite buscar la comida ya sea por nombre de Restaurant o Comida,
                si dicho elemento ingresado por el usuario se encontado en el item 
                devolvera toda la linea completa con los datos que se encuentra en ese item del archivo.
    *Agregar --> Permite agragar mas alimento a las lista del menu del restaurant
en donde las opciones tendra un valor de None--eso es para indicar que va estar vacio
dicho objeto.
Metodo lower():la cual pasa la cadena de caracter en minuscula
"""
def Restaurant():
    opRestaurant=None
    print("Listar --> Permite ordenar por nombre y precio, tambien podra ver la lista del menu")
    print("Buscar --> Permite buscar la comida ya sea por nombre de Restaurant o Comida")
    print("Agregar --> Permite agragar mas alimento a las lista del menu del restaurant")
   
    while opRestaurant != "salir":
        opRestaurant=input("Elija una opcion: ")
        opRestaurant=opRestaurant.lower()
        
        if opRestaurant=="listar":
            opLista=None
           
            while opLista!= "salir":
                opLista="Puede ordenar el menu por: Nombre, Comida y por Precio "
                opLista=opLista.lower()
                lista_Restaurant=Leer_restaurant #Permite leer todos los restaurantes de la lista
                """
                    **El metodo sort ayuda a ordenar los elementos de manera ascendente
                    **El parametro key los cual es una funcion clave que la ordenacion requiere
                        y eso se lo da el operador itemgetter ya que toma el primer elemento de un objeto 
                        al igual a una lista
                """
                if opLista=="nombre":
                    lista_Restaurant.sort(key=itemgetter(0))
                    imprimir_menu(lista_Restaurant)
                
                elif opLista=="comida":
                    lista_Restaurant.sort(key=itemgetter(1))
                    imprimir_menu(lista_Restaurant)
               
                elif opLista=="precio":
                    lista_Restaurant.sort(key=itemgetter(2))
                    imprimir_menu(lista_Restaurant)
                
                elif opLista=="salir":
                    print("***Regresa al menu principal de Restaurant***")
                
                else :
                    print("**Opcion elejida no valida***")
        
        elif opRestaurant=="buscar":
            opBuscar=None
            
            while opBuscar!="salir":
                opBuscar=input("Ingrese el nombre del Restaurant o Comida a buscar: ")
                opBuscar=opBuscar.lower()
               
                if opBuscar!= "salir":
                    lista_Restaurant=Leer_restaurant
                    encontrado=[ ]
                   
                    for item in lista_Restaurant:
                        if opBuscar in item:
                            encontrado.append(item)
                    
                    if encontrado:
                        imprimir_menu(encontrado)
                    
                    else:
                        print("No existe el Restaurant o comida a buscar.....")        
        
        elif opRestaurant=="agregar":
            MenuPedidos()
        
        elif opRestaurant=="salir":
            print("A salido del menu....")
        else:
            print("OPCION ESCOGIDA NO VALIDA......")

    

"""
En esta parte se muestra el menu de pedido de los alimientos,
en donde le cliente eligira 
uno de su gusto
"""   
def MenuPedidos():
    print("Agrega un elemento nuevo al menu del software  ")
    restaurant=input("Ingrese nombre del restaurant: ")
    comida=input("Ingrese el nombre del palto de comida: ")
    precio=input("Ingrese el precio de la comida: ")
    nueva_lista=str(restaurant.lower(),"-",comida.lower(),"-",precio)
    archivo=open("restaurant.txt",'a')
    archivo.write(nueva_lista)
    archivo.close()
    print("Se ha agrega una nueva comida al menu Nombre de restaurant: ",restaurant,
         " comida ",comida," precio ",precio)

    cantidad=int(input("Ingrese productos desea comprar: "))
    contador +=1
    if(contador<=cantidad):
        precio=float(print("El precio a paagar:",contador))
        totalPagar=1*precio
        totalCompra=totalCompra+totalPagar
        return cantidad
    print("==============================================================================")
    print("El precio a pagar por sus productos es de[",totalCompra,"] Dolares")
    print("==============================================================================")
    PagoPedidos()

class Pedidos():
    def __init__(self):
        """
        En el caso de no ser 
        registrado y solo desea realizar 
        su pedido, se pide los datos 
        como nommbre apellido, numero cedula,
        numero telefono y la direccion
        """
        """
        se crea un objeto cliente la cual 
        esta asignado las clase Cliente()
        para que dicho objeto pueda tomar 
        las propiedades de la clase
        """
        cliente=Cliente()
        cliente.nombreApellidos=str(input("Ingrese su nombre y apellido: "))
        cliente.cedula=int(input("Ingrese su numero de cedula: "))
        cliente.telefono=str(input("Ingrese su numero de telefono: "))
        cliente.dirDomicilio=str(input("Ingres su direccion de domicilio: "))
        #lista.append(cliente)
       
        """
        Se hace un llamado a la clase 
        MenuPedidos para que el cliente pueda ver los 
        productos disponibles y escoja el que le guste
        """
        MenuPedidos()


class PagoPedidos():
    def __init__(self):
        seleccion='0'
        print("****** EASY SERVICE ---- MODOS DE PAGO ******")
        print("1.- Pago en efectivo") 
        print("2.- Pago mediante transferencia")
        print("3._ Pago con tarjeta de credito")
        while not (seleccion == '3'):# bucle infinito mientras que el valor de la condicion devuelva false
            seleccion=int(input("Ingrese una opcion para el modo de pago que desee: "))
           
            if (seleccion == 1):
                print("***** OPCION 1 PAGO EN EFECTIVO *****")
                dinero=float(input("Ingrese cuanto Dinero :"))

                if(dinero > MenuPedidos.totalCompra):
                    print("Usted si tiene el dinero suficiente para poder pagar[",MenuPedidos.totalCompra,"]Dolares")
                    cambio=dinero-MenuPedidos.totalCompra
                    print("Su cambio es:",cambio," Dolares")
                
                elif (dinero<MenuPedidos.totalCompra & dinero>0):
                    print("Usted no tiene el dinero suficiente para poder pagar ",MenuPedidos.totalCompra,"] Dolares")
                
                elif dinero < 0:
                    print("No puede ingresar numeros negativos")
            
            if (seleccion == 2):
                print("***** OPCION 2 PAGO CON TRANSFERENCIA *****")
                CuentaCliente=str(input("Ingrese su numero de cuenta: "))
                CuentaEasy=str(input("Ingrese el numero de cuenta del destinatario: "))

            if (seleccion == 3):
                print("***** OPCION 3 PAGO CON TARJETA DE CREDITO *****")
                tarjeta=str(input("Ingrese el numero de su tarjeta: "))
                fechaTarjeta=str(input("Ingrese la fecha de expediciòn de su tarjeta: "))


"""
if __name__=='__main__' ayuda a indicar al intérprete 
de Python que lo que debe ejecutar al lanzarse por consolar
"""

if __name__ == '__main__':
    Menu()