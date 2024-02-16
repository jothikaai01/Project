class phonenames():
    def __init__(self) :
        print("Phone Names")

    def vivo(self):
       print("Vivo Phone")
    def oppo(self):
        print("Oppo Phone")
    def tecno(self):
        print("Tecno Phone")

class phos2(phonenames):
    def __init__(self):
        super().__init__()
        super().oppo()
        super().vivo()
        super().tecno()
        print("--------------\n")
    def samsung(self):
        print("Samsung Phone")

class newphones(phos2):
    pass

#ph=phos2()
#ph.samsung()

nphn=newphones()
