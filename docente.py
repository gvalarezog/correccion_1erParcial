from persona import Persona


#INTEGRANTES
#MELANIE GUSQU PALLO - FREDDY CROFFORD VILLAO

class Docente(Persona):
    _contador_docente=0

    def __init__(self, cedula :str ,nombre :str ,apellido :str ,email :str ,telefono :str ,direccion :str
                 ,numero_libros :int ,activo :bool ,carrera :str, id_docente:int, titulo_3er_nivel:str, titulo_4to_nivel:str):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self._id_docente=id_docente
        self._titulo_3er_nivel=titulo_3er_nivel
        self._titulo_4to_nivel=titulo_4to_nivel
        Docente._contador_docente+=1

    @property
    def contador_docente(self):
        return Docente._contador_docente

    @property
    def id_docente(self):
        return self._id_docente

    @id_docente.setter
    def id_docente(self, nuevo_id):
        self._id_docente=nuevo_id

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, nuevo_titulo):
        self._titulo_3er_nivel=nuevo_titulo

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, nuevo_titulo):
        self._titulo_4to_nivel=nuevo_titulo

    def pedir_libro(self):
        self._contador_estudiante += 1
        return True

    def devolver_libro(self):
        if self._contador_estudiante > 0:
            self._contador_estudiante -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"Docente(cedula={self.cedula}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, telefono={self.telefono}, direccion={self.direccion}, numero_libros={self.numero_libros}, activo={self.activo}, carrera={self.carrera}, id_docente={self.id_docente}, titulo_3er_nivel={self.titulo_3er_nivel}, titulo_4to_nivel={self.titulo_4to_nivel}, contador_docente={self.contador_docente})"

if __name__ == "__main__":
    docen1 = Docente(cedula="0690024187", nombre="Javier", apellido="Macias", email="javimacias@gmail.com", telefono="0995321105", direccion="Alborada", numero_libros=1, activo=True, carrera="Gestión de la información gerencial", id_docente=129, titulo_3er_nivel="si", titulo_4to_nivel="no")
    print(docen1)
    docen2 = Docente(cedula="0974321421", nombre="Mercedes", apellido="Mendoza", email="mercemend@hotmail.com", telefono="0987235117", direccion='Acacias',numero_libros=3, activo=True, carrera="Gestión de la información gerencial", id_docente=103, titulo_3er_nivel="si", titulo_4to_nivel="si")
    print(docen2)
