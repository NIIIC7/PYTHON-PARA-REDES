class red():
    mascara = "/24"
    ipgw = "primer host disponible .1"
    ipred = ".0"
    ipbroadcast = ".255"
    shtudown = True

    def Prender(self):
        self.shutdown = False

    def valores(self):
        print("la mascara de tu red es",self.mascara)
        print("la gw de tu red es",self.ipgw)
        print("la ip de red es",self.ipred)
        print("la la ip boradcast utilizable es  ",self.ipbroadcast)
        print("la svi esta apagada",self.shtudown)


CCOGNOKIA = red()
CCOGNOKIA.valores()


LTEGHUAWEI = red()
LTEGHUAWEI.Prender()
LTEGHUAWEI.valores()
