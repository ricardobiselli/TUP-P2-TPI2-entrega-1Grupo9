from datetime import date

class Archivo():
    def __init__(self, nombre: str, formato: str) -> None:
        self._nombre = nombre
        self._fecha = date.today()
        self._formato = formato
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
        
    @property
    def formato(self):
        return self._formato
    
    @formato.setter
    def formato(self, formato):
        self._formato = formato
        
    def __str__(self) -> str:
        return f"{self.nombre} - ({self.formato}) - fecha: {self.fecha}"
    