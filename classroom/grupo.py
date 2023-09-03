from classroom.asignatura import Asignatura
from multimethod import multimethod

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
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
        return f'Grupo de estudiantes: {self._grupo}'
    @ classmethod
    def asignarNombre(cls, nombre=None):
        if nombre==None:
            cls.grado="Grado 6"
            return
        cls.grado=nombre