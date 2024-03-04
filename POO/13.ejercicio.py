class Red:
    def __init__(self, nombre, ipred, mascara):
        self.nombre = nombre
        self.ipred = ipred
        self.mascara = mascara
        self.__ipgw = None
        self.__shutdown = True

    def prender(self):
        self.__shutdown = False

    def asignar_gateway(self, ipgw):
        self.__ipgw = ipgw

    def valores(self):
        print(f"Nombre de la red: {self.nombre}")
        print(f"Dirección IP de red: {self.ipred}")
        print(f"Máscara de subred: {self.mascara}")
        if self.__ipgw:
            print(f"Dirección IP del gateway: {self.__ipgw}")
        else:
            print("Gateway no configurado")
        print("SVI está apagada" if self.__shutdown else "SVI está encendida")


class RedHuawei(Red):
    pass


class RedJuniper(Red):
    pass


# Creamos instancias de las clases RedHuawei y RedJuniper
red1 = RedHuawei("RedHuawei", "192.168.1.0", "255.255.255.0")
red2 = RedJuniper("RedJuniper", "10.0.0.0", "255.255.255.0")

# Configuramos el gateway para cada red
red1.asignar_gateway("192.168.1.1")
red2.asignar_gateway("10.0.0.1")

# Encendemos las redes
red1.prender()
red2.prender()

# Mostramos la información de las redes
red1.valores()
print("\n")
red2.valores()
