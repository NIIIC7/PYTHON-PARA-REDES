class red():
    def __init__(self):
        self.__mascara = "/24"
        self.__ipgw = "primer host disponible .1"
        self.__ipred = ".0"
        self.__ipbroadcast = ".255"
        self.__shutdown = True
    def Prender(self):
        self.__shutdown = False
    def valores(self):
        print("la mascara de tu red es",self.__mascara)
        print("la gw de tu red es",self.__ipgw)
        print("la ip de red es",self.__ipred)
        print("la la ip boradcast utilizable es  ",self.__ipbroadcast)
        print("la svi esta apagada",self.__shutdown)

class redHuawei(red):
    pass
class redJuniper(red):
    pass




#CCOGNOKIA = red()
#CCOGNOKIA.valores()
#CCOGNOKIA.mascara("defr")
#
#LTEGHUAWEI = red()
#LTEGHUAWEI.Prender()
#LTEGHUAWEI.valores()

TRESTHUAWEI = redHuawei()
TRESTHUAWEI.Prender()
TRESTHUAWEI.valores()


cuatroJuniper=redJuniper()
cuatroJuniper.Prender()
cuatroJuniper.valores()


