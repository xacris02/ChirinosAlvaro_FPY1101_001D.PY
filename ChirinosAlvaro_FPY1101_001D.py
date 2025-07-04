productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
'FS1230HD':["Asus", 17, "8GB","SSD","1T","AMD Ryzen 7", "Nvidia GTX1660"]}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],}
def stock_marca(marca):
    global stock
    global productos
    contador_aux = 0
    stock_aux = 0
    for n in productos:
        if marca in productos[n]:
            contador_aux += 1 
            stock_aux += stock[n][1]
    if contador_aux == 0:
        print("La marca no se encuentra en nuestra tienda.")
    else:
        print(f"El stock es: {stock_aux}")
def buscar_por_precio(p_min,p_max):
    global stock
    lista_notebooks = []
    for n in stock:
        if p_min <= stock[n][0] <= p_max:
            lista_notebooks.append(f"{productos[n][0]}--{n}")
    if lista_notebooks == []:
        print("No hay notebooks en ese rango de precios.")
    else:
        print(sorted(lista_notebooks))
def actualizar_precio(modelo,p):
    global stock
    if modelo not in stock: 
        return False
    else:
        stock[modelo][0] = p
        return True
while True:
    try:
        opcion = int(input("*** MENU PRINCIPAL ***\n1. Stock marca.\n2. Búsqueda por precio.\n3. Actualizar precio.\n4. Salir.\nIngrese una opción: "))
        if opcion not in [1,2,3,4]:
            print("Debe seleccionar una opción válida!!")
        else:
            if opcion == 1:
                marca = input("Ingrese marca a consultar: ")
                if marca in ["asus","dell","ASUS","DELL"]:
                    marca = marca.capitalize()
                elif marca in ["hp","Hp"]:
                    marca = marca.upper()
                elif marca in ["LENOVO", "Lenovo"]:
                    marca = marca.swapcase()
                stock_marca(marca)
            elif opcion == 2:
                while True:
                    try:
                        p_min = int(input("Ingrese precio mínimo: "))
                        p_max = int(input("Ingrese precio máximo: "))
                        if p_max <= p_min:
                            print("El precio máximo no puede ser menor o igual al mínimo.")
                        else:
                            buscar_por_precio(p_min,p_max)
                            break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
            elif opcion == 3:
                while True:
                    try:
                        modelo = input("Ingrese modelo a actualizar: ")
                        nuevo_precio = int(input("Ingrese precio nuevo: "))
                        if nuevo_precio <= 0:
                            print("El nuevo precio no puede ser un numero negativo o 0")
                        else: 
                            if actualizar_precio(modelo,nuevo_precio) == True:
                                print("Precio actualizado!!")
                            elif actualizar_precio(modelo,nuevo_precio) == False:
                                print("El modelo no existe!!")
                            continuar = input("Desea actualizar otro precio (s/n)?: ")
                            if continuar == "no":
                                break
                    except ValueError:
                        print("Ingresar solo enteros")
            else:
                print("Programa finalizado.")
                break  
    except ValueError:
        print("Debe ingresar valores enteros!!")