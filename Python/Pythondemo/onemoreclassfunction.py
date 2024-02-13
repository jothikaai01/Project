'''class phonenames():
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
'''
class Parent():
    def __init__(self):
        print("family name is bright services")
        
    def AadharAccess(self):
        print("Need Aadhar Access")
    def classroom(self):
        print("You can access Class room")
    def lab01(self):
        print("you can access lab 01")
    def lab02(self):
        print("you can access lab02")
    def aibatch(self):
        print("you can join AI course")
    def cadbatch(self):
        print("your can join Cloud application developer course")
    def nightshiftwork(self):
        print("you can join to work in the us process for us work timing")

class Child(Parent):
    def __init__(self):
        super().__init__()
        super().AadharAccess()
        super().lab01()
        super().lab02()
        super().aibatch()
        super().classroom()
        super().cadbatch()

        print("i am a student")

    def car(self):
        print("i do have BMW")

class visitor(Child):
    pass


# s=Child()


# s.car()

v=visitor()