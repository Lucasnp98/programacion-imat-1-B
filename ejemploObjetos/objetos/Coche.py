from excepciones import MatriculaError


class Coche:
    def __init__(self, modelo, color, matricula, km):
        self.modelo = modelo
        self.color = color
        self.km = km
        self.enmarcha = False

        error = True
        if len(matricula) == 7:
            error = False

        if not error:
            self.matricula = matricula
        else:
            raise MatriculaError(
                "La matricula debe ser de longitud 7, la instancia del coche no se ha creado correctamente")

    def arrancar(self):
        self.enmarcha = True

    def apagar(self):
        self.enmarcha = False

    def __str__(self):
        return f"{self.modelo} Color : ({self.color}) - Matricula: {self.matricula} - {self.km} Km - marcha:  {self.enmarcha}"
