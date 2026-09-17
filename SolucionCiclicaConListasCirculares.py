class Nodo:
    def __init__(self, codigo, meta, linea_base, valor_esperado):
        self.codigo = codigo
        self.meta = meta
        self.linea_base = linea_base
        self.valor_esperado = valor_esperado
        self.siguiente = None

class ListaCircular:

    def __init__(self):
        self.ultimo = None


    def agregar(self, codigo, meta, linea_base, valor_esperado):

        nuevo = Nodo(codigo, meta, linea_base, valor_esperado)

        # Si la lista está vacía
        if self.ultimo is None:

            self.ultimo = nuevo
            nuevo.siguiente = nuevo

        # Si la lista ya tiene elementos
        else:

            nuevo.siguiente = self.ultimo.siguiente
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo


    def mostrar(self):

        if self.ultimo is None:
            print("La lista está vacía.")
            return

        actual = self.ultimo.siguiente

        print("\n========== METAS DE MOVILIDAD ==========")

        while True:

            print("\nCódigo:", actual.codigo)
            print("Meta:", actual.meta)
            print("Línea base:", actual.linea_base)
            print("Valor esperado:", actual.valor_esperado)

            actual = actual.siguiente

            if actual == self.ultimo.siguiente:
                break


    def buscar(self, codigo):

        if self.ultimo is None:
            print("La lista está vacía.")
            return

        actual = self.ultimo.siguiente

        while True:

            if actual.codigo == codigo:

                print("\n========== META ENCONTRADA ==========")
                print("Código:", actual.codigo)
                print("Meta:", actual.meta)
                print("Línea base:", actual.linea_base)
                print("Valor esperado:", actual.valor_esperado)

                return

            actual = actual.siguiente

            if actual == self.ultimo.siguiente:
                break

        print("\nNo se encontró la meta", codigo)


    def recorrer_ciclos(self, cantidad):

        if self.ultimo is None:
            print("La lista está vacía.")
            return

        actual = self.ultimo.siguiente

        print("\n========== RECORRIDO CIRCULAR ==========")

        for i in range(cantidad):

            print(actual.codigo, "->", end=" ")

            actual = actual.siguiente

        print("...")


metas = ListaCircular()


metas.agregar(
    "STM02",
    "Elaborar 1 documento de planeación para la promoción de la movilidad activa y sostenible en Cundinamarca.",
    0,
    1
)

metas.agregar(
    "STM03",
    "Elaborar el estudio de factibilidad del sistema público de bicicletas.",
    0,
    1
)

metas.agregar(
    "STM04",
    "Elaborar el estudio de factibilidad para la movilidad eléctrica en el Departamento.",
    0,
    1
)

metas.agregar(
    "STM06",
    "Formular el Plan Maestro de Movilidad del Departamento.",
    0,
    1
)

metas.agregar(
    "STM07",
    "Asistir técnicamente la formulación o actualización de 4 Planes Maestros de Movilidad de los municipios del Departamento.",
    0,
    4
)

metas.agregar(
    "STM11",
    "Apoyar financieramente la implementación del sistema ferroviario eléctrico Regiotram de Occidente.",
    1,
    1
)

metas.agregar(
    "STM12",
    "Estructurar un documento de alternativas de alimentación interurbana de pasajeros al sistema Regiotram del Occidente y del Norte.",
    0,
    1
)

metas.agregar(
    "STM13",
    "Formular el Plan Maestro de Transporte Intermodal de Cundinamarca.",
    0,
    1
)

metas.agregar(
    "STM14",
    "Estructurar el Cable aéreo en Soacha.",
    0,
    1
)

metas.agregar(
    "STM15",
    "Estructurar la consolidación de los estudios de factibilidad de la Línea 3 del Metro.",
    0,
    1
)

metas.agregar(
    "STM16",
    "Estructurar 4 soluciones de movilidad para las interconexiones regionales del Departamento.",
    0,
    4
)

metas.agregar(
    "STM17",
    "Apoyar la estructuración del Sistema Integrado de Transporte Público de Soacha.",
    0,
    1
)

metas.agregar(
    "STM18",
    "Estructurar un documento de esquemas alternativos de financiación para los sistemas de transporte público del Departamento.",
    0,
    1
)

metas.agregar(
    "STM19",
    "Apoyar financieramente la operación del ente gestor de los proyectos de transporte masivo regional.",
    0,
    1
)

metas.agregar(
    "STM20",
    "Realizar la estructuración integral del proyecto Regiotram Norte.",
    0,
    1
)

metas.agregar(
    "STM21",
    "Apoyar financieramente la implementación del sistema de transporte masivo BRT en Soacha en la Fase II.",
    1,
    1
)

metas.agregar(
    "STM22",
    "Estructurar el sistema de transporte masivo BRT en Soacha en la Fase IV.",
    0,
    1
)

while True:

    print("\n========================================")
    print(" SISTEMA DE METAS DE MOVILIDAD")
    print("========================================")
    print("1. Mostrar todas las metas")
    print("2. Buscar una meta")
    print("3. Recorrer la lista circular")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        metas.mostrar()

    elif opcion == "2":

        codigo = input("\nIngrese el código de la meta (ejemplo STM02): ")
        metas.buscar(codigo.upper())

    elif opcion == "3":

        cantidad = int(input("\n¿Cuántos nodos desea recorrer?: "))
        metas.recorrer_ciclos(cantidad)

    elif opcion == "4":

        print("\nPrograma finalizado.")
        break

    else:

        print("\nOpción no válida.")
