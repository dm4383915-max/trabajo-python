# class CuentaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
        # self.__saldo = saldo con el doble __ se coloca un atributo privado



# cuenta1 = CuentaBancaria("juan", 300000)
# cambien o actualiza el saldo
# cuenta1.saldo = -50000 


# print(cuenta1.saldo)
# print(cuenta1.__dict__)

class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo

cuenta1 = CuentaBancaria("juan", 90000)
print(cuenta1._CuentaBancaria__saldo)
cuenta1.__saldo = -300000
print(cuenta1.__saldo)
        

