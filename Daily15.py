class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def describir(self):
        return (f"Motor {self.tipo} con {self.potencia} caballos de fuerza")

class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_auto(self):
        return f"{self.marca} {self.modelo} con {self.motor.describir()}"

motor = Motor(tipo="V8", potencia=450)
auto = Auto(marca="Ford", modelo="Mustang", motor=motor)

print(auto.describir_auto()) 
