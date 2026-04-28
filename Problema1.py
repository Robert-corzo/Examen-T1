class Puesto:
    def __init__(self, codigo=0, descripcion="", area="", plazas=0, sueldo=0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.area = area
        self.plazas = plazas
        self.sueldo = sueldo


# 🔹 BUSCAR DUPLICADO
def buscaPuesto(lista, nuevo):
    for p in lista:
        if (p.codigo == nuevo.codigo or
            p.descripcion == nuevo.descripcion or
            p.area == nuevo.area):
            return True
    return False

def ordBurbuja(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j].codigo < lst[j+1].codigo:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def ordInsercionSueldo(lst):
    for i in range(1, len(lst)):
        aux = lst[i]
        j = i - 1
        while j >= 0 and lst[j].sueldo < aux.sueldo:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = aux

def buscaBinariaSueldo(lst, sueldo):
    izq = 0
    der = len(lst) - 1

    while izq <= der:
        mid = (izq + der) // 2
        if lst[mid].sueldo == sueldo:
            return mid
        elif lst[mid].sueldo < sueldo:
            der = mid - 1
        else:
            izq = mid + 1
    return -1

def ordSeleccionTotal(lst):
    n = len(lst)
    for i in range(n):
        posMayor = i
        for j in range(i + 1, n):
            total_j = lst[j].plazas * lst[j].sueldo
            total_m = lst[posMayor].plazas * lst[posMayor].sueldo

            if total_j > total_m:
                posMayor = j

        lst[i], lst[posMayor] = lst[posMayor], lst[i]

lista = []

while True:
    opc=int(input("1-Agregar, 2-Listar, 3-Borrar codigo, 4-Buscar por sueldo, 5-Puesto contratar, 9-Salir --->"))

    if opc == 1:
        codigo = int(input("Codigo: "))
        descripcion = input("Descripcion: ")
        area = input("Area: ")
        plazas = int(input("Plazas: "))
        sueldo = float(input("Sueldo: "))

        if len(descripcion) < 3 or len(area) < 3:
            print("Debe tener minimo 3 letras")
            continue

        if codigo <= 0 or plazas <= 0 or sueldo <= 0:
            print("Debe ser numeros mayores a 0")
            continue

        nuevo = Puesto(codigo, descripcion, area, plazas, sueldo)

        if buscaPuesto(lista, nuevo):
            print("Ya existe el puesto")
        else:
            lista.append(nuevo)
            print("Agregado")

    elif opc == 2:
        for p in lista:
            print(p.codigo, p.descripcion, p.area, p.plazas, p.sueldo)

    elif opc == 3:
        cod = int(input("Codigo a borrar: "))

        ordBurbuja(lista)

        for p in lista:
            if p.codigo == cod:
                lista.remove(p)
                print("Eliminado")
                break

    elif opc == 4:
        ordInsercionSueldo(lista)
        s = float(input("Sueldo: "))
        pos = buscaBinariaSueldo(lista, s)
        if pos >= 0:
            i = pos
            while i >= 0 and lista[i].sueldo == s:
                print(lista[i].codigo, lista[i].descripcion)
                i -= 1
            i = pos + 1
            while i < len(lista) and lista[i].sueldo == s:
                print(lista[i].codigo, lista[i].descripcion)
                i += 1
        else:
            print("No encontrado")

    elif opc == 5:
        dinero = float(input("Monto total: "))

        ordSeleccionTotal(lista)

        total = 0
        for p in lista:
            costo = p.plazas * p.sueldo
            if total + costo <= dinero:
                print(p.codigo, p.descripcion, "Total:", costo)
                total += costo

        print("Total usado:", total)

    elif opc == 9:
        print("Fin")
        break
