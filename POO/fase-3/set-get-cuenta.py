class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self,nuevo_saldo):
        if nuevo_saldo >=0:
            self.__saldo = nuevo_saldo
        else:
            print("Error: el saldo no puede ser negativo")

cuenta1 = CuentaBancaria("juan", 90000)
print(cuenta1.get_saldo())

cuenta1.set_saldo(-70000)
print("Saldo actualizado: ", cuenta1.get_saldo())