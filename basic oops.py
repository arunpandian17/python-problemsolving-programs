class company:
    def __init__(self,no,name,pos,sal,loc):
        self.no=no
        self.name=name
        self.pos=pos
        self.sal=sal
        self.loc=loc
    def display(self):

        print("ID",self.no)
        print("name", self.name)
        print("position", self.pos)
        print("Salary", self.sal)
        print("Location", self.loc)
        
    def search(a):
        if b1.no==a:
            b1.display()
        elif b2.no==a:
            b2.display()
        elif b3.no==a:
            b3.display()
        elif b4.no==a:
            b4.display()
        

l=list()
b1=company("1","Suresh","Software eng","25000","chennai")
b2=company("2","Roshini","AEO","15000","chennai")
b3=company("3","madhu","Business analyst","50000","chennai")
b4=company("4","satheesh","CA","75000","guntur")



l.append(b1)
l.append(b2)
l.append(b3)
l.append(b4)

a=int(input())
b=company
b.search(a)





