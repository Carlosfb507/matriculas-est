class Persona:
    def _init_(self, nombre, edad, direccion):
        self._nombre = nombre
        self._edad = edad
        self._direccion = direccion

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def _str_(self):
        return f"El nombre del estudiante es {self._nombre}, su edad es: {self._edad}, y vive en {self._direccion}"