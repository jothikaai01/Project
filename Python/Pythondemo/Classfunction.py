class schoolclass:
    def __init__(self,headmaster,assistanthm,teacher):
        self.hm=headmaster;
        self.ahm=assistanthm;
        self.teach=teacher;
    def welcome(self):
        print("\n-----------------------------")
        print(self.hm,self.ahm,self.teach)
x=schoolclass("Jegan","Manjula","Jayshree")
x.welcome()
print("-----------------------------")

class sclclass(schoolclass):
    def __init__(self, headmaster, assistanthm, teacher,schoolpeopleleader,assistentsclplleader):
        self.sclplder=schoolpeopleleader;
        self.asssclplder=assistentsclplleader
        super().__init__(headmaster, assistanthm, teacher)
    def meeting(self):
        print("Good Moring HM",self.hm, "And AHM",self.ahm,"And Teacher",self.teach,"Staff Meeting Arranged by",self.sclplder,"And",self.asssclplder)
y=sclclass("'Jegan'","'Manjula'","'Jayshree'","'Kowsalya'","'Sandhiya'")
y.meeting()
print("-----------------------------\n")