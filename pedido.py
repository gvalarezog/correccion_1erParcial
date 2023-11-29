
from datetime import datetime

from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista


#INTEGRANTES
#MELANIE GUSQU PALLO - FREDDY CROFFORD VILLAO

class Pedido():
    contador_pedido = 0

    def __init__(self, id_pedido=None, solicitante=None, lista_material=None, materia=None, fecha_prestamo=None, fecha_devolucion=None):
        Pedido.contador_pedido += 1
        self._id_pedido = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        # self._nombre_solicitante = None


    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def solicitante(self):
        return self._solicitante

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, nuevo_lista_material):
        self._lista_material = nuevo_lista_material

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nuevo_fecha_prestamo):
        self._fecha_prestamo = nuevo_fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nuevo_fecha_devolucion):
        self._fecha_devolucion = nuevo_fecha_devolucion

    @property
    def nombre_solicitante(self):
        return self._nombre_solicitante

    @nombre_solicitante.setter
    def nombre_solicitante(self, nuevo_nombre):
        self._nombre_solicitante = nuevo_nombre

    def pedir_material(self, material):
        self._lista_material = material
        self._fecha_prestamo = datetime.now()
        self._fecha_devolucion = None
        if self._solicitante:
            self._nombre_solicitante = self._solicitante.nombre
            print(f"Se ha realizado el préstamo del material {self._lista_material} a {self._nombre_solicitante}.")

    def devolver_material(self):
        if self._solicitante:
            self._fecha_devolucion = datetime.now()
            print(f"Se ha devuelto el material {self._lista_material} de {self._nombre_solicitante}.")
        else:
            print("No hay material para devolver o no se ha registrado un solicitante.")


if __name__ == '__main__':
    # Caso con Revista y Estudiante
    revista1 = Revista(211, 'Travis Griffin', 'National Geographic', 2021, 'Edelvives', True, 4)
    libro2 = Libro(id=16, codigo='CP73L', titulo='La Sombra del Viento', autor='Carlos Ruiz Zafón', disponible=True,
                   cantidad_disponible=7, tipo_pasta='Dura')
    estudiante = Estudiante(cedula="0931054233", nombre="Melanie", apellido="Gusqui", email="melaniegusqui@gmail.com",telefono="0997079658", direccion="Pradera 2",  numero_libros=1, activo=True, carrera="Gestión de la información gerencial")
    lista_pedido = list()
    lista_pedido.append(libro2)
    lista_pedido.append(revista1)
    pedido1 = Pedido(solicitante=estudiante, lista_material=lista_pedido)
    # print(pedido1)

    print(f'Solicitante: {pedido1.solicitante.nombre} {pedido1.solicitante.apellido}')
    print(f'Materiales Pedidos:\n')
    # print(pedido1.lista_material)
    for material in pedido1.lista_material:
        print(f'\tTitulo: {material.titulo}')
    # pedido1.pedir_material(revista1)
    # # print(f"Fecha de préstamo: {pedido1.fecha_prestamo}")
    # #
    # # pedido1.devolver_material()
    # # print(f"Fecha de devolución: {pedido1.fecha_devolucion}")
    # #
    # # # Caso con Libro y Docente
    # # libro1 = Libro(101, 'Shelby Mahurin', 'Asesino de Brujas', 2018, 'Puck', True, 19)
    # # docente = Docente(cedula="0974321421", nombre="Mercedes", apellido="Mendoza", email="mercemend@hotmail.com",telefono="0987235117", direccion="Acacias",  numero_libros=3, activo=True, carrera="Ciencias de la Computación", id_docente="DOC001", titulo_3er_nivel="Ph.D. en Ciencias de la Computación", titulo_4to_nivel="")
    # #
    # # pedido2 = Pedido(solicitante=docente)
    #
    # pedido2.pedir_material(libro1)
    # print(f"Fecha de préstamo: {pedido2.fecha_prestamo}")
    #
    # pedido2.devolver_material()
    # print(f"Fecha de devolución: {pedido2.fecha_devolucion}")