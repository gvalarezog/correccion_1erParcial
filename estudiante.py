from persona import Persona


#INTEGRANTES
#MELANIE GUSQU PALLO - FREDDY CROFFORD VILLAO

class Estudiante(Persona):
    _contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, idES=int,
                 nivel=int):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.idES = idES
        self.nivel = nivel
        Estudiante._contador_estudiante += 1

    @property
    def idES(self):
        return self._idES

    @idES.setter
    def idES(self, idES):
        self._idES = idES

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def contador_estudiante(self):
        return Estudiante._contador_estudiante

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
        return f"Estudiante(cedula={self.cedula}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, telefono={self.telefono}, direccion={self.direccion}, numero_libros={self.numero_libros}, activo={self.activo}, carrera={self.carrera}, idES={self.idES}, nivel={self.nivel}, contador_estudiantes={self._contador_estudiante})"

if __name__ == "__main__":
    estudiante1 = Estudiante(cedula="0931054233", nombre="Melanie", apellido="Gusqui", email="melaniegusqui@gmail.com", telefono="0997079658", direccion="Pradera 2", numero_libros=1, activo=True, carrera="Gestión de la información gerencial", idES=101, nivel=3)
    print(estudiante1)
    estudiante1 = Estudiante(cedula="0957808181", nombre="Freddy", apellido="Crofford", email="crovillpapo@gmail.com", telefono="0978759219", direccion="Chambers y avenida del ejército",numero_libros=3, activo=True, carrera="Gestión de la información gerencial", idES=202, nivel=3)
    print(estudiante1)
