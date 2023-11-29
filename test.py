from estudiante import Estudiante
from libro import Libro
from pedido import Pedido
from revista import Revista

revista1 = Revista(211, 'Travis Griffin', 'National Geographic', 2021, 'Edelvives', True, 4)
libro2 = Libro(id=16, codigo='CP73L', titulo='La Sombra del Viento', autor='Carlos Ruiz Zafón', disponible=True,
               cantidad_disponible=7, tipo_pasta='Dura')
estudiante = Estudiante(cedula="0931054233", nombre="Melanie", apellido="Gusqui", email="melaniegusqui@gmail.com",
                        telefono="0997079658", direccion="Pradera 2", numero_libros=1, activo=True,
                        carrera="Gestión de la información gerencial")
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