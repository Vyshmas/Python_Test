class product:
    id=78
    name="Amul"

    def display(self):
        print(f"ID:{self.id} \n Name:{self.name}")

class A(product):
    count=50
    category="butter"
    
    def display(self):
        super().display()
        print(f"count:{self.count} \n category:{self.category}")

class B(product):
    count=90
    category="milk"
    
    def display(self):
        super().display()

        print(f"count:{self.count} \n category:{self.category}")
    
class c(product):
    count=56
    category="choco"
    
    def display(self):
        super().display()
        print(f"count:{self.count} \n category:{self.category}")

p1=c()
print("C class deatils:")
p1.display()
p2=B()
print("B class deatils:")
p2.display()
p3=A()
print("A class deatils:")
p3.display()