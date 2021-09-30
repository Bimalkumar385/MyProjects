#SINGLE INHERITANCE

class Brands:
    def brand_name(self,name):
        print(name,"is an",end=" ")

class Products(Brands):
    def product_name(self,name):
        print(name)

obj=Products()
obj.brand_name("Amazon")
obj.product_name("Online Ecommerce Store")





#MULTIPLE INHERITANCE

class Brands:
    def brand_name(self,name):
        print(name,"is an",end=" ")

class Products:
    def product_name(self,name):
        print(name,"popularity of",end=" ")

class Popularity(Brands,Products):
    def popularity_value(self,name):
        print(name)
obj=Popularity()
obj.brand_name("Amazon")
obj.product_name("Online Ecommerce Store")
obj.popularity_value(100)





#MULTILEVEL INHERITANCE

class Brands:
    def brand_name(self,name):
        print(name,"is an",end=" ")

class Products(Brands):
    def product_name(self,name):
        print(name,"popularity of",end=" ")

class Popularity(Products):
    def popularity_value(self,name):
        print(name)
obj=Popularity()

obj.brand_name("Amazon")
obj.product_name("Online Ecommerce Store")
obj.popularity_value(100)




#HIERARCHICAL INHERITANCE

class Brands:
    def brand_name(self,name):
        print(name,"is an",end=" ")

class Products(Brands):
    def product_name(self,name):
        print(name,"popularity of",end=" ")

class Popularity(Brands):
    def popularity_value(self,name):
        print(name,"Values:",end=" ")

class Value(Brands):
    def value_product(self,name):
        print(name)
obj=Popularity()
obj1=Products()
obj2=Value()
obj.brand_name("Amazon")
obj1.product_name("Online Ecommerce Store")
obj.popularity_value(100)
obj2.value_product("Excellent")




#HYBRID INHERITANCE

class PC:
    def fun1(self):
        print("This is PC class")

class Laptop(PC):
    def fun2(self):
        print("This laptop class inheriting PC class")

class Mouse(Laptop):
    def fun3(self):
        print("This mouse is inheriting Laptop class")

class Student(Mouse,Laptop):
    def fun4(self):
        print("This is Student class inheriting Mouse and Laptop")

obj=Student()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()


