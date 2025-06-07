class College:
    name="NCCS"
    
    @classmethod
    def changeName(self,name):
        self.name=name


c1=College()
c1.changeName("Prime College")
print(c1.name)