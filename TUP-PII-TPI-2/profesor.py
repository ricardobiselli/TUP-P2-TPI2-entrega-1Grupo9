from usuario import Usuario
from curso import listado_cursos

class Profesor(Usuario):
    
    def __init__(self, titulo: str, anio_egreso: int, nombre: str, apellido: str, email: str, password:str): 
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        super().__init__(nombre, apellido, email, password)
        
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def anio_egreso(self):
        return self._anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, value):
        self._anio_egreso = value

    def __str__(self):
        pass

    def dictar_curso(self, objeto_activo, nuevo_objeto_curso):  
        objeto_activo._mis_cursos.append(nuevo_objeto_curso)
        listado_cursos.append(nuevo_objeto_curso)
