'''class student:
    def __init__(self,name,age,sec):
        self.name=name
        self.age=age
        self.sec=sec
        # method that executes when an obj is created
        print(name,age,sec)
obj=student("sri","20","b")
obj1=student("vas","40","b")'''


class ece:
    def sec1(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print(name,rollno)
        

    def sec2(self,n,rno,age):
        self.n=n
        self.rno=rno
        self.age=age
        print(n,rno,age)
obj=ece()
obj.sec1("SRI","90")
obj.sec2("POORNA","85","b")

