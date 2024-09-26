class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.inventario = []
        self.puntos_vida = 100
        self.nivel = 1
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")
    
    def atacar(self):
        print('Atacar!')

juan = Personaje('juan','mago')
juan.atacar()

#TODO coche con 4 ruedas, carroceria, 5 asientos y 1 motor
#TODO 2 ruedas, 1 asiento y 1 motor.

class Vehiculo:
    def __init__(self, ruedas: int, asientos: int, motor: int):
        self.ruedas = ruedas
        self.asientos = asientos
        self.motor = motor

class coche(Vehiculo):
    def __init__(self, ruedas: int, asientos: int, motor: int, carroceria: str):
        super().__init__(self, ruedas, asientos, motor)
        self.carroceria = carroceria