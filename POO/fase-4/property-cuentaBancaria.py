class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    