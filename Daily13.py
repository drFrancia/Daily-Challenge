class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            raise ValueError("La cantidad a depositar debe ser positiva")

    def consultar_saldo(self):
        return self.saldo

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.consultar_saldo())
