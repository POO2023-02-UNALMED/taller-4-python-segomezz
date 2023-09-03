from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if asignaturas is None:
            self._asignaturas=[]
        self.listadoAlumnos = estudiantes
        if estudiantes is None:
            self.listadoAlumnos=[]
        

    def listadoAsignaturas(self, **kwargs):
        signature=[]
        for x in kwargs.values():
            signature.append(x)
            self._asignaturas=signature

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos = lista

    def __str__(self):
        group="Grupo de estudiantes: "+self._grupo
        return group

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    