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